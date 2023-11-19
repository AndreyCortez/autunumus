import can
import os
import time

def can_init():
    os.system("ip link set can0 down")
    time.sleep(1)

    os.system("ip link set can0 type can bitrate 500000")
    time.sleep(1)

    os.system("ip link set can0 up")
    time.sleep(1)

def can_deactivate():
    os.system("ip link set can0 down")
    time.sleep(1)

def can_send_message():
    pass