import serial

ser = serial.Serial('/dev/ttyUSB0', 1000000, timeout=1) # open serial port
while(1):
    print(ser.read())
