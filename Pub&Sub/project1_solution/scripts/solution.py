#!/usr/bin/env python  
import rospy

from std_msgs.msg import Int16
from project1_solution.msg import TwoInts

# write a node to subscribe topics from two_int_talker

def callback(Int16): # need to publish a topic sum
	sumab= Int16.a+Int16.b
	pub.publish(sumab)
	print (sumab)


if __name__ == '__main__':

	rospy.init_node('listener', anonymous=True)

 	rospy.Subscriber("two_ints",TwoInts,callback)
 	pub = rospy.Publisher('sum', Int16, queue_size=10)
 	rate = rospy.Rate(0.5) 

 	rospy.spin()


