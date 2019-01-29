LOADING and TESTING the DOCKER image:

Let's look in our directory:

`ls -l`{{execute}}

Let's confirm no docker images are currently loaded:

`docker image ls`{{execute}}

Let's load the docker image we created:

`docker load < ubuntu-with-r.tar`{{execute}}

Verify our image is loaded:

`docker image ls`{{execute}}

Create a container from the image and use it interactively:

`docker run -v $(pwd):/workspace -it ubuntu-with-r /bin/bash`{{execute}}

Alternatively you can just run your script in the container:

`docker run -v $(pwd):/workspace -it ubuntu-with-r R -f perf_test.R`{{execute}}

To Exit the image:

`exit`{{execute}}