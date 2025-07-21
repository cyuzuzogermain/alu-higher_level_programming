#!/bin/bash
# Script that takes in a URL and displays the size in bytes of the response body
curl -s "$1" | wc -c
