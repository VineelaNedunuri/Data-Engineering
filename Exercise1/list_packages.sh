#!/bin/bash

 #docker run -it ex1-image pip list

 docker start ex1-container

 docker exec ex1-container pip list
