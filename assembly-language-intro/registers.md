Let's set a breakpoint in main:

`b main`{{execute}}

and run the code:

`run`{{execute}}

Let's look at the registers:

`info registers`{{execute}}

|Register|Meaning|Purpose
|----|----|---
|eax|Accumulator|Arithmetic Operations
|ecx|Counter|Shift/Rotate instructions and loops
|edx|Data|Arithment and I/O Operations
|ebx|Base|Pointer to data
|esp|Stack Pointer|Pointer to the top of the stack
|ebp|Stack Base Pointer|Pointer to the base of the stack
|esi|Source Pointer|Pointer to source in stream operations
|edi|Destination Pointer|Pointer to destination in stream operations
