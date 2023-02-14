# Solution 1 - cats2
- This is a PHP site. 
- When viewing images, there is a parameter called ``path``. 
	- This takes a file from the operating system and displays this on the screen.
- When downloading text that is being displayed, there is no restrictions WHERE the file is accessed from!
- Hence, we can use ``/flag.txt`` in the path instead. 
- Flag: SC4{PhP_N0t_Againnnnnnnnn}

# Solution 2 - cats2
- PHAR deserialization vulnerability 
- TODO - more code execution via the URL being passed into fread without sanitization
- Resouces: 
	- https://pentest-tools.com/blog/exploit-phar-deserialization-vulnerability
	- https://vickieli.dev/insecure%20deserialization/php-phar/
	- https://blogs.keysight.com/blogs/tech/nwvs.entry.html/2019/06/26/exploiting_php_phar-PRD7.html