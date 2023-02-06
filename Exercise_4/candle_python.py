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

rand=0.5 #initial condition for random walk

type='uniform' #enter type of random number generator here (uniform, gaussian, or random walk)

def getrandomvalue(rand): #generates random number according to distribution
    
    if type=='uniform':
        randvalue= r.random()
        return randvalue
    
    if type=='gaussian':
        def M_CDF(mu):
            return 1-np.exp(-mu) # integrate M(mu) from 0 to mu bc mu needs to be positive (polar coords)

        def M_inverseCDF(r):
            return -np.log(np.abs(1-r))

        # uniform distribution
        def Theta_CDF(theta):
            return theta/(2*np.pi)

        def Theta_inverseCDF(r):
            return r*2*np.pi

        Nsamp = 1
        trials = range(int(Nsamp))

        values_mu = np.zeros(int(Nsamp))
        values_theta = np.zeros(int(Nsamp))

        # Generate mu and theta separately
        for i in trials:
            r1 = r.random() # value between 0 and 1
            r2 = r.randrange(-1000, 1000)/1000 # value between -1 and 1
        
            values_mu[i] = M_inverseCDF(r1) # store randomly generated mu's
            values_theta[i] = Theta_inverseCDF(r2) # store randomly generated theta's
        
        sigma = 0.2 # arbitrary

        values_r = np.sqrt(2*sigma**2 * values_mu)

        x = values_r*np.cos(values_theta)
        y = values_r*np.sin(values_theta)

        randvalue=x[0]+0.5

        if randvalue<0:
            randvalue=0
        if randvalue>1:
            randvalue=1

        return randvalue

    if type=='random walk':
        added=(r.random()-0.5)/100
        if rand+added<1 and rand+added>0:
            rand=rand+added
        return rand    

serialPort=serial.Serial()
serialPort.baudrate=9600
serialPort.port="COM3"

print(serialPort)
serialPort.open()

data=[]



while True:
    dataRead=False
    rand=getrandomvalue(rand)
    value = int(rand*255)
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
