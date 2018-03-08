#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

rospy.init_node('fake_navigation')
pub = rospy.publisher('fake_navigation', Twist, queue_size=1)

while not rospy.is_shutdown():
	twist = Twist()
	twist.linear.x = 5
	pub.publish(twist)
