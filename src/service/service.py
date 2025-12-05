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

[TIMED_SUSPEND]
enabled = False
hour = 00
minute = 00

[TIMED_SHUTDOWN]
enabled = False
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
    log("idle_time: {}".format(idle_time))
    # timed shutdown
    if "TIMED_SHUTDOWN" in config and "enabled" in config["TIMED_SHUTDOWN"]:
        if config["TIMED_SHUTDOWN"]["enabled"].lower() == "true":
            if "hour" in config["TIMED_SHUTDOWN"] and "minute" in config["TIMED_SHUTDOWN"]:
                hour = int(config["TIMED_SHUTDOWN"]["hour"])
                minute = int(config["TIMED_SHUTDOWN"]["minute"])
                if idle_time > (hour*3600 + minute * 60)*1000:
                    print("timed shutdown")
                    os.system("poweroff -f")
    # timed shutdown
    if "TIMED_SUSPEND" in config and "enabled" in config["TIMED_SUSPEND"]:
        if config["TIMED_SUSPEND"]["enabled"].lower() == "true":
            if "hour" in config["TIMED_SUSPEND"] and "minute" in config["TIMED_SUSPEND"]:
                hour = int(config["TIMED_SUSPEND"]["hour"])
                minute = int(config["TIMED_SUSPEND"]["minute"])
                if idle_time > (hour*3600 + minute * 60)*1000:
                    print("timed suspend")
                    os.system("systemctl suspend")
    # auto shutdown
    if "AUTO_SHUTDOWN" in config and "enabled" in config["AUTO_SHUTDOWN"]:
        if config["AUTO_SHUTDOWN"]["enabled"].lower() == "true":
            if "hour" in config["AUTO_SHUTDOWN"] and "minute" in config["AUTO_SHUTDOWN"]:
                hour = int(config["AUTO_SHUTDOWN"]["hour"])
                minute = int(config["AUTO_SHUTDOWN"]["minute"])
                if check_time(hour, minute):
                    print("auto shutdown")
                    os.system("poweroff -f")
