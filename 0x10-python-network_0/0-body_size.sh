#!/bin/bash
# Display the size in Bytes of HTTP reponse using curl command
curl -s -o /dev/null -w "%{size_download}\n" $1 

