#!/bin/bash
# Display size of body of response; Usage: ./0-body_size.sh 0.0.0.0:5000
curl -sI 
 | grep 'Content-Length:' | cut -f2 -d' '
