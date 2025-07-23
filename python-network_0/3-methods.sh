#!/bin/bash
# Sends an OPTIONS request and extracts the Allow header
curl -sI -X OPTIONS "$1" | grep -i ^Allow:
