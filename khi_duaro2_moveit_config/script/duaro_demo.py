#!/usr/bin/env python

import rospy
import math
from moveit_commander import MoveGroupCommander

if __name__ == '__main__':

    #init_node()
    group = MoveGroupCommander("botharms")
    sleep_time = 1
    exec_vel = 0.7
    exec_acc = 1.0
    accuracy_jt = 0.01

    group.set_goal_joint_tolerance(accuracy_jt)
    group.set_max_velocity_scaling_factor(exec_vel)
    group.set_max_acceleration_scaling_factor(exec_acc)
    group.set_joint_value_target([math.radians(-90), math.radians(90),0.03, math.radians(0.0), math.radians(90), math.radians(-90), 0.4, math.radians(0.0)])
    group.go()
    rospy.sleep(sleep_time)
    group.set_max_acceleration_scaling_factor(exec_acc)
    group.set_max_velocity_scaling_factor(exec_vel)
    group.set_goal_joint_tolerance(accuracy_jt)
    group.set_joint_value_target([math.radians(-90), math.radians(90), 0.55, math.radians(0.0), math.radians(90), math.radians(-90), 0.4, math.radians(0.0)])
    group.go()

