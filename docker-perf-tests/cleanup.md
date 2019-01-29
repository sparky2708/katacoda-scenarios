# Let's clean up any images/containers that are in this environment so we have a clean environment to work in:

List all containers (only IDs)

`docker ps -aq`{{execute}}

Stop all running containers

	`docker stop $(docker ps -aq)`{{execute}}

Remove all containers

	`docker rm $(docker ps -aq)`{{execute}}

Remove all images

	`docker rmi $(docker images -q)`{{execute}}
	
Check all images

	`docker image ls`{{execute}}