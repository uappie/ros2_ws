#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from .user_input import UserInput
from example_interfaces.msg import String
from configparser import ConfigParser
  
  
class UserInputNode(Node):
        def __init__(self, userInput_class:UserInput):
                super().__init__("UserInput_node")  # type: ignore
                self.input_class = userInput_class
  
                # Subscribe to topic "move/command"
                #self.drive_command_subscriber = self.create_subscription(String, "move/command", self.send_command, 10)
                # Create timer to read responses every second
                self.create_timer(1.0, self.read_userInput)
                # Create publisher that publishes responses from arduino
                self.driveCommandPublisher = self.create_publisher(String, "move/command", 10)
                self.get_logger().info("User input node has started")
  
                  
        def send_command(self, message):
                msg = String()
                msg.data = message
                self.driveCommandPublisher.publish(msg)
                self.get_logger().info("Message sent: " + message)
  
        def read_userInput(self):
                response = self.input_class.readInput()
                self.send_command(response)
                self.get_logger().info("Received message: " + response)
  
  
def main(args=None):
        rclpy.init(args=args)
        input_class = UserInput()
        node = UserInputNode(input_class)
        rclpy.spin(node)
        rclpy.shutdown()
  
  
if __name__ == "__main__":
        main()