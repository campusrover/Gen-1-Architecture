#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

rospy.init_node('state')

def state_callback(msg):
	print("STATE", msg.data)
	state = msg.data
	mux_pub.publish(state)

navigation_sub = rospy.Subscriber('/fake_navigation', Int32, state_callback)
teleop_sub = rospy.Subscriber('/teleop', Int32, state_callback)
mux_pub = rospy.Publisher('/mux', Int32, queue_size=1)

rospy.spin()
