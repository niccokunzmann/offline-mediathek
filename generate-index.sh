#!/bin/bash

(
  echo 'FILE_NAMES = []; F=function(s){FILE_NAMES.push(s)};'
  echo 'DESCRIPTIONS = {};'
) > index.js
find content | while read file; do
  echo -n .
  if echo "$file" | grep -qE '\.description$'; then
    (
      echo -n "DESCRIPTIONS['`echo \"$file\" | sed 's/'/\\''`'] = '"
      cat "$file" | sed 's/\n/\\n/' | sed "s/'/\\'/"
      echo "';"
    ) >> index.js
    break
  else
    (
      echo -n 'F("'
      echo "$file" | sed 's/"/\\"/'
      echo '");'
    ) >> index.js
  fi
done

echo '];' >> index.js
echo
