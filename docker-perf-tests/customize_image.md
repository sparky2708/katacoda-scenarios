# Let's customize the docker image

1. Let's select a base image:

	`from ubuntu:latest`{{execute}}

2. Let's have our image contain some libraries:

	* Upgrade Ubuntu:
		`run apt-get update && apt-get upgrade -y`{{execute}}
	* Install some tools: 
		`run apt-get install -y emacs`{{execute}}
	* Install R:
		`run apt-get install r-base`{{execute}}

3. Let's create a workspace directory in our image:

	`run mkdir /workspace
	 workdir /workspace`{{execute}}