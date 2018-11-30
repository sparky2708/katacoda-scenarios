Let's take a look at the disassembly again:

* `disassemble main`{{execute}}

Notice that there is an arrow `=>` which indicates where our breakpoint is currently. Some of the most common instructions are:

|Instruction|Meaning|Example|Explanation
|--------|---------|-------|-----------
|mov|Move 4 bytes|mov eax,ebx|Move 4 bytes in memory at ebx to eax
|push|Push on the hardward stack|push eax|Push eax on the stack
|pop|Pop from the hardware stack|pop eax|pop the top element of the stack to eax
|lea|Load Effective Address|lea edx,[ebx+0x04]|the value in ebx+0x04 is placed into edx
|jmp|Transfer control to instruction at memory location (if statements)|jmp 0x56555527|jump to the instruction at memory location specified
|call|Subroutine Call|call 0x565553b0|Call the subroutine at 0x565553b0
|ret|Return from Subroutine call|ret|Return from subroutine call

Let's closely examine some interesting lines in the disassembly. To step through the disassembly one would use `nexti` (Remember that the eip register contains the current instruction pointer so we can use it to look at the current instruction that is being printed):

* `nexti`{{execute}}
* `x/i $eip`{{execute}}

The instruction is to load the contents of the memory location `eax-0x19f8` into the register `edx` but what is being loaded into `edx`? Let's examine the memory location:

* `x/5x $eax-0x19f8`{{execute}}

Those look like some small values. They kind of look like ASCII text. Let's look at it another way:

* `x/5c $eax-0x19f8`{{execute}}

This looks like a string. Let's examine this as a string:

* `x/s $eax-0x19f8`{{execute}}

Aha, so this memory address stores our string and since strings are terminated by null the starting address of the string is being stored in edx. You can run `disassemble main`{{execute}} to view the disassembly again.