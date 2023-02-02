# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 15:19:48 2023

@author: Bhuvan
"""

import serial
import time as t
import numpy as np
import matplotlib.pyplot as plt

value=255

arraySize=500
serialPort=serial.Serial()
serialPort.baudrate=9600
serialPort.port="COM3"

print(serialPort)
serialPort.open()
dataRead=False
data=[]
while (dataRead==False):
    serialPort.write(bytes([value]))
    t.sleep(0.1)
    inByte = serialPort.in_waiting
#This loop reads in data from the array until byteCount reaches the array size (arraySize)
    byteCount=0
    while ((inByte>0)&(byteCount<arraySize)):

        dataByte=serialPort.read()
        byteCount=byteCount+1
        data=data+[dataByte]
    if (byteCount==arraySize):
        dataRead=True
        
serialPort.close()
dataOut=np.zeros(arraySize)
arrayIndex=range(arraySize)
#Transform unicode encoding into integers
for i in arrayIndex:
    dataOut[i]=ord(data[i])
#Plot your analog output!
f1=plt.figure()
plt.plot(arrayIndex, dataOut)
plt.xlabel("array index")
plt.ylabel("8-bit rounded voltage reading")
print('mean:', np.mean(dataOut))
np.savetxt('e7.3_tb5000.csv', dataOut, delimiter = ',')