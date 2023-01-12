#!/usr/bin/env python

import rospy
import numpy as np
import cv2
import time
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


def pub_img(video_name):
    pub = rospy.Publisher("tennis_ball_image",Image,queue_size=10)
    rospy.init_node("tennis_ball_publisher",anonymous=True)
    rate = rospy.Rate(1) # 1hz

    while not rospy.is_shutdown():
        video_capture = cv2.VideoCapture("video/"+ video_name)
        while(True):
            ret, frame = video_capture.read()
            time.sleep(0.3)
            pub.publish(frame)
            rate.sleep()
            if cv2.waitKey(10) & 0xFF == ord('q'): 
                break

if __name__ == '__main__':
    try:
        video_name = "tennis-ball-video.mp4"
        pub_img(video_name)    
    except rospy.ROSInterruptException:
        pass

