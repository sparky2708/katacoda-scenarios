To build the DOCKER image execute:

`docker build -t ubuntu-with-r .`{{execute}}


To see what images are currently built you can run the following:

`docker image ls`{{execute}}


Let's save the image so we can use it locally:

`docker save ubuntu-with-r > ubuntu-with-r.tar`{{execute}}


Let's cleanup so our environment is clean:

`docker rmi $(docker images -q)`{{execute}}