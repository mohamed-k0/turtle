
import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from turtlesim.msg import Color
from std_msgs.msg import String

from pynput import keyboard



class Controller(Node):
    def __init__(self):
        super().__init__('controller_node')

        # Declare parameters to prevent hard-coding

        self.declare_parameter('cmd_vel_topic', '/cmd_vel')  # declare a parameter of name cmd_vel_topic with default value /cmd_vel
        self.declare_parameter('dominant_color_topic', '/dominant_color')
        self.declare_parameter('color_sensor_topic', '/turtle1/color_sensor')

        # Getting the parameters 

        cmd_vel_topic = self.get_parameter('cmd_vel_topic').value 
        dominant_color_topic = self.get_parameter('dominant_color_topic').value
        color_sensor_topic = self.get_parameter('color_sensor_topic').value

        # Declare Publisher of velocity commands

        self.vel_publisher = self.create_publisher(Twist, cmd_vel_topic, 10)

        # Declare Subscriber to color sensor of turtle

        self.color_subscriber = self.create_subscription(Color, color_sensor_topic, self.callback_color, 10)


        # Declare Publisher of dominant color
        self.dominant_publisher = self.create_publisher(String, dominant_color_topic, 10)

        # Setting Speeds
        self.linear_speed = 2.0
        self.angular_speed = 2.0

        # Start the keyboard listening
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()

        print("Controller started. Use W-A-S-D")

        


        

def main():

    rclpy.init()
    node = Controller()

    rclpy.spin(node)




    ...







if __name__ == "__main__":
    main()
