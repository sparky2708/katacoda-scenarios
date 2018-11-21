To start working with let's setup the environment using a DOCKER image:

`docker run -v $(pwd):/workspace -it daa82/gdb-katacoda /bin/bash`{{execute}}


Let's compile the code:

`gcc -g -o hello_world hello_world.c`{{execute}}