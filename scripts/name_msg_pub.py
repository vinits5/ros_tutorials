#!/usr/bin/env python

import rospy
from ros_tutorials.msg import Name

def name_msg_pub():
	pub=rospy.Publisher('chatter',Name,queue_size=10)
	rospy.init_node('name_msg_pub',anonymous=True)
	rate=rospy.Rate(10)
	while not rospy.is_shutdown():
		hello_str="hello world %s" % rospy.get_time()
		rospy.loginfo(hello_str)
		pub.publish(hello_str)
		rate.sleep()
	
if __name__=='__main__':
	try:
		name_msg_pub()
	except rospy.ROSInterruptException:
		pass

