#!/bin/bash

echo 'ALL_FILES = [' > index.js
find content | while read file; do
  echo -n .
  echo -n '  "' >> index.js
  echo -n "$file" | sed 's/"/\\"/' >> index.js
  echo '",' >> index.js
done

echo '];' >> index.js
echo
