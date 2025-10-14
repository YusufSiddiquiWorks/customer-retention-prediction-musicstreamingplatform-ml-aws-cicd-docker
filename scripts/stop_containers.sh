echo "Stopping the Previous Container"

docker rm -f $(docker ps -q --filter "ancestor=yswork/musicstreaming-customerretention-prediction-ml:aws_prod_v1")

echo "Container Successfully Stopped"

echo "Now Starting Containers"