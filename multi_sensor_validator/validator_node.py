import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32,String
from message_filters import Subscriber,ApproximateTimeSynchronizer

class ValidatorNode(Node):
    def __init__(self):
        super().__init__("validator_node")
        self.get_logger().info("Initializing validator node")
        #self.ultrasonic_sub = self.create_subscription(Int32,"/ultrasonic_range",self.ultrasonic_listener,10)
        #self.infrared_sub = self.create_subscription(Int32,"/infrared_range",self.infrared_listener,10)
        self.ultrasonic_sub = Subscriber(self,Int32,"/ultrasonic_range",qos_profile=10)
        self.infrared_sub = Subscriber(self,Int32,"/infrared_range",qos_profile=10)
        self.validation_pub = self.create_publisher(String,"/validation_result",10)
        self.synced_sub = ApproximateTimeSynchronizer([self.ultrasonic_sub,self.infrared_sub],10,slop=.1,allow_headerless=True) 
        self.synced_sub.registerCallback(self.validate)

    def validate(self,msg1:Int32,msg2:Int32):
        print(f"ultrasonic : {msg1.data} cm | infrared : {msg2.data} cm | difference : {abs(msg1.data - msg2.data)}")
        msg = String()
        if(abs(msg1.data - msg2.data) <= 20):
            msg.data = "Sensor readings consistent"
        else:
            msg.data = "Sensor readings inconsistent"
        self.validation_pub.publish(msg)
def main(args = None):
    rclpy.init(args=args)
    node = ValidatorNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()