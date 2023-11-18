import numpy as np
import serial
import cv2

ser = serial.Serial('/dev/ttyUSB0', 1000000, timeout=1) # open serial port
while(1):
    line = ser.readline()
    line = line.split()
    i = 1
    for val in line:
        if(i%2 == 0):
            valy = val
            plt.scatter(int(valx),int(valy))
        else:
            valx = val
        i = i + 1
    plt.show

