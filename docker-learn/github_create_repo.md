# If you already have a REPO in GITHUB called docker-images then skip to the next slide

There are 2 ways to create a GITHUB REPO:

1. You can login to your GITHUB and create a REPO using their web interface (call it "docker-images") OR

2. You can execute the following CURL script that will create a `docker-images` repo for you on GITHUB:

`curl -u ${GITHUB_USER} https://api.github.com/user/repos -d '{"name":"docker-images"}'{{execute}}
