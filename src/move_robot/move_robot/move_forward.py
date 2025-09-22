import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Imu

class Move(Node):
    time = 0
    leftWheelPos = 0
    def __init__(self):
        super().__init__("move_node")
        self.vel_publisher = self.create_publisher(Twist, "/cmd_vel", 10)
        self.jointPos = self.create_subscription(Imu, "/imu", self.printCurrentIMU, 10)
        self.get_logger().info("move node init!")
        self.create_timer(0.1, self.move)

    def move(self):
        message = Twist()
        self.time = self.time + 0.1
        if self.time < 5.5:
            message.linear.x = 0.25
        elif self.time > 5.5 and self.time < 6.5:
            message.linear.x = 0.0
            message.angular.z = 1.60
        elif self.time < 11.0:
            message.linear.x = 0.25
            message.angular.z = 0.0
        elif self.time > 11.0 and self.time < 12.0:
            message.linear.x = 0.0
            message.angular.z = -1.60
        elif self.time < 22.0:
            message.linear.x = 0.25
            message.angular.z = 0.0
        else:
            message.linear.x = 0.0
            message.angular.z = 0.0
            
        self.vel_publisher.publish(message)

    def printCurrentIMU(self, imu:Imu):
        self.get_logger().info(str(imu.linear_acceleration))

        

def main(args=None):
    rclpy.init(args=args)

    node = Move()
    rclpy.spin(node)
    rclpy.shutdown()