
### Let's setup the local machine for performance testing:

`sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get install -y --no-install-recommends --allow-unauthenticated r-base-dev && Rscript -e "install.packages('microbenchmark', repos = 'http://cran.us.r-project.org')"`{{execute}}


Run the performance test on all the environments: 
	* local machine (Latest R Environment)
`Rscript perf_test.R`{{execute}}

	* Docker container (Latest R Environment):
`docker run -v $(pwd):/workspace -it ubuntu-with-r Rscript perf_test.R`{{execute}}

	* Docker container (R-3.0.1 Environment)
microbenchmark package not supported)
