#!/bin/bash

#docker start ex1-container

#docker exec -it ex1-container pip list

#docker stop ex1-container

docker run -it ex1-image pip list > requirements.txt
