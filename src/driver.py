#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def mux_callback(msg):
	cmd_vel_pub.publish(msg)

rospy.init_node('driver')
mux_sub = rospy.Subscriber('/mux', Twist, mux_callback)
cmd_vel_pub = rospy.Publisher('/robot0/cmd_vel', Twist, queue_size = 1)

rospy.spin()
	
