"""
pip - pip installs packages - package installer

PyPi - Python Package index - list of external packages written in Python

WRITE a function that will open website provided as argument

create a list of websites

create a list of websites that DIDn't open properly (404)

save all these not opening websites into a file
save all  websites that are opening into another file



"""

import requests

response = requests.get("http://github.com")
