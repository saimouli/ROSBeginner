#!/usr/bin/env python  
import rospy

from std_msgs.msg import Int16
from project1_solution.msg import TwoInts

# write a node to subscribe topics from two_int_talker

def callback(Int16): # need to publish a topic sum
	sumab= Int16.a+Int16.b # add the subscribed two integers
	pub.publish(sumab) #publish the sum of instegers as a sum topic 
	print (sumab) #print to screen


if __name__ == '__main__':

	rospy.init_node('listener', anonymous=True) #initialize subscriber as listner 

 	rospy.Subscriber("two_ints",TwoInts,callback)
 	pub = rospy.Publisher('sum', Int16, queue_size=10)
 	rate = rospy.Rate(0.5) 

 	rospy.spin()


