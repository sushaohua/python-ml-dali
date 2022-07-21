import pyserial as serial
import time
import asyncio
import threading
com = 'ttyUSB0'

def ComOpen():
    print('aaaaa')
    ser = serial.Serial()
    print(ser)

def main():
    ComOpen()

if __name__ == "__main__":
    main()