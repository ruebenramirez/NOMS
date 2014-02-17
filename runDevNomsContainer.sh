#!/bin/bash

sudo docker run -d -p 0.0.0.0:80:80 -v ./app:/home/docker/code/app NOMS
