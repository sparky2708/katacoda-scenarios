packages <- c("microbenchmark")
if (length(setdiff(packages, rownames(installed.packages()))) > 0) {
  install.packages(setdiff(packages, rownames(installed.packages())))  
}
library(microbenchmark)

mean1 <- function(x) mean(x)
mean2 <- function(x) sum(x) / length(x)
x <- runif(1000)
stopifnot(all.equal(mean1(x), mean2(x)))

microbenchmark(
  mean1(x),
  mean2(x)
)