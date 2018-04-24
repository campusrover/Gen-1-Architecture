#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

rospy.init_node('state') 

current_state = 0

def state_callback(msg):
	state = msg.data
	if(current_state == state):
		# negative feedback
	elif(state == 0):
		if(current_state == 1 || current_state == 2 || current_state == 3 || current_state == 4 || current_state == 5):
			current_state = 0
		else:
			# negative feedback
	elif(state == 1):
		if(current_state == 0 || current_state == 2 || current_state == 8 || current_state == 3 || current_state == 5):
			current_state = 1
		else:
			# negative feedback
	elif(state == 2):
		if(current_state == 0 || current_state == 3 || current_state == 5):
			current_state = 2
		else:
			# negative feedback
	elif(state == 3):
		if(current_state == 0 || current_state == 2 || current_state == 5 || current_state == 8):
			current_state = 3
		else:
			# negative feedback
	elif(state == 4):
		if(current_state == 0 || current_state == 3 || current_state == 5 || current_state == 2):
			current_state = 4
		else:
			# negative feedback
	elif(state == 5):
		if(current_state == 0 || current_state == 2 || current_state == 7):
			current_state = 5
		else:
			# negative feedback
	elif(state == 6):
		if(current_state == 0 || current_state == 3 || current_state == 4 || current_state == 5):
			current_state = 6
		else:
			# negative feedback
	elif(state == 7):
		if(current_state == 0 || current_state == 6):
			current_state = 7
		else:
			# negative feedback
	elif(state == 8):
		if(current_state == 0 || current_state == 1 || current_state == 5 || current_state == 6):
			current_state = 8
		else:
			# negative feedback
	state_pub.publish(current_state)

teleop_sub = rospy.Subscriber('/teleop/state', Int32, state_callback)
state_pub = rospy.Publisher('/state', Int32, queue_size=1)

rospy.spin()
