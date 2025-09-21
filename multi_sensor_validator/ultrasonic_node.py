import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from multi_sensor_validator.ultrasonic_sensor import UltrasonicSensor

class UltrasonicNode(Node):
    def __init__(self):
        super().__init__("ultrasonic_node")
        self.get_logger().info("initializing ultrasonic sensor publisher")
        self.publisher = self.create_publisher(Int32,"/ultrasonic_range",10)
        self.create_timer(1,self.publish_message)

        self.ultrasonic = UltrasonicSensor()

    def publish_message(self):
        msg = Int32()
        msg.data = self.ultrasonic.get_reading()
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = UltrasonicNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()