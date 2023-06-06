#!/bin/bash

docker start ex1-container

docker exec -it ex1-container pip list

#docker run -it ex1-image pip list > installed_packages.txt
