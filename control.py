#!/usr/bin/python
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
import serial
import time
import urllib2

ser = serial.Serial('/dev/ttyACM0',9600)
ser.readline()

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet1 = client.open("project").sheet1
#sheet2 = client.open("project").sheet2

# Extract and print all of the values
#list_of_hashes = sheet.get_all_records()
#print(list_of_hashes)
i=0
temp=0

import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)
 
Motor1A = 7
Motor1B = 8
Motor1_s = 0
Motor2_s = 0
if_manual = 0

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)

while True:
    rusky = ser.readline().split()
    print(rusky) 
    response=urllib2.urlopen("http://10.0.3.23:4000/polls/temp/?t="+rusky[0]+"&&cm=+"+rusky[1]+"&&m="+rusky[2]+"&&uid=Aakash"+"&&id=orchid"+"&&act="+Motor1_s)
    response=urllib2.urlopen("http://10.0.3.23:4000/polls/temp/?t="+rusky[0]+"&&cm=+"+rusky[1]+"&&m="+rusky[3]+"&&uid=Aakash"+"&&id=marigold"+"&&act="+Motor2_s)
    #G sheets API
    
    if_manual=sheet1.cell(9,3).value
    
    if if_manual== 1:
        s_act1=sheet1.cell(7,3).value    
        s_act2=sheet1.cell(8,3).value
        if (s_act1 == 1):
            GPIO.output(Motor1A,GPIO.HIGH)
            Motor1_s = 1
        elif (s_act1 == 0):
            GPIO.output(Motor1A,GPIO.LOW)
            Motor1_s = 0
            
        elif (s_act2 == 1):
            GPIO.output(Motor1B,GPIO.HIGH)
            Motor2_s = 1
        elif (s_act2 == 0):
            GPIO.output(Motor1B,GPIO.LOW)
            Motor2_s = 0
            
    else : 
        if (rusky[2] < 20 && Motor1_s == 0):
            print("Turning motor 1 on")
            GPIO.output(Motor1A,GPIO.HIGH)
            Motor1_s = 1
        elif (rusky[2] >= 20 && Motor1_s == 1):
            print("Stopping motor 1")
            GPIO.output(Motor1A,GPIO.LOW)
            Motor1_s = 0
            
            
        if (rusky[3] < 20 && Motor2_s == 0):
            print("Turning motor 2 on")
            GPIO.output(Motor1B,GPIO.HIGH)
            Motor2_s = 1
        elif (rusky[3] >= 20 && Motor2_s == 1):
            print("Stopping motor 2")
            GPIO.output(Motor1B,GPIO.LOW)
            Motor2_s = 0

    time.sleep(10)
