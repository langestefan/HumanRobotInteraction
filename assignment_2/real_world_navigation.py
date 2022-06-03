from turtle import distance
import nao_nocv_2_1 as nao
from time import sleep
import numpy as np

from landmark_detection import compute_landmark_location

from definitions import marvin


def detectLandmarkLoop(interval=0.1, max_duration=5):
    while(cur_duration < max_duration):
        # detect landmark
        detected, timestamp, markerInfo = nao.DetectLandMark()

        if detected:
            print("timestamp:",timestamp)
            print("markerInfo:",markerInfo)

        sleep(interval)
        cur_duration += interval


def StaticScan(yaw_val_deg=(0, 0), pitch_val_deg=-20):
    # yaw val in radians from degrees
    yaw_val_rad_left = np.radians(yaw_val_deg[0])
    yaw_val_rad_right = np.radians(yaw_val_deg[1])

    # create a list of yaw values
    n_angles = 20
    t_offset = 0
    degrees_per_sec = 50
    # rads_per_sec = np.radians(degrees_per_sec)

    # pitch val in rads
    pitch_val_rad = np.radians(pitch_val_deg)

    # time it takes to move from left to right should depend on total distance we move
    max_time_sec = (yaw_val_deg[1] - yaw_val_deg[0]) / degrees_per_sec
    print("max_time_sec: ", max_time_sec)

    yaw_val_rad = np.linspace(yaw_val_rad_left, yaw_val_rad_right, num=n_angles).tolist()
    yaw_timelist = np.linspace(t_offset, max_time_sec+t_offset, num=n_angles+1).tolist()

    # scan the environment with Nao's head, not moving the robot
    for idx, yaw_angle_rad in enumerate(yaw_val_rad):
        print("{0} : {1}".format(idx, yaw_angle_rad))
        sleep(yaw_timelist[idx+1] - yaw_timelist[idx])
        nao.MoveHead(yaw_angle_rad, pitch_val=pitch_val_rad, post=False)

        # look for landmark
        detected, timestamp, markerInfo = nao.DetectLandMark()

        if detected:
            print("timestamp: ", timestamp)
            # print("markerInfo: ", markerInfo)
            distance, angle_rad, angle_deg = compute_landmark_location(markerInfo)   
            print("Target found at distance: {0} angle: {1}".format(distance, angle_deg))     

        else:
            print("Didn't detect target")

    print("Done scanning")

    # detectLandmarkLoop(max_duration=10)

def main():
    nao.InitProxy(marvin['ip_address'])
    nao.InitPose()

    # tickrate in seconds
    tickrate = 0.1

    # init sonar
    # nao.InitSonar()

    # while(True):
    sleep(tickrate)
    
    # get sonar data
    # SonarLeft, SonarRight = nao.ReadSonar()
    # print("SonarLeft, SonarRight: ", SonarLeft, SonarRight)

    # init landmark
    nao.InitLandMark(switch=True, period = 500)

    # scan the environment with Nao's head, not moving the robot
    # positive = left, negative = right?
    StaticScan(yaw_val_deg=(-90, 90))
    sleep(10)
        
    # nao crouch
    nao.Crouch()

        

    # rotate the robot in place
    # nao.Move(dx=0, dy=0, dtheta=0.5, freq=1)
    # nao.Crouch()

if __name__ == "__main__":
    main()

