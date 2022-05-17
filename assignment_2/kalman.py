from __future__ import division
import numpy as np


def Kalman(sonar_left,sonar_right,sonar_left_modify,sonar_right_modify):

    Kalman_gain_left = 1/float(len(sonar_left_modify))
    Kalman_gain_right = 1/float(len(sonar_right_modify))

    sonar_left_update = sonar_left_modify[-1] + Kalman_gain_left * (sonar_left - sonar_left_modify[-1])
    sonar_right_update = sonar_right_modify[-1] + Kalman_gain_right * (sonar_right - sonar_right_modify[-1])  
     
    return sonar_left_update, sonar_right_update
    