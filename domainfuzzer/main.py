import os

# Set user input as domain to fuzz
domain = input("Domain: ")
print("fuzzing top 1000 subdomains for "+domain+"...")

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
    x = 0
    while x < len(subdomains):
        cmd = "wget -q -O - -U demo http://"+subdomains[x]+"."+domain+"/df.txt --header \"Host: domainfronter.pages.dev\""
        res = os.system(cmd)
        if res == "domain fronting works!":
            print(subdomains[x])
        x += 1

# Future additions:
#   -Create a "domainfronter.pages.dev" variant on each of the popular CDNs
#   -User chooses from list of CDNs and program choose corresponding Host header