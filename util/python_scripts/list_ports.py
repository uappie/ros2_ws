

from serial import Serial as serialInstance
import serial.tools.list_ports


def list_ports():
     baudrate = 9600
     timeout = 5
     serialInst = serialInstance()
     user_stop = False

     ports = serial.tools.list_ports.comports()
     portlist = []
     for oneport in ports:
          portlist.append(str(oneport))
     print(portlist)



if __name__ == "__main__":

     print('COM ports:')
     list_ports()
     userInput = input('Press enter')
