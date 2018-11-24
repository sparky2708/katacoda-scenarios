To start creating our docker image let's setup some environment variables
so this learning exercise can be applied to most docker projects

1. Setup the name of the docker image you will be working on:

	`export DOCKER_IMAGE_NAME=NAME_OF_YOUR_DOCKER_IMAGE` (e.g. sample-katacoda)

2. Setup your username and email as required for github:

	A. `export GITHUB_USER=YOUR_GITHUB_USERNAME` (e.g. user123)
	
	B. `export GITHUB_EMAIL=YOUR_GITHUB_EMAIL` (e.g. user123@gmail.com)

	C. `git config --global user.name ${GITHUB_USER} && git config --global user.email ${GITHUB_EMAIL}`{{execute}}

	D. Check your configuration settings: `git config --list | grep -e 'user|image'`{{execute}}

3. Setup your username for docker:

	A. `export DOCKER_USER=YOUR_DOCKER_USERNAME` (e.g. user123)
	
4. Check your settings

	`set | grep -E '_USER|_IMAGE'{{execute}}
