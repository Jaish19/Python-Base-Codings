'''
SubProcess : Spawn and communicate with additional processes.

The subprocess module present in Python(both 2.x and 3.x) is used to 
run new applications or programs through Python code by creating new 
processes. It also helps to obtain the input/output/error pipes as well as 
the exit codes of various commands.

To execute different programs using Python two functions of the subprocess 
module are used:

subProcess.check_call()
subProcess.check_output()
'''

# http://python101.pythonlibrary.org/chapter19_subprocess.html

import subprocess

# Simple command
subprocess.call(['ls', '-1'], shell=True)

value = subprocess.call("Notepad.exe")
if value == 0:
	print "Success"
else:
	print "Fail"

-------------------------------------------------

data=subprocess.Popen(["ping", "www.yahoo.com"],stdout = subprocess.PIPE, stderr=subprocess.PIPE)
data = value.communicate()

-------------------------------------------------
