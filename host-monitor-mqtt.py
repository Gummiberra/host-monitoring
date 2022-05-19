import paho.mqtt.client as mqtt
import config
import json
import time
import raspberry as pi
import logging

Log_Format = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = config.log_file,
                    format = Log_Format,
                    level = config.log_level)

logger = logging.getLogger()

logger.debug("Reading config")
node = config.node
node = json.loads(node)

def config_payload(object):
    logger.debug("Generating config payload for: " + object)
    data = {
        "state_topic": "",
        "icon": "",
        "name": "",
        "unique_id": "",
        "unit_of_measurement": "",
        "device": {
            "identifiers": [hostname],
            "manufacturer": manufacturer,
            "model": model,
            "name": hostname
        }
    }

    data["state_topic"] = config.mqtt_topic + "/" + hostname + "/" + object
    data["unique_id"] = hostname + "_" + object

    if object == "cpu_temp":
        data["icon"] = "mdi:thermometer"
        data["name"] = hostname + " CPU Temperature"
        data["unit_of_measurement"] = "°C"
    elif object == "cpu_usage":
        data["icon"] = "mdi:chart-donut-variant"
        data["name"] = hostname + " CPU Usage"
        data["unit_of_measurement"] = "%"
    elif object =="cpu_clockspeed":
        data["icon"] = "mdi:sine-wave"
        data["name"] = hostname + " CPU Clockspeed"
        data["unit_of_measurement"] = "Mhz"
    elif object =="cpu_cores":
        data["icon"] = "mdi:cpu-64-bit"
        data["name"] = hostname + " CPU Cores"
        data["unit_of_measurement"] = "Cores"
    elif object =="memory_usage":
        data["icon"] = "mdi:memory"
        data["name"] = hostname + " Memory Usage"
        data["unit_of_measurement"] = "%"
    elif object =="memory_total":
        data["icon"] = "mdi:memory"
        data["name"] = hostname + " Memory Total"
        data["unit_of_measurement"] = "MB"
    elif object =="memory_available":
        data["icon"] = "mdi:memory"
        data["name"] = hostname + " Memory Available"
        data["unit_of_measurement"] = "MB"
    elif object =="disk_usage":
        data["icon"] = "mdi:harddisk"
        data["name"] = hostname + " Disk Usage"
        data["unit_of_measurement"] = "%"
    elif object =="disk_total":
        data["icon"] = "mdi:harddisk"
        data["name"] = hostname + " Disk Total"
        data["unit_of_measurement"] = "GB"
    elif object =="disk_available":
        data["icon"] = "mdi:harddisk"
        data["name"] = hostname + " Disk Available"
        data["unit_of_measurement"] = "GB"
    elif object =="host_uptime":
        data["icon"] = "mdi:raspberry-pi"
        data["name"] = hostname + " Host Uptime"
        data["unit_of_measurement"] = "days"

    logger.debug("Config payload for " + object + " generated. \n" + data)
    return json.dumps(data)

def send_mqtt_update(hostname = "",cpu_temp = 0, cpu_usage = 0, cpu_cores = 0,cpu_clockspeed = 0, memory_usage = 0, memory_total = 0, memory_available = 0, disk_usage = 0, disk_total = 0, disk_available = 0, host_uptime = 0):
    logger.debug("Starting MQTT Client")
    mqClient = mqtt.Client()
    mqClient.username_pw_set(config.mqtt_username,config.mqtt_password)
    mqClient.connect(config.mqtt_ip,int(config.mqtt_port))
    logger.debug("MQTT Client connected")

    
    if config.home_assistnat_discovery:
        logger.info("Home assistant discovery configured")
        if node["Cpu_Temperature"]:
            mqClient.publish("homeassistant/sensor/" + config.mqtt_topic + "/" + hostname + "_cpu_temp/config", config_payload("cpu_temp"))
            time.sleep(1);
        if node["Cpu_Usage"]:
            mqClient.publish("homeassistant/sensor/" + config.mqtt_topic + "/" + hostname + "_cpu_usage/config", config_payload("cpu_usage"))
            time.sleep(1);
        if node["Cpu_Cores"]:
            mqClient.publish("homeassistant/sensor/" + config.mqtt_topic + "/" + hostname + "_cpu_cores/config", config_payload("cpu_cores"))
            time.sleep(1);
        if node["Cpu_Clockspeed"]:
            mqClient.publish("homeassistant/sensor/" + config.mqtt_topic + "/" + hostname + "_cpu_clockspeed/config", config_payload("cpu_clockspeed"))
            time.sleep(1);
        if node["Memory_Usage"]:
            mqClient.publish("homeassistant/sensor/" + config.mqtt_topic + "/" + hostname + "_memory_usage/config", config_payload("memory_usage"))
            time.sleep(1);
        if node["Memory_Total"]:
            mqClient.publish("homeassistant/sensor/" + config.mqtt_topic + "/" + hostname + "_memory_total/config", config_payload("memory_total"))
            time.sleep(1);
        if node["Memory_Available"]:
            mqClient.publish("homeassistant/sensor/" + config.mqtt_topic + "/" + hostname + "_memory_available/config", config_payload("memory_available"))
            time.sleep(1);
        if node["Disk_Usage"]:
            mqClient.publish("homeassistant/sensor/" + config.mqtt_topic + "/" + hostname + "_disk_usage/config", config_payload("disk_usage"))
            time.sleep(1);
        if node["Disk_Total"]:
            mqClient.publish("homeassistant/sensor/" + config.mqtt_topic + "/" + hostname + "_disk_total/config", config_payload("disk_total"))
            time.sleep(1);
        if node["Disk_Available"]:
            mqClient.publish("homeassistant/sensor/" + config.mqtt_topic + "/" + hostname + "_disk_available/config", config_payload("disk_available"))
            time.sleep(1);
        if node["Host_Uptime"]:
            mqClient.publish("homeassistant/sensor/" + config.mqtt_topic + "/" + hostname + "_host_uptime/config", config_payload("host_uptime"))
            time.sleep(1);


    logger.info("Sending values to MQTT broker")
    if node["Cpu_Temperature"]:
        mqClient.publish(config.mqtt_topic + "/" + hostname + "/cpu_temp", cpu_temp)
        time.sleep(1);
    if node["Cpu_Usage"]:
        mqClient.publish(config.mqtt_topic + "/" + hostname + "/cpu_usage", cpu_usage)
        time.sleep(1);
    if node["Cpu_Cores"]:
        mqClient.publish(config.mqtt_topic + "/" + hostname + "/cpu_cores", cpu_cores)
        time.sleep(1);
    if node["Cpu_Clockspeed"]:
        mqClient.publish(config.mqtt_topic + "/" + hostname + "/cpu_clockspeed", cpu_clockspeed)
        time.sleep(1);
    if node["Memory_Usage"]:
        mqClient.publish(config.mqtt_topic + "/" + hostname + "/memory_usage", memory_usage)
        time.sleep(1);
    if node["Memory_Total"]:
        mqClient.publish(config.mqtt_topic + "/" + hostname + "/memory_total", memory_total)
        time.sleep(1);
    if node["Memory_Available"]:
        mqClient.publish(config.mqtt_topic + "/" + hostname + "/memory_available", memory_available)
        time.sleep(1);
    if node["Disk_Usage"]:
        mqClient.publish(config.mqtt_topic + "/" + hostname + "/disk_usage", disk_usage)
        time.sleep(1);
    if node["Disk_Total"]:
        mqClient.publish(config.mqtt_topic + "/" + hostname + "/disk_total", disk_total)
        time.sleep(1);
    if node["Disk_Available"]:
        mqClient.publish(config.mqtt_topic + "/" + hostname + "/disk_available", disk_available)
        time.sleep(1);
    if node["Host_Uptime"]:
        mqClient.publish(config.mqtt_topic + "/" + hostname + "/host_uptime", host_uptime)
        time.sleep(1);

logger.info("Host type: " + config.host_type)
if config.host_type == "Raspberry Pi":
    hostname = pi.get_hostname()
    model = pi.get_model_name()
    manufacturer = pi.get_manufacturer_name()
    cpu_temp = pi.get_cpu_temp()
    cpu_usage = pi.get_cpu_usage()
    cpu_cores = pi.get_cpu_cores()
    memory_usage = pi.get_memory_usage()
    memory_total = pi.get_memory_total()
    memory_available = pi.get_memory_available()
    disk_usage = pi.get_disk_usage()
    disk_total = pi.get_disk_total()
    disk_available = pi.get_disk_available()
    host_uptime = pi.get_uptime()
    cpu_clockspeed = pi.get_cpu_clockspeed()
    


send_mqtt_update(hostname,cpu_temp, cpu_usage, cpu_cores, cpu_clockspeed, memory_usage, memory_total, memory_available, disk_usage, disk_total, disk_available, host_uptime)
