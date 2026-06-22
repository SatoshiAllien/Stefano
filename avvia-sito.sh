#!/bin/bash
echo "Stefano Ciancimino — http://localhost:8081"
cd "$(dirname "$0")"
python3 -m http.server 8081
