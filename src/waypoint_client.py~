#!/usr/bin/env python
import rospy

from campus_rover.srv import *

def waypoint_client(location):
	rospy.wait_for_service('location_to_waypoint')
	try:
		location_to_waypoint = rospy.ServiceProxy('location_to_waypoint', Waypoint)
		response = location_to_waypoint(location)
		return response
	except rospy.ServiceException, e:
			print "Service call failed %s"%e

request = WaypointRequest('test')
print request
waypoint_client(request)


