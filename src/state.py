#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

rospy.init_node('state')

def state_callback(msg):
	state = msg.data
	state_pub.publish(state)

teleop_sub = rospy.Subscriber('/teleop/state', Int32, state_callback)
state_pub = rospy.Publisher('/state', Int32, queue_size=1)

rospy.spin()
