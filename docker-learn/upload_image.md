To upload the image to docker first you need to login to your account:

`docker login`{{execute}}


Let's tag the image so it looks correct when we upload it to docker:
the general syntax should be: docker tag image username/repository:tag

This is the command that will run (inspect to make sure it is correct:

`echo docker tag ${DOCKER_IMAGE_NAME} ${DOCKER_USER}/${DOCKER_IMAGE_NAME}:latest`{{execute}}


Run the command:

`docker tag ${DOCKER_IMAGE_NAME} ${DOCKER_USER}/${DOCKER_IMAGE_NAME}:latest`{{execute}}


To publish the image to docker run:

`docker push ${DOCKER_USER}/${DOCKER_IMAGE_NAME}:latest`{{execute}}