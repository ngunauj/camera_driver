#!/usr/bin/env python
import rospy
import sys
import cv2
import signal
from std_msgs.msg import String
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image


class image_converter:

    def __init__(self):
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/webcam/img", Image, self.callback)

    def callback(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)

        #(rows, cols, channels) = cv_image.shape
        cv2.imshow("Image window", cv_image)
        cv2.waitKey(3)
        '''
        todo 
        '''
if __name__ == '__main__':
    ic = image_converter()
    rospy.init_node('pysub_img', anonymous=True)
    try:
    	rospy.spin()
    except KeyboardInterrupt:
    	print("Shutting down")
    cv2.destroyAllWindows()

    '''
    todo
    '''
