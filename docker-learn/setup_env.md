To start creating our docker image let's setup some environment variables
so this learning exercise can be applied to most docker projects

1. Setup the name of the docker image you will be working on:

	`export DOCKER_IMAGE_NAME=sample-katacoda`{{execute}}

2. Setup your username and email as required for github:

	A. `export GITHUB_USER=YOUR_GITHUB_USERNAME`
	
	B. `export GITHUB_EMAIL=YOUR_GITHUB_EMAIL`

	C. `git config --global user.name ${GITHUB_USER} 
 		&& git config --global user.email ${GITHUB_EMAIL}`{{execute}}


3. Setup your username for docker:

	A. `export DOCKER_USER=YOUR_DOCKER_USERNAME`
