#include <stdlib.h> 
#include <stdio.h>

/*
Compile: 
`gcc -m32 firsty.c -fno-stack-protector -o firsty -no-pie`
*/

int main(){

	// Create a local variable on the stack 
	char my_string[16];
	int x;
	
	// Set my cool variable 
	x = 0x11223344; 
	
	printf("Please insert a cool string: ");

	// Put data into my cool string 
	fgets(my_string,32,stdin);

	if(x != 0x11223344){
		FILE *fp; 
		int c; 
		fp = fopen("flag.txt","r");
		if(fp){
			while((c = getc(fp)) != EOF)
				putchar(c); 
			fclose(fp);
			return 0; 
		}else {
			puts("Unable to read flag");
		}
	}
	else{
		puts("Lit :fire");
	}
	return 0;

}
