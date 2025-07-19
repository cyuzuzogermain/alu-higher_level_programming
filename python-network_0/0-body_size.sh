#!/bin/bash
# Get response body size in bytes using curl for a given URL
curl -s -o /dev/null -w "GET / => \"$(curl -s $1)\"\n" $1
