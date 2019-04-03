library(microbenchmark)

### FUNCTION 1 ###
mean1 <- function(x) mean(x)

### FUNCTION 2 ###
mean2 <- function(x) sum(x) / length(x)

#### MAIN CODE ####
x <- runif(5000000)
stopifnot(all.equal(mean1(x), mean2(x)))

microbenchmark(
  mean1(x),
  mean2(x)
)