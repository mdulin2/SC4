# Solutions 
- This is a list of solutions to various *buffer overflow* challenges. 
- This is meant to ease students into the area, instead of drowning them on redirecting execution right away

## Firsty 
- The buffer is 16 characters long but accepts 32 characters. What happens if we write more than 16 characters? In particular, write 20 to get the flag.
- The stack is setup in the following way:
	- cool_string 
	- cool_int 
- So, when the string gets added with more than 16 characters, then **cool_int** is overwritten!
- Simply corrupting this value is enough to pass the challenge.


## Dead 
- A little bit more tricky! 
- The overflow is the same as before, with the same stack setup. 
- But, instead, we are using the overflow to **set** the integer value to a specific value! The char array is 8 bytes (1 * 8 = 8). Then, the integer is 4 bytes long.
- There are two main tricks to this: 
	- Writing the bytes properly 
	- Endianness
- Writing bytes: 
	- We are trying to write the integer 0xdeadbeef into memory.
	- The hex stream \xef is not a normal character. So, how do we write this? 
	- In Python (Python 2 at least) you can write escaped bytes with hex codes. 
	- Python example: print "\xef" 
		- This would print the literal byte 0xef
	- Common: 
		- Students will try to print the literal 0xdeadbeef. This will not work because this is intertuped as an integer.
- What is endianness? 

	- The ordering in which bytes are organized in memory. x86 is little Endian, meaning that the least significant byte appears first.
	- So, with 0xdeadbeef, we need to write this in the following way: 0xefbeadde. 
	- Remember, we are writing BYTES. 0xef is a SINGLE byte still.

- Final payload:
	- `python3 -c "import sys; sys.stdout.buffer.write(b'A' * 0x10 + b'\xef\xbe\xad\xde')" | ./dead`
	- Prints the proper bytes (with the Python hex escaping) and prints it in the proper Endinness.

## Auth
### Vuln Hunting:
- First, figure out the vuln. By putting in too many characters, a seg fault is created...Or, by reading the source code, there is no check on the input size of the buffer.
- Since the stack stores important information, overwriting it will cause a segmentation. Most importantly, the stack holds the *return address*. 
	- It is our goal to edit the *return address* to point to something that we want to call.
- Second, figure out the offset. This can be done in GDB, by manually looking at the stack during execution or using something like pattern.py. The offset should be 40 characters. The 40-43 characters are the return address on the stack.
- Third, go into GDB to figure out the address of the function "do_valid_stuff". Do this by typing in `disas do_valid_stuff`. This will give you an address to jump the flow of the program to.
    - I use `print do_valid_stuff`, then use the beginning address of the function to find where we need to go.

### Exploit
- Now, it is time to craft the exploit.
    - 1. Find the address of the serial number by using 'print &serial' while in the function 'validate_serial'. 
	- 2. Find the address of the return function pointer within this function. This can be done via running 'bt' (backtrace) and finding the location to jump back to in the program. This address from the backtrace will be on the stack. This is the location we're trying to overwrite. 
	- 3. Subtract the address from the serial number to the location of the RET pointer. Use this as the amount of filler bytes to write.
    - 4. Because the OS's Endian, we need to turn the Big Endian (i.e. 0x80485c3) into little Endian (i.e. 0xc3850408). Notice that this is PER byte. 
    - 5. Since we are writing raw values to the stack, we need to use hex code to do this. In order to do this, we must write the characters prefaced with `\x`. So, in the example, turn `0x565556b4` into `\xb4\x56\x55\x56`. Add this value to the payload.
    - 6. If all is done write, you should have redirected execution of the program to where the flag is at, displaying the flag.
    - 7. My final payload is `python3 -c "import sys; sys.stdout.buffer.write(b'A' * 0x1c + b'\xc3\x85\x04\x08')" | ./auth`
		- The exact address will differ from system to system though. 

### Further explanation:
- How the stack works:
    - On load of a function, the function address is pushed, followed by ebp then local variables (if needed).
    - Last on, first off style.
- Little Endian vs Big Endian:
    - https://chortle.ccsu.edu/AssemblyTutorial/Chapter-15/ass15_3.html
    - The location of the significance of the value. Most general number systems are little Endian (little end first) 1234 would be 1 x10^3+ 2x10^2 + 3x10^1 + 4x10^0 for instance. Big Endian would be 4x10^3....
- gdb:
    - This is a debugger
    - https://darkdust.net/files/GDB%20Cheat%20Sheet.pdf
