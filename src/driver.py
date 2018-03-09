#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def mux_callback(msg):
	mux_twist = msg.data
	cmd_vel_pub.publish(mux_twist)

rospy.init_node('driver')
mux_sub = rospy.Subscriber('/mux', Twist, mux_callback)
cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 1)

rospy.spin()
	
