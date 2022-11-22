#!/usr/bin/python3
"""
fetch https://intranet.hbtn.io/status; display response
"""

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alu-intranet.hbtn.io/status') as response:
        html = response.read()
