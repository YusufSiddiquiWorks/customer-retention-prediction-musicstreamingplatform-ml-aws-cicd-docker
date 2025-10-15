#!/bin/bash
set -e

echo "Docker Pull Starting"

docker pull yswork/music-customer-churn-prediction-ml:aws_prod_v1

echo "Docker Image "yswork/music-customer-churn-prediction-ml:aws_prod_v1" Pulled Successfully"

echo "Docker Run Starting on Port 7003 "

docker run -d -p 7003:7003 yswork/music-customer-churn-prediction-ml:aws_prod_v1

echo "Docker Run Successfully Started on Port 7003 "
