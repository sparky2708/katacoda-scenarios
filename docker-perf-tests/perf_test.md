
### Let's setup the local machine for performance testing:

`sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get install -y --no-install-recommends --allow-unauthenticated r-base-dev && Rscript -e "install.packages('microbenchmark', repos = 'http://cran.us.r-project.org')"`{{execute}}


Run the performance test on all the environments: 
	* local machine
`Rscript perf_test.R`{{execute}}

	* R-3.0.1 Environment:
`docker run -v $(pwd):/workspace -it daa82/ubuntu_r-3.0.1 Rscript perf_test.R`{{execute}}

	* Latest R Environment:
`docker run -v $(pwd):/workspace -it ubuntu-with-r Rscript perf_test.R`{{execute}}
