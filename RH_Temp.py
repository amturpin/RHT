# Python Code for Temp, RH, Pressure Sensor test for pCO2 Project
import time
import os, sys
import serial
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as md
import numpy as np
import datetime as dt

class Trinket():
    string = []
    def __init__(self, port = []):
        self.portnames = []
        self._detectPorts()
        self.ser = serial.Serial(self.port, baudrate=9600, timeout=2)
            
    def _detectPorts(self):
        
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i+1) for i in range(256)]
            print("Windows")
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        self.portnames[:] = []
        print(self.portnames)
            
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                self.portnames.append(port)
            except (OSError,serial.SerialException):
                pass
        print("Current Ports:")
        i = 0
        for port in self.portnames:
            print(str(i) +" - " + port)
            i += 1

        val = input("Enter port to use (0-99):")
        print(val)

        self.port = self.portnames[int(val)]

            
    
        
BME = Trinket()


filename = time.strftime("%Y%m%d", time.gmtime()) + '.csv'

if(os.path.isfile(filename)==False):
    f = open(filename, 'a', newline='')
    f.write("Date_Time,datenum,Temperature,Humidity\n")
else:
    f = open(filename, 'a', newline='')

DAY = time.localtime().tm_mday
while(1):
    #Time_Stamp = time.strftime("%m/%d/%Y %H:%M:%S,", time.localtime())
    
    if(DAY is not time.localtime().tm_mday):
        f.close()
        filename = time.strftime("%Y%m%d", time.localtime()) + '.csv'
        if(os.path.isfile(filename)==False):
            f = open(filename, 'a', newline='')
            f.write("Date_Time,datenum,Temperature,Humidity\n")
        else:
            f = open(filename, 'a', newline='')

    
    if(BME.ser.in_waiting>10):
        now = dt.datetime.now()
        Time_Stamp = dt.datetime.strftime(now ,"%Y-%m-%d %H:%M:%S,")
        dn = str(md.date2num(now)) +','
        sample = BME.ser.readline().decode()
        line = Time_Stamp + dn + sample[sample.find(':')+1:sample.find('\r')] + '\n'
        print(line)
        f.write(line)
    
BME.ser.close()
        
        

