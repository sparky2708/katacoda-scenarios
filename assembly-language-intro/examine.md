At any point in time we can examine our environment. The command to examine is `x`. The syntax for `x` is:

`x/<num of tokens><token size format><output format> <value>`

The token size parameters:

|Token Size Format|Meaning
|------|-------
|b|Byte
|h|Half-word (2 bytes)
|w|Word (4 bytes)
|g|Giant (8 bytes)

The output formatting parameters:

|Output Format|Meaning
|------|------
|x|Integer
|o|Octal
|t|Binary
|c|Character
|s|String
|i|Machine Instruction
|d|Signed Decimal
|u|Unsigned Decimal

## Just to illustrate this concept let's look at the current instruction pointer (EIP):

To see the memory location:

* `x/2x $eip`{{execute}}

To see which instruction it points to:

* `x/i $eip`{{execute}}

## Let's now look at another register. 
For example we have an instruction `0x56555524 <+7>:     push   DWORD PTR [ecx-0x4]`. This pushes the value `ecx-4` on the hardware stack. Let's take a look at the ways to examine that memory address:

* `info register ecx` {{execute}}

Let's look at the 4 bytes before the address on the ecx register:

* `x/4xb $ecx -4`{{execute}}

We can also look at the memory location directly (see output from above command for the memory location):

* `x/4xb 0xffffd7ac`{{execute}}

We can also use the print command:

* `print $ecx - 4`{{execute}}

Since $1 was set to that location in memory we can now examine it using $1:

* `x/4xb $1`{{execute}}

Or we can look at the data as a 4-byte word:

* `x/4xw $1`{{execute}}

Notice that the bytes are reversed. This is due to the fact that the x86 architecture is little-endian meaning that multi-byte values are going to be reversed (least-significant byte first order)

