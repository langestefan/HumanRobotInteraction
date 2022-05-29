import math
import numpy as np
from assignment_2.kalman import state_read
from definitions import *
from kalman import Kalman

def compute_target_location(robot, alltargets):
    """This function computes the distance to the target and the angle relative to the robot in world coordinates"""
    dist = []
    angle = []
    for tar in alltargets:
        dx = tar.x - robot.x
        dy = tar.y - robot.y
        dist.append(np.linalg.norm([dx, dy]))
        angle.append(math.atan2(dy, dx))
    i = np.argmin(dist)
    return dist[i], angle[i]


def scan_world(bn_robot, robot, allobstacles, alltargets):
    """ This function scans the world with sonar sensors and returns the distance to the closest obstacle.

        parameters:
            bn_robot: the behaviour_based_navigation robot
            robot: the robot object
            allobstacles: a list of all obstacles
            alltargets: a list of all targets
            sonar_right_modify: the modified sonar right
            sonar_left_modify: the modified sonar left
        returns:
            sonar_right_update: the updated sonar right
            sonar_left_update: the updated sonar left
    """

    # let sonars scan the target instead of the obstacles
    [sonar_left, sonar_right] = robot.sonar(allobstacles)
    target_distance, target_angle = compute_target_location(robot, alltargets)  # The angle is with respect to the world frame
    # print sonar_left, sonar_right, target_distance, target_angle
    target_angle_robot = target_angle - robot.phi  # This is the angle relative to the heading direction of the robot.

    Kalman(robot,sonar_left,sonar_right)
    # sonar_left_update, sonar_right_update, sigma_l, sigma_r = Kalman(sonar_left,sonar_right,sonar_right_modify,sonar_left_modify, sigma_l, sigma_r)

    # if Kalman_config is True:
    #     sonar_left = sonar_left_update
    #     sonar_right = sonar_right_update

    turn_rate = bn_robot.compute_turnrate(target_distance, target_angle_robot, sonar_left, sonar_right, robot=robot)
    velocity = bn_robot.compute_velocity(target_distance, target_angle_robot)
    robot.set_vel(velocity, turn_rate) # the simulated robot does not sidestep
    # print('update_l',sonar_left)
    # print('update_r',sonar_right)
    # print('sigma_l',sigma_l)
    # print('sigma_r',sigma_r)
    # print velocity, turn_rate
