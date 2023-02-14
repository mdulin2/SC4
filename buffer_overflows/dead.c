#include <stdlib.h> 
#include <stdio.h>

/*
Compile: 
`gcc -m32 dead.c -fno-stack-protector -o dead -no-pie` 

socat TCP-LISTEN:2323,reuseaddr,fork EXEC:"./dead"
*/

int main(){

	setvbuf(stdout, NULL, _IONBF, 0);

	// Create a local variable on the stack 
	char my_string[16];
	int x;
	
	// Set my cool variable 
	x = 0x11223344; 
	
	printf("Please insert a cool string: ");

	// Put data into my cool string 
	fgets(my_string,32,stdin);

	if(x == 0xdeadbeef){
		FILE *fp; 
		int c; 
		fp = fopen("flag.txt","r");
		if(fp){
			while((c = getc(fp)) != EOF)
				putchar(c); 
			fclose(fp);
			return 0; 
		}
		else {
			puts("Unable to read flag");
		}
	}
	else{
		puts("Lit :fire");
	}
	return 0;

}
