#!/usr/bin/env python3
import rospy
from visualization_msgs.msg import Marker


if __name__ == '__main__':
    rospy.init_node("box_pose_visualiser")
    pub_ma = rospy.Publisher("~marker", Marker, queue_size=1)

    r = rospy.Rate(30)

    # define markers directly in tag frame

    while not rospy.is_shutdown():

        time = rospy.get_rostime()

        m = Marker()
        m.header.frame_id = "obj/jaffa"
        m.header.stamp = time
        m.ns = "objects"
        m.id = 0
        m.type = Marker.CUBE
        m.pose.orientation.w = 1
        m.action = Marker.ADD
        m.color.r = 1
        m.color.a = 0.5
        m.scale.x = 0.17
        m.scale.y = 0.17
        m.scale.z = 0.055
        pub_ma.publish(m)

        m = Marker()
        m.header.frame_id = "obj/oats"
        m.header.stamp = time
        m.ns = "objects"
        m.id = 1
        m.type = Marker.CUBE
        m.pose.orientation.w = 1
        m.action = Marker.ADD
        m.color.r = 1
        m.color.a = 0.5
        m.scale.x = 0.125
        m.scale.y = 0.21
        m.scale.z = 0.06
        pub_ma.publish(m)

        try:
            r.sleep()
        except rospy.exceptions.ROSTimeMovedBackwardsException:
            pass
