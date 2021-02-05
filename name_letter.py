#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

# Name: SIVANAGA SURYA VAMSI POPURI
# ASU ID: 1217319207
# ROS VERSION: KINETIC
# UBUNTU VERSION: 16.04 Xenial LTS
# Package requirements: rospy, geometry_msgs.msg, turtlesim.msg


# The following program draws the letter 'P', the starting letter of the 
# name 'POPURI', using turtlesim. 

# Class, for encapsulation and simplification of code. 
class DrawLetter:
    def __init__(self):
	self.v = Twist()    
	self.pi = 3.14159
	self.pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	self.rate = rospy.Rate(20) 
        self.x = 0
	self.y = 0
	self.theta = 0 
	print("\nThe program has begun.")

        '''
        The __init__ function was used to initialize the publisher, 
        pose variables, rate and the velocity publishing variable.
        ''' 

    def pose_callback(self, msg):
	self.x = msg.x
	self.y = msg.y
	self.theta = msg.theta
        '''
        Subscriber callback function. Gets the robot's pose and angle. 
        '''

    def halt(self):
	self.v.linear.x = 0
	self.v.angular.z = 0
	self.pub.publish(self.v)

    def clockwise(self, c=0):
	g_count = 0
	while g_count <= c:
	    self.v.linear.x = 1.0
	    self.v.angular.z = -1.0
	    self.pub.publish(self.v)
	    g_count += 1
	    self.rate.sleep()	

    def counter_clockwise(self, c=0):
	g_count = 0
	while g_count <= c:
	    self.v.linear.x = 1.0
	    self.v.angular.z = 1.0
	    self.pub.publish(self.v)
	    g_count += 1
	    self.rate.sleep()

    def move_forward(self, c=0):
	g_count = 0
	while g_count <= c:
	    self.v.linear.x = 1.0
	    self.v.angular.z = 0
	    self.pub.publish(self.v)
	    g_count += 1
	    self.rate.sleep()

    def move_back(self, c=0):
        g_count = 0
	while g_count <= c:
	    self.v.linear.x = -1.0
	    self.v.angular.z = 0
	    self.pub.publish(self.v)
	    g_count += 1
	    self.rate.sleep()

    def face_SE(self):
	while abs(self.theta - self.pi * 1.75) > 0.05:
	    self.se = rospy.Subscriber('/turtle1/pose', Pose, self.pose_callback)
	    self.v.linear.x = 0
	    self.v.angular.z = 1.0
	    self.pub.publish(self.v)
	    self.rate.sleep()

	self.v.linear.x = 0; self.v.angular.z = 0
        self.pub.publish(self.v)

    def face_SW(self):
	while abs(self.theta - self.pi * 1.25) > 0.05:
	    self.sw = rospy.Subscriber('/turtle1/pose', Pose, self.pose_callback)
	    self.v.linear.x = 0
	    self.v.angular.z = 1.0
	    self.pub.publish(self.v)
	    self.rate.sleep()

	self.v.linear.x = 0; self.v.angular.z = 0
        self.pub.publish(self.v)

    def face_NE(self):
	while abs(self.theta - (self.pi/4)) > 0.05:
	    self.ne = rospy.Subscriber('/turtle1/pose', Pose, self.pose_callback)
	    self.v.linear.x = 0
	    self.v.angular.z = 1.0
	    self.pub.publish(self.v)
	    self.rate.sleep()

	self.v.linear.x = 0; self.v.angular.z = 0
        self.pub.publish(self.v)

    def face_NW(self):
	while abs(self.theta - self.pi * 0.75) > 0.05:
	    self.nw = rospy.Subscriber('/turtle1/pose', Pose, self.pose_callback)
	    self.v.linear.x = 0
	    self.v.angular.z = 1.0
	    self.pub.publish(self.v)
	    self.rate.sleep()

	self.v.linear.x = 0; self.v.angular.z = 0
        self.pub.publish(self.v)

    def face_west(self):
	while abs(self.theta - self.pi) > 0.05:
	    self.we = rospy.Subscriber('/turtle1/pose', Pose, self.pose_callback)
	    self.v.linear.x = 0
	    self.v.angular.z = 1.0
	    self.pub.publish(self.v)
	    self.rate.sleep()

	self.v.linear.x = 0; self.v.angular.z = 0
        self.pub.publish(self.v)

    def face_north(self):
	while abs(self.theta - (self.pi / 2)) > 0.05:
	    self.s1 = rospy.Subscriber('/turtle1/pose', Pose, self.pose_callback)
	    self.v.linear.x = 0
            self.v.angular.z = 1.0
            self.pub.publish(self.v) 
            self.rate.sleep()

        self.v.linear.x = 0; self.v.angular.z = 0
        self.pub.publish(self.v)
        '''
        Upon opening Turtlesim, the robot faces to the side (EAST). Since the letter 'S'
        can be drawn easily if the robot initially starts facing up, the face_north() function
	was used. 
	'''
    def face_east(self):
	while abs(self.theta) > 0.08 :
	    self.s3 = rospy.Subscriber('/turtle1/pose', Pose, self.pose_callback)
	    self.v.linear.x = 0
            self.v.angular.z = 1.0
            self.pub.publish(self.v) 
            self.rate.sleep()

        self.v.linear.x = 0; self.v.angular.z = 0
        self.pub.publish(self.v)

    def face_south(self):
	while abs(self.theta - 1.5 * self.pi) > 0.05:
	    self.s4 = rospy.Subscriber('/turtle1/pose', Pose, self.pose_callback)
	    self.v.linear.x = 0
            self.v.angular.z = 1.0
            self.pub.publish(self.v) 
            self.rate.sleep()

    def get_initial_pose(self):
	start = [0, 0]
        count = 0
        while count <= 2:
	    self.s2 = rospy.Subscriber('/turtle1/pose', Pose, self.pose_callback)
	    start[0] = self.x
	    start[1] = self.y
	    count += 1
	    self.rate.sleep()
        return start
	'''
	This is just to get the initial pose of the robot. Not of much contribution to the main task. 
	This was part of a series of debuggings and testings!!
	'''

    def trace(self, letter):
        if letter == 's' or letter == 'S': 
	    self.face_north()
	    self.counter_clockwise(185)
	    self.clockwise(185)
	    self.halt()

	if letter == 'q' or letter == 'Q':
	    g_count = 0
	    self.face_east()
	    self.counter_clockwise(120)
	    self.move_forward(10)
	    self.halt()
        
        if letter == 'p' or letter == 'P': # First letter of last name. 
	    self.face_north()
	    g_count = 0
	    self.move_forward(60)
	    self.face_east()
	    self.clockwise(50)
	    self.halt()

	if letter == 'f' or letter == 'F':
	    self.face_north()
	    self.move_forward(90)
	    self.face_east()
	    self.move_forward(30)
	    self.move_back(30)
	    self.face_south()
	    self.move_forward(45)
	    self.face_east()
	    self.move_forward(30)
	    self.move_back(30)
	    self.halt()

	if letter == 'h' or letter == 'H':
	    self.face_north()
	    self.move_forward(40)
	    self.move_back(80)
	    self.move_forward(40)
	    self.face_east()
	    self.move_forward(40)
	    self.face_north()
	    self.move_forward(40)
	    self.move_back(80)
	    self.move_forward(40)
	    self.halt()

	if letter == 'g' or letter == 'G':
	    self.face_north()
	    self.counter_clockwise(60)
	    self.face_south()
	    self.move_forward(20)
	    self.counter_clockwise(60)
	    self.face_west()
	    self.move_forward(15)
	    self.halt()

	if letter == 'A' or letter == 'a':
	    self.face_NE()
	    self.move_forward(30)
	    self.face_SE()
	    self.move_forward(30)
	    self.move_back(15)
	    self.face_west()
	    self.move_forward(15)
	    self.halt()
	
	if letter == 'B' or letter == 'b':
	    self.face_north()
	    self.move_forward(83)
	    self.face_east()
	    self.clockwise(60)
	    self.face_east()
	    self.clockwise(60)
	    self.halt()

	if letter == 'c' or letter == 'C':
	    self.face_north()
	    self.counter_clockwise(60)
	    self.face_south()
	    self.move_forward(20)
	    self.counter_clockwise(60)
	    self.halt()

	if letter == 'x' or letter == 'X':
	    self.face_NW()
	    self.move_forward(15)
	    self.move_back(30)
	    self.move_forward(15)
            self.face_SW()
	    self.move_forward(15)
	    self.move_back(30)
	    self.move_forward(15)
	    self.halt()

	if letter == 'U' or letter == 'u':
	    self.face_south()
	    self.move_forward(40)
	    self.counter_clockwise(60)
	    self.move_forward(40)
	    self.halt()

	if letter == 'y' or letter == 'Y':
	    self.face_NE()
	    self.move_forward(40)
	    self.move_back(40)
	    self.face_NW()
	    self.move_forward(40)
	    self.move_back(40)
	    self.face_south()
	    self.move_forward(60)
	    self.halt()

	if letter == 'n' or letter == 'N':
	    self.face_north()
	    self.move_forward(40)
	    self.face_SE()
	    self.move_forward(50)
	    self.face_north()
	    self.move_forward(40)
	    self.halt()

	if letter == 'M' or letter == 'm':
	    self.face_north()
	    self.move_forward(40)
	    self.face_SE()
	    self.move_forward(50)
	    self.face_NE()
	    self.move_forward(50)
	    self.face_south()
	    self.move_forward(40)
	    self.halt()

	if letter == 'z' or letter == 'Z':
	    self.face_east()
	    self.move_forward(40)
	    self.face_SW()
	    self.move_forward(50)
	    self.face_east()
	    self.move_forward(40)
	    self.halt()

	'''
	For the letter 'P', the robot needs to first face north, travel upwards, 
	and then draw a semi circle in the clockwise direction and halt when it 
	touches the line it drew in the first place. The trace resembles the 
	letter 'P'. 
	'''

    def draw_letter(self, letter):
	self.s = self.get_initial_pose()
	print("Letter {} is being traced.".format(letter))
	self.trace(letter)
        print("The program has ended.\n")
	'''
	Function to execute the trace drawing actions in a sequence. 
	'''


if __name__ == '__main__':
    rospy.init_node('my_initials')
    D = DrawLetter()
    #l = input('Enter a character Letter: ')
    D.draw_letter('X') # Pass a letter here. CHange to 'S' if you need the letter.
    
    # An object that does it all, by calling the draw_letter function. 
    # This program can be used in another program as a user-defined library 
    
