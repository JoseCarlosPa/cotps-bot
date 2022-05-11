from datetime import datetime
import sys
import os


def get_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time


def get_date():
    now = datetime.now()
    current_date = now.strftime("%d-%m-%Y")
    return current_date


def restart():
    print("argv: ", sys.argv)
    print("sys executable: ", sys.executable)
    print("Restarting...")
    os.execv(sys.executable, ['python'] + sys.argv)