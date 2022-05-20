import nao_nocv_2_1 as nao
from time import sleep
import numpy as np

marvin = {'ip_address' : '192.168.0.115', 'colour' :'orange'}
bender = {'ip_address' : '192.168.0.112', 'colour' :'red'}

def detectLandmarkLoop(interval=0.1, max_duration=5):
    while(cur_duration < max_duration):
        # detect landmark
        detected, timestamp, markerInfo = nao.DetectLandMark()

        if detected:
            print("timestamp:",timestamp)
            print("markerInfo:",markerInfo)

        sleep(interval)
        cur_duration += interval


def StaticScan(yaw_val_deg=0):
    # yaw val in radians from degrees
    yaw_val_rad = np.radians(yaw_val_deg)

    # scan the environment with Nao's head, not moving the robot
    nao.MoveHead(yaw_val=yaw_val_rad, pitch_val=0)
    detectLandmarkLoop(max_duration=10)

def main():
    nao.InitProxy(bender['ip_address'])
    nao.InitPose()

    # tickrate in seconds
    tickrate = 0.1

    # init sonar
    nao.InitSonar()

    while(True):
        sleep(tickrate)
        
        # get sonar data
        SonarLeft, SonarRight = nao.ReadSonar()
        print("SonarLeft, SonarRight: ", SonarLeft, SonarRight)

        # scan the environment with Nao's head, not moving the robot
        StaticScan(yaw_val_deg=10)
        
        

        

    # rotate the robot in place
    # nao.Move(dx=0, dy=0, dtheta=0.5, freq=1)
    # nao.Crouch()

if __name__ == "__main__":
    main()

