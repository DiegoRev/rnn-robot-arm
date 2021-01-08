# -*- coding: utf-8 -*
import numpy as np
import serial, time
import struct
from array import array
from io import BytesIO
from joblib import dump, load
import math
clf = load('Red_neuronal_brazo.joblib')
class RobotCmd(object):

    _struct = struct.Struct('<hhh')

    def __init__(self):
        self.t1 = 0
        self.t2 = 0
        self.t3 = 0

    def serialize(self, buff):
        try:
            buff.write(RobotCmd._struct.pack(self.t1, self.t2, self.t3))
        except struct.error as se:
            raise SerializationError('Error in serialization %s' % (self.__str__))
        


def to_hex(data):
    return ":".join("{:02x}".format(c) for c in data)

def angulos(th1, th2, th3):
    cmd = RobotCmd()
    buff = BytesIO()
    cmd.t1 = th1
    cmd.t2 = th2
    cmd.t3 = th3
    cmd.serialize(buff)
    base_cmd = bytearray(buff.getvalue())
    arduino.write(base_cmd)
    
    # ser_bytes = arduino.readline() # lee una linea del puerto serial
    # decoded_bytes = str(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
    # print(decoded_bytes)

    # ser_bytes = arduino.readline()
    # decoded_bytes = str(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
    # print(decoded_bytes)
    
    # ser_bytes = arduino.readline()
    # decoded_bytes = str(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
    # print(decoded_bytes)


if __name__ == '__main__':

    arduino = serial.Serial('COM3', 9600)
    cmd = RobotCmd()
    buff = BytesIO()
    cmd.serialize(buff)

    while True:
        try:
            y=[]
            print("Ingrese su posicion")
            a=int(input("X = "))
            b=int(input("Y = "))
            c=int(input("Z = "))
            y.append(a)
            y.append(b)
            y.append(c)
            pos=[]
            pos.append(y)
            angulo =clf.predict(pos)
            
            th1=angulo[0,0]
            t1=round(th1*180.0/math.pi)

            th2=angulo[0,1]
            t2=round(th2*180.0/math.pi)

            th3=angulo[0,2]
            t3=round(th3*180.0/math.pi)

            angulos(t1,t2,t3)
            
        except:
            print("e")
            exit()