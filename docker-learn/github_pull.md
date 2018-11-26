First, let's pull the DOCKER image source code from github:

`git clone https://github.com/${GITHUB_USER}/docker-images.git`{{execute}}

Now let's see the source that was pulled from github and add the image we will be working with if it doesn't already exist:

`[ -d docker-images/${DOCKER_IMAGE_NAME} ] || mkdir docker-images/${DOCKER_IMAGE_NAME} 
&& cd docker-images/${DOCKER_IMAGE_NAME} 
&& touch Dockerfile 
&& ls`{{execute}}

Make sure that your DOCKER image source code appears as you had expected when you run the above statement.
