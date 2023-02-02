# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 16:07:34 2023

@author: Bhuvan
"""


import serial
import time as t
import numpy as np
import matplotlib.pyplot as plt
import random as r


serialPort=serial.Serial()
serialPort.baudrate=9600
serialPort.port="COM3"

print(serialPort)
serialPort.open()

data=[]



while True:
    dataRead=False
    value = int(r.random()*255)
    print("value", value)
    while (dataRead==False):
        serialPort.write(bytes([value]))
        t.sleep(0.1)
        inByte = serialPort.in_waiting
        print(inByte)
        if (inByte>0):
            serialStringIn = serialPort.readline().decode(encoding="utf-8", errors="strict")
            if(serialStringIn[0]== 'W'):
                dataRead=True
        
serialPort.close()
