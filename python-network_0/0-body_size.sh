#!/bin/bash
# Script that takes in a URL and displays the size in bytes of a 200 OK response body
curl -sL -w "%{http_code}" "$1" -o body.tmp | grep -q 200 && wc -c < body.tmp || echo 0
