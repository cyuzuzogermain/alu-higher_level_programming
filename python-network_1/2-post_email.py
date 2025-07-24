#!/usr/bin/python3
"""
A Python script that sends a POST request to a given URL with an email as a parameter
and prints the response body decoded in UTF-8.

Requirements:
- The script uses only `urllib` and `sys`.
- No argument validation is required.
- Must use a `with` statement when handling the response.
"""

import sys
from urllib import request, parse

"""
Module
"""
# Get the URL and email from the command-line arguments
url = sys.argv[1]
email = sys.argv[2]

# Encode the data with the email as the only POST variable
post_data = parse.urlencode({'email': email}).encode('utf-8')

# Create a Request object with the URL and encoded data
req = request.Request(url, data=post_data)

# Send the request and read the response using a 'with' statement
with request.urlopen(req) as response:
    # Decode and print the response body as UTF-8
    print(response.read().decode('utf-8'))
