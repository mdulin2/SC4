## Solutions 
- This is a list of solutions to various Linux challenges.

### first_ssh 
SSH to the server on port 2226 using the credentials ``first_ssh: first_ssh``. Once there, run ``cat flag.txt`` to get the flag. Simple as that!

### deeper 
The ‘grep’ command can be used to search for a string within a file. We will use this within the ``/etc/`` directory in order to find the flag. Since all flags are prefixed with ‘SC4{‘, we can use this as the search string. The command ``grep -r “SC4{” /etc/``  will output the flag in the results. 

Flag: SC4{grep_is_used_everywhere!}

