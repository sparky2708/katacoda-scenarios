To test the DOCKER image:

Let's look in our directory:
`ls -la`{{execute}}

Let's confirm no docker images are currently loaded:
`docker image ls`{{execute}}

Let's load the docker image we created:
`docker load < ubuntu-with-r.tar`{{execute}}

Verify:
`docker image ls`{{execute}}

Run the image:
`docker run -v $(pwd):/workspace -it ubuntu-with-r /bin/bash`{{execute}}

To Exit the image:
`exit`{{execute}}