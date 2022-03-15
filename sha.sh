#!/bin/bash

echo "# Generated SHA256 checksums"
echo "| File | SHA256 sum |" >> README.md
echo "|------|------------|" >> README.md
while read file path sha rest; do
    echo "| [$file]($path) | $sha |" >> README.md
done < <(find . -type f -name "*.apk" -printf "%f %P " -exec sha256sum {} \;)
