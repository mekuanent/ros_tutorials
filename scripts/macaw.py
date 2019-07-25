#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('tweet', String, queue_size=10)
    rospy.init_node('Macaw', anonymous=True)
    rate = rospy.Rate(1)
    tweets = ["I woke up", "Breakfast is awesome!", "Better hit the gym"];

    index = 0
    while not rospy.is_shutdown():
        info = "typing with my little fingers at %s" % rospy.get_time()
        rospy.loginfo(info)
        pub.publish(tweets[index % 6])
        rate.sleep()
        index+=1

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
