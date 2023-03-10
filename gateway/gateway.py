print("Hello")      # Debug file

# Import packages ###############################
import paho.mqtt.client as mqttclient
import json
import time
import serial.tools.list_ports
import random
import psycopg2
from datetime import datetime
################ Import packages ################ 

# DATA QUERY EXAMPLE ############################

# conn = psycopg2.connect(database="gateway",
#                         host="192.168.1.12",
#                         user="postgres",
#                         password="password",
#                         port="5432")

# current_time = datetime.now().strftime("%H:%M:%S")
# print("Current Time =", current_time)

# temp = "BUTTON1:ON"
# splitData = temp.split(":")
# cursor = conn.cursor()
# cursor.execute("INSERT INTO feed_value (feed_name,timestamp,value) VALUES ('button1','"+current_time+"',1)")
# conn.commit()
# cursor.execute("SELECT * FROM feed_value;")
# print(cursor.fetchall())
# cursor.close()
# conn.close()

################ DATA QUERY EXAMPLE ################




# ADAFRUIT User Information --------------------------------------
ADAFRUIT_USERNAME = "dangnguyen"
BROKER_ADDRESS = "io.adafruit.com"
ADAFRUIT_ACCESS_TOKEN = "aio_rjuW84d3fI6sJeLCCCdD3pKR5GPH"
PORT = 1883
#  ---------------------------------------------------------------



# Adafruit feeds ------------------------------------------------------
feed = "dangnguyen/feeds/"
AIO_FEED_SUBCRIBE = [   "button1/",         # Fan controller
                        "button2/",         # Light controller
                        "FanValue/",        # Fan's rotation
                        "LightValue/",      # Light's brightness
                        "sensor1/",         # temperature sensor
                        "sensor2/",         # light sensor
                        "FanDisplay/",
                        "LightDisplay/"]         
AIO_FEED_PUBLISH = ["sensor1", 
                    "sensor2",
                    "button1", 
                    "button2", 
                    "FanValue", 
                    "LightValue",
                    "FanDisplay",
                    "LightDisplay"]
jsons = "json"
feedID = {
    "button1": 2463386,
    "button2": 2463387,
    "FanValue": 2463415,
    "LightValue": 2465220,
    "sensor1": 2462542,
    "sensor2": 2464202,
    "LightDisplay" : 2470613,
    "FanDisplay" : 2470612
}
# ---------------------------------------------------------------------



# message received by serial ------------------------------------------
mess = ""
fanValue = ""
lightValue = ""
# ---------------------------------------------------------------------



# Get serial port =======================

'''
    @name: find_port()
    @param:
        None
    @exp:
        Find serial port connects to YOLO:bit.
'''
# def find_port():
#     for port in list(serial.tools.list_ports.comports()):
#         txt = str(port)
#         if "USB Serial" in txt:
#             return (str(port).split("-")[0]+"-"+str(port).split("-")[1]).strip()

# bbc_port = find_port()
# if len(bbc_port) > 0:
#     ser = serial.Serial(bbc_port, 115200, bytesize=8, stopbits=serial.STOPBITS_ONE, parity=serial.PARITY_NONE)

# =============================================================



# Basic MQTT functions defined by user =======================

def subscribed(client, userdata, mid, granted_qos):
    print("Subscribed...")


def recv_message(client, userdata, message):
    global fanValue, lightValue
    received =  json.loads(message.payload.decode("utf-8"))
    cmd = "" 
    print("Received from: " + str(received['id']))
    #TODO: Update the cmd to control the device
    try:
        if received["id"] == feedID["FanValue"]:
            if received["last_value"] != "#":
                fanValue += received["last_value"]
                print(fanValue)
            else: 
                fanValue = fanValue.replace("*", "")
                
                if int(fanValue) >= 100:
                    fanValue = "100"
                client.publish(feed + AIO_FEED_PUBLISH[6], int(fanValue))
                cmd = "!FAN:ON:"+fanValue+"#"
        
        if received["id"] == feedID["LightValue"]:
            if received["last_value"] != "#":
                lightValue += received["last_value"]
                print(lightValue)
            else: 
                lightValue = lightValue.replace("*", "")
                
                if int(lightValue) >= 100:
                    lightValue = "100"
                client.publish(feed + AIO_FEED_PUBLISH[7], int(lightValue))
                cmd = "!LI:ON:"+lightValue+"#"

        if received["id"] == feedID["button1"] or received["id"] == feedID["FanDisplay"] :
            if received["last_value"] == "ON":
                cmd = "!FAN:ON:0#"
            if int(received["last_value"]) > 0:
                cmd = "!FAN:ON:" + str(received["last_value"]) + "#"
            if received["last_value"] == "OFF" or received["last_value"] == "0":
                cmd = "!FAN:OFF#"
        
        if received["id"] == feedID["button2"] or received["id"] == feedID["LightDisplay"]:
            if received["last_value"] == "ON":
                cmd = "!LI:ON:0#"
            if int(received["last_value"]) > 0:
                cmd = "!LI:ON:" + str(received["last_value"]) + "#"
            if received["last_value"] == "OFF" or received["last_value"] == "0":
                cmd = "!LI:OFF#"

        if received["id"] == feedID["sensor1"]:
            print("Temp: " + received["last_value"] + "??C")

        if received["id"] == feedID["sensor2"]:
            print("Light: " + received["last_value"] + " lux")

    except: 
        pass
    print(cmd)
#     if len(bbc_port) > 0:
#         ser.write((str(cmd)).encode())


def connected(client, userdata, flags, rc):
        try:
            print("Connected successfully!!")
            for topic in AIO_FEED_SUBCRIBE:
                client.subscribe(feed+topic+jsons)
                print("Connected to " + topic + " successfully!!")
        except:
            print("Connection is failed")
            pass

# ===================================================



# Serial process ------------------------------------

'''
    @name: processData()
    @param:
        data: string
    @exp:
        from Serial, received data will be processed and pushed to Adafruit.
'''
def processData(data):
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    print(splitData)
    
    if splitData[0] == "TE":
        client.publish(feed + AIO_FEED_PUBLISH[0], int(splitData[1]))
        serial.write("!ACK:TE#".encode())

    if splitData[0] == "LI":
        client.publish(feed + AIO_FEED_PUBLISH[1], int(splitData[1]))
        serial.write("!ACK:LI#".encode())

    if splitData[0] == "BUT":
        if splitData[1] == "1":
            client.publish(feed + AIO_FEED_PUBLISH[2], (splitData[1]))
            if splitData[1] == "ON":
                client.publish(feed + AIO_FEED_PUBLISH[6], int(splitData[2]))
            serial.write("!ACK:B1#".encode())

        if splitData[2] == "2":
            client.publish(feed + AIO_FEED_PUBLISH[3], (splitData[1]))
            if splitData[1] == "ON":
                client.publish(feed + AIO_FEED_PUBLISH[7], int(splitData[2]))
            serial.write("!ACK:B2#".encode())

'''
    @name: readSerial()
    @param:
        None
    @exp:
        Receiving data by readind byte to byte, and each message is between "!" and "#" characters.
'''
def readSerial():
    bytesToRead = ser.inWaiting()
    if (bytesToRead > 0):
        global mess
        mess = mess + ser.read(bytesToRead).decode("UTF-8")
        while ("#" in mess) and ("!" in mess):
            start = mess.find("!")
            end = mess.find("#")
            processData(mess[start:end + 1])
            if (end == len(mess)):
                mess = ""
            else:
                mess = mess[end+1:]

# --------------------------------------------------------------------



######################## PAHO-MQTT CONNECTION ########################
# define client
client = mqttclient.Client("Gateway_Adafruit")

# set username and password
client.username_pw_set(ADAFRUIT_USERNAME, ADAFRUIT_ACCESS_TOKEN)

# connect to broker with address and port
    # Port:
        # 1883: Insecure port.
        # 8883: Secure port.
        # 443: MQTT through Websocket. 
client.connect(BROKER_ADDRESS, 1883)


# subcribe and receive data from server. _________
client.on_connect = connected
client.loop_start()
client.on_subscribe = subscribed
client.on_message = recv_message
# ________________________________________________

######################## DONE ########################

'''
    Enter while loop.
'''
while True:

    # if len(bbc_port) >  0:
    #     try:
    #         readSerial()
            
    #     except:
    #         pass
    time.sleep(1)







