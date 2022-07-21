import serial
import time
import asyncio
import threading
com = '/dev/ttyUSB0'
testdata = b'\x01\x34\x56\x78\x9a\xbc\xde\xfe\x43'
head = 'a11a'
tail = '0d13'


string = '123456789'

def crc16(data:bytes):
    crc = 0xffff
    for cur_byte in data:
        crc = crc ^ cur_byte
        for _ in range(8):
            a = crc
            carry_flag = a & 0x0001
            crc = crc >> 1
            if carry_flag == 1:
                crc = crc ^ 0xa001
    return bytes([crc % 256, crc >> 8 % 256])


def ComOpen():
    ser = serial.Serial(com,baudrate=115200)
    # ser.write()
    # ser.read_until(b'\x0d\x13')
    # ser.read_all()
    # ser.readall()
    ser.write()
    return ser
def recv(ser):
    while True:
        data = ser.read_all()
        if data =='':
            continue
        else:
            break
        sleep(0.02)
    return data
def send(ser):
    ser.write(testdata)

def main():
    ser = ComOpen()
    print(ser)
    print(ser.isOpen())



    crc = crc16(testdata)
    print(crc.hex())
    print(crc.splitlines)
    print(str(crc.hex()))


    ser.close()
    print(ser.isOpen())
if __name__ == "__main__":
    main()