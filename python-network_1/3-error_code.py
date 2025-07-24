#!/usr/bin/python3
"""
Fetch and display the body of a response from a given URL.

If an HTTPError occurs, prints: Error code: <HTTP status code>

Usage:
    python3 fetch_url.py <URL>
"""

import sys
from urllib import request, error

url = sys.argv[1]

try:
    # Send the request and read the response using a with-statement
    with request.urlopen(url) as response:
        print(response.read().decode('utf-8'))

except error.HTTPError as e:
    # Print error code if an HTTPError is raised
    print("Error code:", e.code)
