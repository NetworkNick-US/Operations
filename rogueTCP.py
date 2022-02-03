import time
import subprocess

#usually written to a file and searched with grep or related tool
While True:
    check = subprocess.getoutput("lsof - nPi tcp")
    print(str(check))
    time.sleep(1)
