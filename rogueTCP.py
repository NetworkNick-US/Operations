import time
import subprocess

While True:
    check = subprocess.getoutput("lsof - nPi tcp")
    print(str(check))
    time.sleep(1)