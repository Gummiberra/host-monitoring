# MQTT Server config
mqtt_ip = "ip"
mqtt_port = "1883"
mqtt_username = "user"
mqtt_password = "password"
mqtt_topic = "monitor"

# Homeassistant config
home_assistnat_discovery = True
node = [{
    "Cpu_Temperature" : True,
    "Cpu_Usage" : True,
    "Cpu_Cores" : True,
    "Cpu_Clockspeed" : True,
    "Memory_Usage" : True,
    "Memory_Total" : True,
    "Memory_Available" : True,
    "Disk_Usage" : True,
    "Disk_Total" : True,
    "Disk_Available" : True,
    "Host_Uptime" : True
}]

# Host config
host_type = "Raspberry Pi" # Raspberry Pi, Linux, Windows