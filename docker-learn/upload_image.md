To upload the image to docker first you need to login to your DOCKER account:

`docker login`{{execute}}

You might get the following WARNING:

WARNING! Your password will be stored unencrypted in /root/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

This can be ignored as Katacoda will destroy this session when you exit or
if enough time elapses. If you feel strongly about the warning then feel free to 
explore the credential store for docker using the link above.


Let's tag the image so it looks correct when we upload it to docker:
the general syntax should be: docker tag image username/repository:tag

This is the command that will run (inspect to make sure it is correct):

`echo docker tag ${DOCKER_IMAGE_NAME} ${DOCKER_USER}/${DOCKER_IMAGE_NAME}:latest`{{execute}}


Run the command:

`docker tag ${DOCKER_IMAGE_NAME} ${DOCKER_USER}/${DOCKER_IMAGE_NAME}:latest`{{execute}}


Let's check if the image was successfully created (you should see the new image alongside your old image:

`docker image ls | grep ${DOCKER_IMAGE_NAME}`{{execute}}


To publish the image to docker run:

`docker push ${DOCKER_USER}/${DOCKER_IMAGE_NAME}:latest`{{execute}}
