# Subdomain Fuzzing Tools for Enumerating Domain Fronting Proxies
### A python application used to prove concepts in https://mdsoar.org/handle/11603/28900

domainfuzzer.py uses customized HTTP headers within wget statements to request the file domainfuzzer.pages.dev/df.txt from another domain within the CloudFlare CDN.
For example: wget -q -O - -U http://www.nginx.com/df.txt --header "Host: domainfronter.pages.dev"

Subdomains are then fuzzed from the BitQuark Top 1000 Popular Subdomains list onto a user given domain and reports back all subdomains that successfully passed the df.txt file.

## Installation & Use:

Currently domainfuzzer.py is only supported on Linux machines.  It will function on Windows machines with the wget binary but the threading is currently only designed for Linux OS.

Download the repository  
Unzip the folder  
Run domainfronter.py using *python3 domainfronter.py*

## Meta

Charles Miller – https://www.linkedin.com/in/cmillercybsec/ – cmiller4@umbc.edu  
IS 701 - Independent Study: Domain Fronting  
Dr. Augusto Casas - UMBC: MS in Information Systems  

## Contribution

Dr. Michael Brown (UMBC) - Co-author of _Domain Fronting Through Microsoft Azure and CloudFlare: How to Identify Viable Domain Fronting Proxies_

Dr. Michael Pelosi (Texas A&M) - Co-authoer of _Domain Fronting Through Microsoft Azure and CloudFlare: How to Identify Viable Domain Fronting Proxies_

Zachary Miller - https://www.linkedin.com/in/zachary-miller-57a738141/  
10/17/22 - designed domainfronter.py threading capabilities and authored many unused line comments
