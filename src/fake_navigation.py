#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

rospy.init_node('fake_navigation')
pub = rospy.Publisher('/mux', Twist, queue_size=1)

while not rospy.is_shutdown():
	twist = Twist()
	twist.linear.x = 0.25
	pub.publish(twist)
