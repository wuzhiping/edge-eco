# share 
<pre>
docker network ls
       
docker run --rm -it --name=tools --network=xxx_yyyy busybox /bin/sh

docker-compose.yaml
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
version: "3"
services:
  tools:
    #image: busybox
    image: jonlabelle/network-tools
    container_name: tools
    command: ping openresty
    healthcheck:
      test: ["CMD", "curl", "-f", "http://opa:8181"]
      interval: 60s
      timeout: 60s
      retries: 3
  opa:
    image: openpolicyagent/opa:0.56.0
    restart: always
    #ports:
    #  - "8181:8181"
    command:
      - "run"
      - "--server"
      - "--set=decision_logs.console=true"

networks:
  default:
    external:
      name: axelor_default
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
</pre>
<pre>
docker run --rm -it shawoo/node:edge /bin/bash

node -v

export https_proxy="http://10.20.46.34:3128"

curl -o- https://a.feg.com.tw/nvm-v0.39.4-install.sh | bash

<strong>
su
source ~/.profile
</strong>
       
SHELL ["/bin/bash", "-c"]
       
nvm install 18
nvm use 18
nvm alias default 18
       
node -v
</pre>

# docker service create --name dtm -p 36789:36789 -p 36790:36790 --network my-network --constraint 'node.hostname==cds' yedf/dtm:latest

# docker pull mcr.microsoft.com/dotnet/runtime:6.0

# docker-compose
## shawoo/node:edge
## shawoo/node:edge-arm
# docker swarm
## shawoo/node:eco    
## shawoo/node:eco-arm

<pre>
docker network create -d overlay my-overlay

docker service ps --no-trunc ecoa

docker service create --name=consul -e CONSUL_BIND_INTERFACE=eth1 --network my-networ -p 8500:8500 --constraint 'node.hostname==cds' consul
docker service create --name=consul -e CONSUL_BIND_INTERFACE=eth0 --network my-network -p 8500:8500 consul

docker service create --name redisdb --network my-network redis
docker service create --name zipkin --network my-network -p 9411:9411 openzipkin/zipkin
docker service create --name placement --network my-network -p 50005:50005 daprio/dapr ./placement -port 50005

docker service create --name ecoa -e APP_ID=ecoa -e APP_PORT=3303 -p 3601:3500 --network my-network --constraint 'node.hostname==cds' shawoo/node:eco
docker service create --name ecob -e APP_ID=ecob -e APP_PORT=3303 -p 3602:3500 --network my-network --constraint 'node.hostname==cds' shawoo/node:eco

docker service create --name ecoc -e APP_ID=ecoc -e APP_PORT=3303 -p 3603:3500 --network my-network --constraint 'node.hostname==black-pearl' shawoo/node:eco-arm
docker service create --name ecod -e APP_ID=ecod -e APP_PORT=3303 -p 3604:3500 --network my-network --constraint 'node.hostname!=black-pearl' shawoo/node:eco
docker service create --name ecoe -e APP_ID=ecoe -e APP_PORT=8080 -p 3605:3500 --network my-network --constraint 'node.hostname==black-pearl' shawoo/java8:eco-arm

docker service create --name ecof -e APP_ID=ecof -e APP_PORT=5000 -p 3606:3500 --network my-network --constraint 'node.hostname==cds' shawoo/dotnet6:eco

docker plugin install weaveworks/net-plugin:latest_release
docker stack deploy --compose-file docker-compose.yml ecosys
</pre>

<pre>
docker plugin install vieux/sshfs
docker plugin install --grant-all-permissions vieux/sshfs

docker plugin ls

docker volume create --driver vieux/sshfs \
       -o sshcmd=ateam@redash.feg.cn:/home/ateam \
       -o password=123456  \
       sshvolume

docker run --rm -it -v sshvolume:/data nginx ls /data
</pre>
