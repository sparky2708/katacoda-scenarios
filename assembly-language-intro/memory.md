Let's keep going:

* `nexti`{{execute}}
* `x/i $eip`{{execute}}

The code executes `push edx` which just puts the edx register on the stack. This shows how a parameter is getting passed to the `printf` function. It is pushed on the stack and sunbsequently used within the printf function.

How is memory organized:

|Address Seq|Segment Type|Purpose|Growth|
|--------|--------|--------|----|
|Low Address|Code Segment|Stores instructions of program
||Data Segment|Stores global or static variables initialized with data|
||bss Segment|Stores global or static variables not initialized
||Heap Segment|Dynamically allocated space. Must be allocated with malloc()/free()|Grows to higher memory addresses
|High Address|Stack Segment|Contains local variables (declared and defined in function)|Grows to lower memory addresses


Here is an example of code that shows the memory segment:

```c
#include <stdio.h>

int global_var;
int global_init_var = 10;

void someFunc() {
	int stack_var;
    //this variable is on the stack	
	printf("function stack_var is at address: 0x%O8x\n", &stack_var);
}

int main() {
	int stack_var; 
	static int static_init_var = 5;
	static int static_var;
	int *heap_var_ptr;
	
	heap_var_ptr = (int *) malloc(sizeof(int))
	
	//these variables are in the data segment
	printf("global_init_var is at address: 0x%O8x\n", &global_init_var);
	printf("static_init_var is at address: 0x%O8x\n", &static_init_var);

	//these variables are in the bss segment
	printf("global_var is at address: 0x%O8x\n", &global_var);
	printf("static_var is at address: 0x%O8x\n", &static_var);
	
	//this variable is in the heap segment
	printf("heap_var is at address: 0x%O8x\n", &heap_var_ptr);
	
	//these variables are in the stack segment
	printf("stack_var is at address: 0x%O8x\n", &stack_var);
	someFunc();
}
```
