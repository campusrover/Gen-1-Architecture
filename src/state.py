#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

rospy.init_node('state') 

current_state = 0
state_change = [[1, 2, 3, 4, 5], [0, 2, 8, 3, 5], [0, 3, 5], [0, 2, 5, 8], [0, 3, 5, 2], [0, 2, 7], [0, 3, 4, 5], [6], [0, 1, 5, 6]]

def state_callback(msg):
	state = msg.data

	if current_state == state:
		continue
	else 
		if state in state_change[current_state]:
			current_state = state
		else:
			log_pub.publish('Unable to convert from state %s to state %s' % (current_state, state))

	state_pub.publish(current_state)

teleop_sub = rospy.Subscriber('/state', Int32, state_callback)
state_pub = rospy.Publisher('/state', Int32, queue_size=1)
log_pub = rospy.Publisher('/state/log', String, queue_size=1)

rospy.spin()
