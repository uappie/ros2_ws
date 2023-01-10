
from serial import Serial as serialInstance
import serial.tools.list_ports

from configparser import ConfigParser
from time import sleep

#configur = ConfigParser()
#configur.read('config.ini')
BAUDRATE =  115200 #configur.getint('serialcom','baudrate')
TIMEOUT =  5 #configur.getint('serialcom','timeout')

class ArduinoSerial:
    def __init__(self, baudrate, timeout) -> None:
        self.baudrate = baudrate
        self.timeout = timeout
        self.serialInst = serialInstance()
        self.user_stop = False

    def list_ports(self):
        ports = serial.tools.list_ports.comports()
        portlist = []
        for oneport in ports:
            portlist.append(str(oneport))
        print(portlist)

    def connect(self, port):
        self.serialInst.baudrate = self.baudrate
        self.serialInst.timeout = self.baudrate
        self.serialInst.port = port
        self.serialInst.open()


    def disconnect(self):
        if self.serialInst.isOpen():
            self.serialInst.close()

    def read(self):
        data = 0
        if self.serialInst.in_waiting:
            data = self.serialInst.readline().decode('ascii').rstrip()
            
        return data

    def write(self, text):
        self.serialInst.write(text.encode('utf-8'))

    def loop(self):
        try:
            while True:
                data = self.read()
                if data != 0:
                    print(data)
                sleep(0.5)

        except KeyboardInterrupt:
            self.disconnect()
        except Exception:
            self.disconnect()
    
if __name__ == "__main__": 
     serialcom = ArduinoSerial(BAUDRATE, TIMEOUT)
     print('COM ports:')
     serialcom.list_ports()
     userInput = input('Select one of the ports for connecting. Input in "COM4" format: ')
     serialcom.connect(userInput)
     serialcom.loop()
