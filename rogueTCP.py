#!/usr/bin/python

import time
import subprocess

#usually written to a file and searched with grep or related tool
try:
    While True:
        check = subprocess.getoutput("lsof - nPi tcp")
        print(str(check))
        time.sleep(1)

except KeyboardInterrupt:
    print("\n\nKeyboardInterrupt. Exiting script.... (╯°□°)╯︵ ┻━┻\n\n")