import sys
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import BatteryState



class Publisher(Node):

    def __init__(self):
        super().__init__('spot_recorder')
        self.get_logger().info("Spot recorder started")
        self.publisher_ = self.create_publisher(BatteryState, '/battery', 1)


def main(args=None):
    rclpy.init(args=args)
    publisher = Publisher()
    rclpy.spin(publisher)
    publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()