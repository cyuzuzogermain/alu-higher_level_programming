#!/usr/bin/python3
"""
A Python script that sends a POST request to a
given URL with an email as a parameter
and prints the response body decoded in UTF-8.

Requirements:
- The script uses only `urllib` and `sys`.
- No argument validation is required.
- Must use a `with` statement when handling the response.
"""

import sys
import urllib.parse
import urllib.request

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Retrieve the URL and email from command-line arguments
    url = sys.argv[1]  # The first argument is the URL
    email = sys.argv[2]  # The second argument is the email

    # Encode the email as a URL parameter
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Use 'with' statement to ensure proper resource management
    with urllib.request.urlopen(url, data) as response:
        # Read the response body and decode it in UTF-8
        body = response.read().decode('utf-8')
        # Print the decoded response body to the console
        print(body)
