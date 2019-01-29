TESTING MULTIPLE DOCKER images on the same host:

Let's find another image to load:

`docker search daa82`{{execute}}

Let's load the image that has R-3.0.1 installed:

`docker pull daa82/ubuntu_r-3.0.1`{{execute}}

What images are now available?

`docker image ls`{{execute}}

Let's verify the images (to exit the image: `exit`{{execute}})

	* R-3.0.1 Environment:
`docker run -v $(pwd):/workspace -it ubuntu_r-3.0.1 R --version`{{execute}}

	* Latest R Environment:
`docker run -v $(pwd):/workspace -it ubuntu-with-r R --version`{{execute}}

We can also run scripts in each environment:

	* R-3.0.1 Environment:
`docker run -v $(pwd):/workspace -it ubuntu_r-3.0.1 R -f perf_test.R --version`{{execute}}

	* Latest R Environment:
`docker run -v $(pwd):/workspace -it ubuntu-with-r R -f perf_test.R --version`{{execute}}


To Exit the image:
