#!/bin/bash

docker build -t aisenpai_prod:1 .
docker run -it -d --name aisenpai-prod-1 -p 5555:3000 \
	aisenpai_prod:1
