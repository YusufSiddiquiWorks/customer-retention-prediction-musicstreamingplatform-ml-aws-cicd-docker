#!/bin/bash
set -e

echo "Docker Pull Starting"

sudo docker pull yswork/musicstreaming-customerretention-prediction-ml:aws_prod_v1

echo "Docker Image "yswork/musicstreaming-customerretention-prediction-ml:aws_prod_v1" Pulled Successfully"

echo "Docker Run Starting on Port 7003 "

sudo docker run -d -p 7003:7003 yswork/musicstreaming-customerretention-prediction-ml:aws_prod_v1

echo "Docker Run Successfully Started on Port 7003 "
