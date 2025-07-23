#!/bin/bash
# Send GET request and print body only if status is 200
curl -s -w "%{http_code}" -o /tmp/resp_body "$1" | grep -q "^200$" && cat /tmp/resp_body
