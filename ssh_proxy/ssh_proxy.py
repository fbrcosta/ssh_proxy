
import pexpect

class SSHProxy(object):

    def __init__(self, address, username=None, password=None, timeout=30):
        self.address = address
        self.username = username
        self.password = password
        self.timeout = timeout

    def read_until(self, regex, timeout=30):
        pass



#####################################################################
# Check for ssh program on system

import os

found = False
lst = os.environ["PATH"].split(os.pathsep)
i = 0

while i < len(lst) and found == False:
    path = lst[i].strip('"')
    exe_file = os.path.join(path, "ssh")
    if os.path.isfile(exe_file) and os.access(exe_file, os.X_OK):
        found = True
    i+=1

if not found:
    raise Exception("ssh is not installed.")

#####################################################################