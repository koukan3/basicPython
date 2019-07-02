# coding=utf-8

import subprocess

print("=====控制子进程的输入和输出: 启动进程并输入参数=====")
print("$nslookup www.python.org")
"""
    Run command with arguments and  Wait for command to complete or timeout, 
    then return the returncode attribute.

    The arguments are the same as for the Popen constructor.  Example:
    retcode = call(["ls", "-l"])
    """
r = subprocess.call(['nslookup','www.python.org'])
print("Exit code: ",r)

print("=====控制子进程的输入和输出: 启动进程，后续输入参数=====")
print("$nslookup")
p = subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
'''
The optional "input" argument should be data to be sent to the child process .
(if self.universal_newlines is True, this should be a string; 
 if it is False, "input" should be bytes)
 by default, universal_newlines = False
'''
# p.communicate : return (stdout, stderr)
getStdout,getStderr = p.communicate(b'set q=mx\npython.org\nexit\n')
print("stdout: %s \n stderr: %s"%(getStdout.decode('gbk'),getStderr.decode('gbk')))
print("return code: ",p.returncode)


