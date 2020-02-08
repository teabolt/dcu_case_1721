# service to crash
service="$1"

# find ID of main process inside container
# `sudo docker container top $service`
pid="$2"

# connect to container and kill the main process
sudo docker-compose exec $service bash -c "kill -SIGINT $pid"
