
import pexpect

class SSHProxy(object):

    def __init__(self, address, username=None, password=None, timeout=30):
        self.address = address
        self.username = username
        self.password = password
        self.timeout = timeout

        self.connect()

    def connect(self):
        self.session = pexpect.spawn('ssh ' + self.username + '@' + self.address)
        match_index = self.session.expect(['(P|p)assword:', '(\$|\#):'], timeout=10)

        if match_index == 0:
            self.session.sendline (self.password + '\r')

        match_index = self.session.expect('(\$|\#)', timeout=10)

        print(match_index)

        self.session.sendline ('uname -a\r')
        match_index = self.session.expect('(\$|\#)', timeout=10)
        print (self.session.before)


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