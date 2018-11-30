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