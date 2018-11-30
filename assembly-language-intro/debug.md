Let's take a look at the disassembly again:

`disassemble main`{{execute}}

Notice that there is an arrow `=>` which indicates where our breakpoint is currently
Let's see what happens next by stepping through the code (Remember that the eip register contains the current instruction pointer):

`nexti`{{execute}}

`x/i $eip`{{execute}}

The instruction is `lea` which stands for `load efficient access` which basically means that we are loading the contents of the memory location `eax-0x19f8` into the register `edx` but what is being loaded into `edx`? Let's examine the memory location:

`x/5x $eax-0x19f8`{{execute}}

Those look like some small values. They kind of look like ASCII text. Let's look at it another way:

`x/5c $eax-0x19f8`{{execute}}

This looks like a string. Let's examine this as a string:

`x/s $eax-0x19f8`{{execute}}

Aha, so this memory address stores our string and since strings are terminated by null the starting address of the string is being stored in edx. You can run `disassemble main`{{execute}} to view the disassembly again.

Let's keep going:

`nexti`{{execute}}
`disassemble main`{{execute}}

The code executes `push edx` which just puts the value of the edx register (a pointer to the "Hello World" string on the hardware stack. 

