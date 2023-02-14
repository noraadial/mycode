#!/usr/bin/python3

import requests

# define the URL we want to use
POSTURL = "http://validate.jsontest.com/"

def main():
    # test data to validate as legal json
    # when a POST json= is replaced by the KEY "json"
    # the key "json" is mapped to a VALUE of the json to test
    # because the test item is a string, we can include whitespaces
    # The trickiest thing about this exercise is that the documentation 
    # does a poor job explaining that the proper formatting for your 
    # form data is {"json" : "the json to validate"}.
    mydata = {"json": "{'fruit': ['apple', 'pear'], 'vegetable': ['carrot']}" }

    # use requests library to send an HTTP POST
    resp = requests.post(POSTURL, data=mydata)

    # strip off JSON response
    # and convert to PYTHONIC LIST / DICT
    respjson = resp.json()

    # display our PYTHONIC data (LIST / DICT)
    print(respjson)

    # JUST display the value of "validate"
    print(f"Is your JSON valid? {respjson['validate']}")

if __name__ == "__main__":
    main()

