#!/usr/bin/env python3

import os

import rospy
from duckietown_msgs.msg import WheelsCmdStamped
from sensor_msgs.msg import Joy


class DTJoystickDemoNode:
    def __init__(self):
        rospy.init_node("dt_joystick_demo_node")

        # Get the vehicle name, which is stored as an environment variable
        veh_name = os.environ["VEHICLE_NAME"]

        # Subscribe to the joy data
        self.sub_joy = rospy.Subscriber(
            f"/{veh_name}/joy",
            Joy,
            self.process_joy,
            queue_size=1,
        )

        # Set up a way to publish the wheel command data
        self.pub_wheel_cmds = rospy.Publisher(
            f"/{veh_name}/wheels_driver_node/wheels_cmd",
            WheelsCmdStamped,
            queue_size=1,
        )

    # This will be the main function to process the incoming joystick data and
    # publish the wheel commands
    def process_joy(self, msg):
        cmd_to_publish = WheelsCmdStamped()
        cmd_to_publish.header = msg.header
        cmd_to_publish.vel_right = 0.0
        cmd_to_publish.vel_left = 0.0

        ### TODO! You need to fill in this part to set the left and right wheel commands based on the
        ### the incoming joystick data contained in `msg`

        # Finally we publish the data
        self.pub_wheel_cmds.publish(cmd_to_publish)


if __name__ == "__main__":
    # Initialize the node
    node = DTJoystickDemoNode()
    # Keep it spinning
    rospy.spin()
