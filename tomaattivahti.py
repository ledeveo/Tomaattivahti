#!/usr/bin/env python3
import requests
import serial
from time import sleep

def serReadLine(ser):
	s = ser.readline(500)
	s = s.decode('ASCII')	# convert bytes b'foo' to string 'foo'
	assert type(s)==str

	if len(s)<=1:
		return None
	if not s.endswith('\n'):
		return 'ERROR: Serial: Unknown command "%s"' % s
	s = s.replace('\n', '');

	return s

def isfloat(value):
  try:
    float(value)
    return True
  except:
    return False

def send_alert():
    return requests.post(

# replace your Mailgun api token, key and email recipient
#
#           "https://api.mailgun.net/"
#           auth=("api", ""),
#           data={"from": "Tomaattivahti <",
#                  "to": [""],
                    "subject": "Alert",
                    "text": alertmessage})
            

ser = serial.Serial(port="/dev/ttyACM0", baudrate=115200, timeout=1)

while True:
    s = serReadLine(ser)
    if s == None:
        s = "Noneerror"
    s = s.split()
    if len(s)==4:
        if isfloat(s[0]) & isfloat(s[1]) & isfloat(s[2]):
            temp = float(s[1])
            airhumidity = float(s[0])
            soilhumidity = float(s[2])
            light = float(s[3])
            alertmessage = ""
            if temp<10:
                alertmessage = "Alert! Low temperature "
            elif temp>80:
                alertmessage = "Alert! Extreme temperature, fire hazard "
            elif temp>35:
                alertmessage = "Alert! High temperature "
            if airhumidity < 30:
                alertmessage = alertmessage+ "Alert! Low humidity "
            elif airhumidity > 90:
                alertmessage = alertmessage+ "Alert! High humidity "
            if soilhumidity > 700:
                alertmessage = alertmessage+ "Alert! Soil too wet "
            elif soilhumidity < 300:
                alertmessage = alertmessage+ "Alert! Soil too dry "
            if light > 800:
                alertmessage = alertmessage+ "Alert! Plant lights are off "
                                    
            if alertmessage != "":
                r = send_alert()
                print (alertmessage)
            else:
                print ("no alert " +s[0] + s[1] + s[2])
            print (s)
            break
        else:
            print (s)
            sleep(0.1)
    else:
        print (s)
        sleep(0.1)
