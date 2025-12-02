import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from datetime import datetime


from xidle import get_idle_time
from logger import log

# define variables
shutdown_diff = 60*60*1000
hour = 19
minute = 0

def poweroff():
    with open("/proc/sys/kernel/sysrq", "w") as f:
        f.write("1")
    with open("/proc/sysrq-trigger", "w") as f:
        f.write("_reisuo")
        f.flush()

def service():
    log("###### Eta Shutdown {} ######".format(time.time()))
    for display in os.listdir("/tmp/.X11-unix/"):
        idle_time = get_idle_time(f":{display[1:]}")
        # check time diff and current time
        if idle_time > shutdown_diff:
            poweroff()
        # check current time
        now = datetime.now()
        nex = datetime(now.year, now.month, now.day, hour, minute)
        if  nex.timestamp() - now.timestamp() < 0:
            poweroff()
