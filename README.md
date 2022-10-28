# Subdomain Fuzzing Tools for Enumerating Domain Fronting Proxies
> Python application used to prove concepts in https://docs.google.com/document/d/1NbrhF-ZcsJPxDE-pvl9mq373EM_iavCW/edit?usp=sharing&ouid=111027394185246946986&rtpof=true&sd=true

[![NPM Version][npm-image]][npm-url]
[![Build Status][travis-image]][travis-url]
[![Downloads Stats][npm-downloads]][npm-url]

domainfronter.py uses customized HTTP headers within wget statements to request the file domainfronter.pages.dev/df.txt from another domain within the CloudFlare CDN.
For example: wget -q -O - -U http://www.nginx.com/df.txt --header "Host: domainfronter.pages.dev"

Subdomains are then fuzzed from the BitQuark Top 1000 Popular Subdomains list onto a user given domain and reports back all subdomains that successfully passed the df.txt file.

## Installation & Use:

Currently domainfronter.py is only support on Linux machines.  It will function on Windows machines with the wget binary but the threading is currently only designed for Linux OS.

Download the repository
Unzip the folder
Run domainfronter.py using *python3 domainfronter.py*

## Meta

Charles Miller – https://www.linkedin.com/in/cmillercybsec/(https://twitter.com/dbader_org) – cmiller4@umbc.edu
IS 701 - Independent Study: Domain Fronting
Dr. Augusto Casas - UMBC: MS in Information Systems

## Contribution

Zachary Miller - https://www.linkedin.com/in/zachary-miller-57a738141/
  10/17/22 - designed domainfronter.py threading capabilities and authored many unused line comments
