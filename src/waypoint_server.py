#!/usr/bin/env python
import rospy
from campus_rover.srv import *
from move_base_msgs.msg import *

def process_location(request):
	test = MoveBaseGoal()
	return WaypointResponse(test)

def waypoint_server():
	rospy.init_node('waypoint_server')
	s = rospy.Service('location_to_waypoint', Waypoint, process_location)
	rospy.spin()

if __name__ == "__main__":
	waypoint_server()


