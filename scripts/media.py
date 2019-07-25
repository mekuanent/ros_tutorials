#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo('Macaw said %s', data.data)

def listener():

    #initialize ros node with a name, and anonymus is set to True if there are multiple
    #nodes with the same name, it will assign a unique name
    rospy.init_node('media', anonymous=True)

    rospy.Subscriber('tweet', String, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
