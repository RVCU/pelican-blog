#!/bin/bash
echo "Please enter password to encrypt the encrypted pages with"
read -r password
find content/ -type f -name "*.md" -exec sed -i "s/<PASSWORD>/$password/g" {} +
