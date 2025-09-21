import rclpy
import random
from rclpy.node import Node
from std_msgs.msg import Int32

class InfraredNode(Node):
    def __init__(self):
        super().__init__("infrared_node")
        self.get_logger().info("initializing infrared sensor publisher")
        self.publisher = self.create_publisher(Int32,"/infrared_range",10)
        self.create_timer(1,self.publish_message)

        self.infrared = InfraredSensor()

    def publish_message(self):
        msg = Int32()
        msg.data = self.infrared.get_reading()
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = InfraredNode()
    rclpy.spin(node)
    rclpy.shutdown()

class InfraredSensor():
    def get_reading(e=None):
        return random.randint(10,200)
if __name__ == '__main__':
    main()