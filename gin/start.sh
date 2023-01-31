#!/bin/bash
fresh &

export DARP_HOST_IP=$(nslookup $APP_ID | grep "Address: " | awk '{print $2}' | tr -d 'addr:')

echo $DAPR_HOST_IP

dapr run --app-id $APP_ID --app-port 8080 --dapr-http-port 3500 --components-path /dapr/components --config /dapr/config.yaml --placement-host-address placement:50005

