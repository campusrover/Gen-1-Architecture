#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32
from geometry_msgs.msg import Twist

rospy.init_node('mux')
global mux_state

def teleop_callback(msg):
	if mux_state == 0:
		command_pub.publish(msg)
	
def nav_callback(msg):
	if mux_state == 1:
		command_pub.publish(msg)

def state_determine(msg):
	if msg.data == 0:
		mux_state = 0
	else: 
		mux_state = 1
	
	
state_sub = rospy.Subscriber('/state', Int32, state_determine) 
teleop_sub = rospy.Subscriber('/turtlebot3_teleop', Twist, teleop_callback)
nav_sub = rospy.Subscriber('/fake_navigation', Twist, nav_callback)
command_pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 1)

rospy.spin()
