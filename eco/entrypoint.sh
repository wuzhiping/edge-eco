#!/bin/sh

# Make sure config.yaml exists

# Specify weave network interface
# It's needed since dapr use multicast, so make sure that you'd attached a weave network
# to this container with multicast enabled weave flag
# export DAPR_HOST_IP=$(ifconfig ethwe0 | grep "inet " | awk '{print $2}' | tr -d 'addr:')

cd /opt/bpm
pm2 start bpm.js -i 2
pm2 logs

#export DARP_HOST_IP=$(nslookup $APP_ID | grep "Address: " | awk '{print $2}' | tr -d 'addr:')
#dapr run \
#    --app-id "${APP_ID}" \
#    --app-port "${APP_PORT}" \
#    ---dapr-grpc-port 50000 \
#    --components-path /dapr/components \
#    --config /dapr/config.yaml
#    --placement-host-address placement:50005 \
#    -- "$@"
