import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class LoggerNode(Node):
    def __init__(self):
        super().__init__("logger_node")
        self.sub = self.create_subscription(String,"validation_result",self.logger_listener,10)
    def logger_listener(self,msg : String):
        print(msg.data)
def main(args=None):
    rclpy.init(args=args)
    node = LoggerNode()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == "__main__":
    main()