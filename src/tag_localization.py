#!/usr/bin/env python
import rospy
import tf
from tf import TransformerROS, Transformer 
from geometry_msgs.msg import PoseStamped
from apriltags2_ros.msg import AprilTagDetectionArray

rospy.init_node('tag_localization')

transformer = TransformerROS()
listener = tf.TransformListener()

def tag_detection_callback(msg):
	if msg.detections:
		robot_to_tag_pose = PoseStamped(msg.detections[0].pose.header, msg.detections[0].pose.pose.pose)
		print robot_to_tag_pose
		pos = robot_to_tag_pose.pose.position
		br.sendTransform(
			(pos.x, pos.y, pos.z),
			(0, 0, 0, 1.0),
			rospy.Time.now(),
			'camera_rbg_optical_frame',
			'tag_6'
			
		) 
		camera_rgb_frame_to_tag_pose = transformer.transformPose('camera_rgb_frame', robot_to_tag_pose)
		print camera_rbg_frame_to_tag_pose


tag_detection_sub = rospy.Subscriber('/tag_detections', AprilTagDetectionArray, tag_detection_callback)
br = tf.TransformBroadcaster()
rate = rospy.Rate(5)

while not rospy.is_shutdown():
	br.sendTransform(
		(0.585, 7.85, -0.00143),
		(0, 0, 0, 1.0),
		rospy.Time.now(),
		'tag_6',
		'map'
	)
	rate.sleep()
