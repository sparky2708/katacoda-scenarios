
Put the following in the Dockerfile editor to create your own Docker image
1. Let's select a base image:

	`from ubuntu:latest`

2. Let's have our image contain some libraries:

	* Upgrade Ubuntu:
		`ENV TZ=US
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
run apt-get update && apt-get upgrade -y`
	* Install some tools: 
		`run apt-get install -y emacs`
	* Install R:
		`run apt-get install -y --no-install-recommends --allow-unauthenticated r-base-dev`
	* Install R packages:
		`run Rscript -e "install.packages('microbenchmark')"`

3. Let's create a workspace directory in our docker image:

	`run mkdir /workspace
workdir /workspace`