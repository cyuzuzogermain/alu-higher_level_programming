#!/bin/bash
# Print size of response body in bytes from given URL using curl
curl -s -L -o /dev/null -w '%{size_download}\n' "$1"
