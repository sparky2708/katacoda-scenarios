TESTING the DOCKER image:

Let's look in our directory:
	* `ls -l`{{execute}}

Let's confirm no docker images are currently loaded:
	* `docker image ls`{{execute}}

Let's load the docker image we created:
	* `docker load < ubuntu-with-r.tar`{{execute}}

Verify our image is loaded:
	* `docker image ls`{{execute}}

Use the image to create a container and run in it:
	* `docker run -v $(pwd):/workspace -it ubuntu-with-r /bin/bash`{{execute}}

To Exit the image:
	* `exit`{{execute}}