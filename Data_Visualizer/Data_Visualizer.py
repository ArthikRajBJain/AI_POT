import numpy as np
import matplotlib.pyplot as plt
import serial

ser = serial.Serial('/dev/ttyUSB0', 1000000, timeout=1) # open serial port
while(1):
    line = ""
    byte = ""
    print('reading')
    byte = ser.read()
    while(byte!=b'\n'):
        line = line + str(byte.decode("ascii"))
        byte = ser.read()
    line = line.split()
    i = 1
    valx=[]
    valy=[]
    for val in line:
        if(i%2 == 0):
            valy.append(int(val))
        else:
            valx.append(int(val))
        i = i + 1
    plt.scatter(valx,valy)
    plt.show()

