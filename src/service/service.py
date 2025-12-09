import os
import sys
import time
import configparser

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from datetime import datetime

from xidle import get_idle_time
from logger import log

"""
[AUTO_SHUTDOWN]
enabled = False
hour = 01
minute = 00

[TIMED_SHUTDOWN]
mode = "shutdown"
hour = 00
minute = 00
"""

CONFIG_FILE = "/etc/pardus/eta-shutdown.conf"
config = configparser.ConfigParser()
config.read(CONFIG_FILE)

def check_time(hour, minute):
    now = datetime.now()
    nex = datetime(now.year, now.month, now.day, hour, minute)
    print(now, nex)
    return nex.timestamp() - now.timestamp() < 0



def service():
    log("###### Eta Shutdown {} ######".format(time.time()))
    idle_time = -1
    for display in os.listdir("/tmp/.X11-unix/"):
        idle = get_idle_time(f":{display[1:]}")
        if idle_time < idle or idle_time < 0:
            idle_time = idle
    print("idle_time: {}".format(idle_time))
    # timed shutdown
    mode = config["TIMED_SHUTDOWN"]["mode"]
    if mode != "none":
        hour = int(config[sec]["hour"])
        minute = int(config[sec]["minute"])
        req_idle = (hour*3600 + minute * 60)*1000
        print("req_idle:", req_idle)
        if idle_time > req_idle:
            if mode == "shutdown":
                os.system("poweroff -f")
            elif mode == "suspend":
                os.system("systemctl suspend")
    # auto shutdown
    if config["AUTO_SHUTDOWN"]["enabled"].lower() == "true":
        hour = int(config["AUTO_SHUTDOWN"]["hour"])
        minute = int(config["AUTO_SHUTDOWN"]["minute"])
        if check_time(hour, minute):
            print("auto shutdown")
            os.system("poweroff -f")
