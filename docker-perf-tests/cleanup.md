
List all containers that are running (only IDs)

`docker ps -aq`{{execute}}

Stop all running containers (if any are running)

`docker stop $(docker ps -aq)`{{execute}}

Remove all containers (if any are hanging)

`docker rm $(docker ps -aq)`{{execute}}

Remove all images (if any)

`docker rmi $(docker images -q)`{{execute}}
	
Check all images 

`docker image ls`{{execute}}