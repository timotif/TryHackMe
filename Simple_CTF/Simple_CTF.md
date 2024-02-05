
# Simple CTF
https://tryhackme.com/room/easyctf

- I start with nmap: there's a HTTP server running.
- gobuster finds the folder /simple
- In that page I see (bottom left) I see
> © Copyright 2004 - 2024 - CMS Made Simple   This site is powered by
> [CMS Made Simple](http://www.cmsmadesimple.org) version 2.2.8

- Google "CMS made simple 2.2.8 exploit": I find https://www.exploit-db.com/exploits/46635 and this https://nvd.nist.gov/vuln/detail/CVE-2019-9053
-  I downloaded the exploit python script. It didn't work: syntax error
With some research I realized that `print "something"` without () is a syntax of python2, so I tried to run the script with python2: still didn't work.
termcolor wasn't installed for python2, it was for python3, pip2 didn't work, after many attempts I just copied 

sudo cp -r /usr/lib/python3/dist-packages/termcolor.py /usr/lib/python2.7/dist-packages

and 

    sudo cp -r /usr/lib/python3/dist-packages/termcolor-1.1.0.egg-info/ /usr/lib/python2.7/dist-packages
- Now the script works: I get the user and password
- I saw earlier with nmap that SSH is listening on port 2222 so I connect with the credentials I found
- running `sudo -l` I get the list of commands the user can run with high privilege: it turns out that vim is one of them.
- At the sudo section of this https://gtfobins.github.io/gtfobins/vim/ I find that I can get a shell from vim with sudo vim -c ':!/bin/sh'
- Done: I'm root
