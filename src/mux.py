#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32
from geometry_msgs.msg import Twist

rospy.init_node('mux')

mux_state = 1

def teleop_callback(msg):
	if mux_state == 0:
		driver_pub.publish(msg)
	
def nav_callback(msg):
	if mux_state == 1:
		driver_pub.publish(msg)

def state_callback(msg):
	global mux_state
	mux_state = msg.data
	
	
state_sub = rospy.Subscriber('/state', Int32, state_callback) 
teleop_sub = rospy.Subscriber('/teleop', Twist, teleop_callback)
nav_sub = rospy.Subscriber('/fake_navigation', Twist, nav_callback)
driver_pub = rospy.Publisher('/mux', Twist, queue_size = 1)

rospy.spin()
