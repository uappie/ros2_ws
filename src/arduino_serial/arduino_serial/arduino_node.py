#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from .serial_com import ArduinoSerial
from example_interfaces.msg import String
from configparser import ConfigParser

# Read settings from .ini file. Maybe not a normal way of doing this in ROS
# configur = ConfigParser() 
# configur.read('config.ini')
BAUDRATE =  115200#configur.getint('serialcom','baudrate')
TIMEOUT =  5#configur.getint('serialcom','timeout')
COM_PORT =  "/dev/ttyACM0" #configur.getint('serialcom','port')


class ArduinoSerialNode(Node):
    """
    Node that wraps some class used for serial communication.
    """
    def __init__(self, serial_class:ArduinoSerial):
        super().__init__("arduino_serial_node")  # type: ignore
        self.serial_class = serial_class

        # Subscribe to topic "move/command"
        self.drive_command_subscriber = self.create_subscription(String, "move/command", self.send_command, 10)
        # Create timer to read responses every second
        self.create_timer(1.0, self.read_response)
        # Create publisher that publishes responses from arduino
        self.drive_response_publisher = self.create_publisher(String, "move/response", 10)
        self.get_logger().info("Arduino serial communication has started")

 
    def send_command(self, message):
        self.serial_class.write(message.data)
        self.get_logger().info("Message sent: " + message.data)

    def read_response(self):
        response = self.serial_class.read()
        if response != 0:
            self.get_logger().info("Received message: " + response)



def main(args=None):
    rclpy.init(args=args)
    serial_class = ArduinoSerial(BAUDRATE, TIMEOUT)
    serial_class.connect(COM_PORT)
    node = ArduinoSerialNode(serial_class)
    rclpy.spin(node) 
    serial_class.disconnect()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
