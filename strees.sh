#!/bin/bash

COUNT=$1
echo $COUNT

for i in $(seq 1 $COUNT);
do
    curl -X POST \
      'http://localhost:3000/api/v1/validate' \
      --header 'Accept: */*' \
      --header 'User-Agent: Thunder Client (https://www.thunderclient.com)' \
      --header 'Content-Type: application/json' \
      --data-raw '{
      "json_schema": "{\"name\": {\"type\": \"string\"}}",
      "json_body": "{\"name\": \"viccari\"}"
    }'
done

