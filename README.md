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
