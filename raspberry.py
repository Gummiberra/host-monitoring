import os
import socket
from gpiozero import CPUTemperature
import psutil


def get_manufacturer_name() -> str:
    with open('/proc/device-tree/model') as f:
        model = f.read()
    return model[0:12]

def get_model_name():
    with open('/proc/device-tree/model') as f:
        model = f.read()
    return model

def get_hostname():
    hostname = socket.gethostname()
    return hostname

def get_cpu_temp():
    cpuTemp = CPUTemperature()
    return cpuTemp.temperature

def get_cpu_usage():
    cpu = psutil.cpu_percent()
    return cpu

def get_cpu_clockspeed():
    freq = psutil.cpu_freq()
    return freq

def get_cpu_cores():
    cpuCore = psutil.cpu_count()
    return cpuCore

def get_memory_usage():
    memory = psutil.virtual_memory()
    return (memory.percent)

def get_memory_total():
    memory = psutil.virtual_memory()
    total = (round(memory.total/1024.0/1024.0,1))
    return total

def get_memory_available():
    memory = psutil.virtual_memory()
    available = (round(memory.available/1024.0/1024.0,1))
    return available

def get_disk_usage():
    disk = psutil.disk_usage('/')
    return disk.percent

def get_disk_total():
    disk = psutil.disk_usage('/')
    total = round(disk.total/1024.0/1024.0/1024.0,1)
    return total

def get_disk_available():
    disk = psutil.disk_usage('/')
    free = round(disk.free/1024.0/1024.0/1024.0,1)
    return free

def get_uptime():
    uptime = os.popen("awk '{print $1}' /proc/uptime").readline()
    return round(float(uptime)/3600/24)