If you haven't created a repo yet to store all your images on github, let's do that now:

1. We're going to create a local directory we'll call `docker-images` (that will be our repo-name in github)

`mkdir docker-images && cd docker-images`{{execute}}

2. Initialize this as your base repository

`git init`{{execute}}

3. Inside let's create our first git image source directory where we will store the source code for our DOCKER image:

`mkdir ${DOCKER_IMAGE_NAME}`{{execute}}

4. Add everything to git and commit locally

`git add . && git commit -m "Creating initial image"`{{execute}}

5. Declare the URL to the remote repository and verify it was created successfully

`git remote add origin https://github.com/${GITHUB_USER}/docker-images.git && git remote -v`{{execute}}

6. Push to github (will ask for your github username/password):

`git push origin master`{{execute}}