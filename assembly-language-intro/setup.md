To start working with GDB let's setup the environment using a DOCKER image:

`docker run --cap-add=SYS_PTRACE --security-opt seccomp=unconfined -v $(pwd):/workspace -it daa82/gdb-katacoda /bin/bash`{{execute}}


Let's compile the code:

`gcc -g -m32 -o hello_world hello_world.c`{{execute}}


Let's start the debugger:

`gdb -q hello_world`{{execute}}
