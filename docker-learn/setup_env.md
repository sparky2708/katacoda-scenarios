To start creating our docker image let's setup some environment variables
so this learning exercise can be applied to most docker projects

Setup the name of the docker image you will be working on:

`export DOCKER_IMAGE_NAME=sample-katacoda`{{execute}}

Setup your username and email as required for github:

`export GITHUB_USER=sparky2708`{{execute}}
`export GITHUB_EMAIL=daa82@columbia.edu`{{execute}}

`git config --global user.name ${GITHUB_USER} 
 && git config --global user.email ${GITHUB_EMAIL}`{{execute}}


Setup your username for docker:

`export DOCKER_USER=daa82`{{execute}}
