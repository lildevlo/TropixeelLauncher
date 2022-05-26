from subprocess import call
import os

if os.name == "nt":
    call(["python", "nt.py"])

elif os.name == "posix":
    call(["python", "posix.py"])