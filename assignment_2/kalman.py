from __future__ import division
import numpy as np
from matplotlib import pyplot as plt
'''
state space model
position_new = position_old + potision_update
x: state, z:measurement, u: movement
x_{k} = A@x_{k-1} + B@u_{k-1} + epsilon_R
z_{k} = C@x_{k} + epsilon_Q
'''
# state initialization
# state = [[position_x],[position_y],[head_phi]]
state_hat = np.array([[5,5,0]]).reshape(3,1)
# cov matrix = diag(1,1,1)
cov_hat = np.eye(3)
# A and C are both identity matrix (3x3)
A, C = np.eye(3), np.eye(3)
# epsilon is noise
epsilon_R = 1e-3*np.eye(3)
epsilon_Q = 1e-3*np.eye(3)
cov_hat = np.zeros(3)
# sonar_left = sonar_right = 10
sonar_left, sonar_right = 10, 10

state_hat_plot, state_real_plot = np.zeros_like(state_hat), np.zeros_like(state_hat)
degree = np.pi/180.0
iteration = 0

def state_read(robot):
    return robot.x, robot.y, robot.phi

def Kalman(robot,sonar_distance_left,sonar_distance_right):

    global sonar_left, sonar_right, state_hat, cov_hat, iteration, state_hat_plot, state_real_plot

    # get states 
    x_position, y_position, head_phi = state_read(robot)
    state_real = np.array([x_position, y_position, head_phi]).reshape(3,1)
    state_real_plot = np.append(state_real_plot,state_real,axis=0)
    # x,y movement unpate, w is constant
    # sonar distance change by cos(30*degree) times the distance moved by the robot
    # dx = cos(phi+-30)*move_distance, dy = sin(phi+-30)*move_distance, dw = 0
    B = np.array([np.cos(30*degree + head_phi),np.cos(head_phi - 30*degree),
                  np.sin(30*degree + head_phi),np.sin(head_phi - 30*degree),
                  0,0]).reshape(3,2)

    dsonar_distance_left, dsonar_distance_right = sonar_left - sonar_distance_left, sonar_right - sonar_distance_right
    sonar_left, sonar_right = sonar_distance_left, sonar_distance_right

    print('sonar_left',sonar_left)
    print('sonar_right',sonar_right)

    u_k = np.array([dsonar_distance_left,dsonar_distance_right]).reshape(2,1)

    # update rule:
    # miu = miu_hat + K@(z - C@miu_hat)
    # cov = (I - K@C)@cov_hat
    # where K = cov@C.T(C@cov@C.T+epsilon_Q)^(-1)
    # prediction:
    # x_{k} = A_{k}@x_{k-1} + B_{k}@u_{k-1} 
    #     = x_{k-1} + B_{k}@u_{k-1}
    # cov_{k} = A_{k}@cov_{k-1}@A_{k}.T + epsilon_R_{k}
    #         = cov_{k-1} + epsilon_R_{k}
    # check if it is the first iteration
    if iteration == 1:
        Kalman_gain = cov_hat.dot((np.linalg.inv(cov_hat+epsilon_Q)))
        state_update = state_real + Kalman_gain.dot((state_real+epsilon_Q - state_real))
        cov_update = (np.eye(3) - Kalman_gain).dot(cov_hat)
        state_hat = state_update + B.dot(u_k)
        cov_hat = cov_update + epsilon_R
        iteration += 1
    else:
        Kalman_gain = cov_hat.dot((np.linalg.inv(cov_hat+epsilon_Q)))
        state_update = state_hat + Kalman_gain.dot((state_real - state_hat))
        cov_update = (np.eye(3) - Kalman_gain).dot(cov_hat)
        state_hat = state_update + B.dot(u_k)
        cov_hat = cov_update + epsilon_R

    print('state_hat',state_hat)
    print('state_update',state_update)

    state_hat_plot = np.append(state_hat_plot,state_hat,axis=0)

    # if len(sonar_left_modify) == 1:
    #     sigma_left.append(0.25)
    #     sigma_right.append(0.25)

    # Kalman_gain_left = sigma_left[-1]/(sigma_left[-1] + sigma_noise)
    # Kalman_gain_right = sigma_right[-1]/(sigma_right[-1] + sigma_noise)

    # sonar_left_update = sonar_left_modify[-1] + Kalman_gain_left * (sonar_left - sonar_left_modify[-1])
    # sonar_right_update = sonar_right_modify[-1] + Kalman_gain_right * (sonar_right - sonar_right_modify[-1])  

    # sigma_left_ = (1-Kalman_gain_left) * sigma_left[-1]
    # sigma_right_ = (1-Kalman_gain_right) * sigma_right[-1]
     
    # return sonar_left_update, sonar_right_update, sigma_left_, sigma_right_
    

def trajectory():
    global state_hat_plot, state_real_plot

    plt.plot(state_hat_plot[3:len(state_hat_plot):3],state_hat_plot[4:len(state_hat_plot):3],'rx',
             state_real_plot[3:len(state_real_plot):3],state_real_plot[4:len(state_real_plot):3],'bo')
    plt.legend(['Kalman filtered state','Real state'])
    plt.show() 
