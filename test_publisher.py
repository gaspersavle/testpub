from colorama import Fore
import rospy
import std_msgs.msg
from std_msgs.msg import String

class PubTest():
    def __init__(self):
        self.textTopic = '/rostest/text'
        self.rosNodeText = 'rostest'

        self.initRosPy()

        while 1:
            self.publishString()

    def initRosPy():
        rospy.init_node(self.rosNodeText, anonymous=True)
        self.PUB_string = rospy.Publisher(self.textTopic, String, queue_size=10)
        self.r = rospy.Rate(1)

    def publishString():
        self.PUB_string.publish("kosamona, masterpi in this bitch")
        self.r.sleep()

if __name__ == "__main__":
    print(f"{Fore.RED} Starting publisher")
    PubTest()


