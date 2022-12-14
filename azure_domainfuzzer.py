import _thread
import time
import threading
import subprocess
import sys
import time
import termcolor
from termcolor import colored, cprint

# Set user input as domain to fuzz
domain = input("Domain: ")
num_thread = 10
print("fuzzing top 1000 subdomains for", end=" ")
termcolor.cprint(domain, "red", attrs=["bold"], end="")
print("...")

# Open bitquark top 100 subdomains and read each line into a list
#
# Updates are regularly made to this list on bitquark github
# https://github.com/bitquark/dnspop
with open("bitquark_20160227_subdomains_popular_1000") as subdomains:
    subdomains = subdomains.readlines()

# Scrub new line character and parse to string
for i in range(len(subdomains)):
    subdomains[i] = str(subdomains[i])
    subdomains[i] = subdomains[i].replace('\n', '')

# Run wget command with custom HTTP header pointed towards CloudFlare CDN instance
termcolor.cprint("Successful subdomains:", "green",attrs=["bold"])

# def runWget(subDomains, domain):

class thread_wget(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        # Add loop into this function to keep popping through the stack
        global subdomains
        while len(subdomains) > 0:
            subDomain = subdomains.pop()
            cmd = "wget -q --connect-timeout=2 -O - -U demo http://" + subDomain + "." + domain + "/df.txt --header \"Host: delightful-sand-056d73f0f.2.azurestaticapps.net\""
            sp = subprocess.Popen(str(cmd), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                  universal_newlines=True)
            rc = sp.wait()
            out, err = sp.communicate()

            if out == "domain fronting works!":
                termcolor.cprint("   " + subDomain + "." + domain, "blue")
            elif len(subdomains) % 100 == 0:
                print(str(len(subdomains))+" subdomains remaining...")


for i in range(0, num_thread):
    thread_wget(str(i)).start()

# Future additions:
#   -Create a "domainfronter.pages.dev" variant on each of the popular CDNs
#   -User chooses from list of CDNs and program choose corresponding Host header
