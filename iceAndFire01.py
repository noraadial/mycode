#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests

AOIF = "https://www.anapioficeandfire.com/api"

def main():
    ## Send HTTPS GET to API
    gotresp = requests.get(AOIF)

    ## Decode response
    got_dj = gotresp.json()

    ## print response
    print(got_dj)

    ## display only keys - great for seeing what's there for lookup
    print(got_dj.keys())

if __name__ == "__main__":
    main()
