import os
import sys
import time
import configparser

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from datetime import datetime

from xidle import get_idle_time
from logger import log

# define variables
shutdown_diff = 60*60*1000

config_test = """
[poweroff]
command=poweroff -f
timeout=3600000
hour=19
minute=0

[suspend]
command=systemctl suspend
timeout=3600000
hour=19
minute=0
"""

config = configparser.ConfigParser(config_test)

def check_time(hour, minute):
    now = datetime.now()
    nex = datetime(now.year, now.month, now.day, hour, minute)
    return nex.timestamp() - now.timestamp() < 0

def service():
    log("###### Eta Shutdown {} ######".format(time.time()))
    for display in os.listdir("/tmp/.X11-unix/"):
        idle_time = get_idle_time(f":{display[1:]}")
        for sec in config.sections():
            if idle_time > int(config[sec]["timeout"]):
                os.system(config[sec]["command"])
            if check_time(int(config[sec]["hour"]), int(config[sec]["minute"])):
                os.system(config[sec]["command"])

        if idle_time > shutdown_diff:
        # check current time
            poweroff()
