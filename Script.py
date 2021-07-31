import TorStart
import VpnStart
import subprocess
import time

subprocess.run("python3 VpnStart.py", shell=True)
time.sleep(5)
subprocess.run("python3 TorStart.py", shell=True)
