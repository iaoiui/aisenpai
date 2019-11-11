#!/bin/bash

docker build -t toys_war_prod:1 .
docker run -it -d --name toys-war-prod-1 -p 5555:3000 \
	toys_war_prod:1
