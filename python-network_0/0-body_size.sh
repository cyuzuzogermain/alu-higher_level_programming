#!/bin/bash

# Check if URL argument is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

URL=$1

# Use curl to fetch the response body silently and output its size in bytes
# -s: silent mode
# -L: follow redirects
# -o /dev/null: discard output
# -w '%{size_download}': write the size of the downloaded content

size=$(curl -s -L -o /dev/null -w '%{size_download}' "$URL")

echo "Response body size: $size bytes"
