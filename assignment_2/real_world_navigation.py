import nao_nocv_2_1 as nao
from time import sleep
import numpy as np

marvin = {'ip_address' : '192.168.0.115', 'colour' :'orange'}
bender = {'ip_address' : '192.168.0.112', 'colour' :'red'}

# eve = {'ip_address' : '192.168.0.119', 'colour' :'white'}


def detectLandmarkLoop(interval=0.1, max_duration=5):
    while(cur_duration < max_duration):
        # detect landmark
        detected, timestamp, markerInfo = nao.DetectLandMark()

        if detected:
            print("timestamp:",timestamp)
            print("markerInfo:",markerInfo)

        sleep(interval)
        cur_duration += interval


def StaticScan(yaw_val_deg=(0, 0)):
    # yaw val in radians from degrees
    yaw_val_rad_left = np.radians(yaw_val_deg[0])
    yaw_val_rad_right = np.radians(yaw_val_deg[1])

    # create a list of yaw values
    n_angles = 100
    t_offset = 0
    degrees_per_sec = 2
    rads_per_sec = np.radians(degrees_per_sec)

    max_time_sec = (yaw_val_deg[1] - yaw_val_deg[0]) / degrees_per_sec
    yaw_val_rad = np.linspace(yaw_val_rad_left, yaw_val_rad_right, num=n_angles).tolist()
    yaw_timelist = np.linspace(t_offset, max_time_sec+t_offset, num=n_angles).tolist()

    # scan the environment with Nao's head, not moving the robot
    for idx, angle_rad in enumerate(yaw_val_rad):
        print(f"{idx} : {angle_rad}")
        sleep(yaw_timelist[idx+1] - yaw_timelist[idx])
        nao.MoveHead(angle_rad, pitch_val=0, post=False)

    # scan the environment with Nao's head, not moving the robot
    # nao.MoveHead(yaw_val=yaw_val_rad_left, pitch_val=0)
    # sleep(5)
    # nao.MoveHead(yaw_val=yaw_val_rad_right, pitch_val=0)

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

    # scan the environment with Nao's head, not moving the robot
    # positive = left, negative = right?
    StaticScan(yaw_val_deg=(-60, 60))
    sleep(10)
        
    # nao crouch
    nao.Crouch()

        

    # rotate the robot in place
    # nao.Move(dx=0, dy=0, dtheta=0.5, freq=1)
    # nao.Crouch()

if __name__ == "__main__":
    main()

