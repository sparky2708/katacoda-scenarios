
### Let's find another image to load:

`docker search daa82`{{execute}}

Let's load the image that has R-3.0.1 installed:

`docker pull daa82/ubuntu_r-3.0.1`{{execute}}

What images are now available?

`docker image ls`{{execute}}

### We can run scripts in each environment:

	* R-3.0.1 Environment:
`docker run -v $(pwd):/workspace -it daa82/ubuntu_r-3.0.1 Rscript hello.R`{{execute}}

	* Latest R Environment:
`docker run -v $(pwd):/workspace -it ubuntu-with-r Rscript hello.R`{{execute}}
