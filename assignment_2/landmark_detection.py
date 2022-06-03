#from sqlalchemy import true
import nao_nocv_2_1 as nao
import numpy as np
from time import sleep
import math
import almath
import naoqi


def compute_landmark_location(markerInfo):
    """
    In order to use this 'compute the landmark location' function, 
    please call nao.DetectLandMark(), to get detected, timestamp, markerInfo 

    parameters:
            markerInfo: markerInfo[1][0]  # markerID
                        markerInfo[0][1], # alpha - x location in camera angle
                        markerInfo[0][2], # beta  - y location
                        markerInfo[0][3], # sizeX
                        markerInfo[0][4], # sizeY
                        markerInfo[0][5]  # orientation about vertical w.r. Nao's head    
    """
    landmarkTheoreticalSize = 0.092 # in meters
   
    # Compute distance to landmark.
    angle_rad = markerInfo[0][1]
    x_size = markerInfo[0][3]
    distance = landmarkTheoreticalSize / (2*math.tan(x_size / 2))

    # convert angle to degrees
    angle_deg = np.degrees(angle_rad)

    return distance, angle_rad, angle_deg

# test compute_landmark_location function
def test():
    ip = "192.168.0.115"
    
    nao.InitProxy(ip)

    nao.InitPose() #this line makes the robot stand up 

    #nao.Walk(1,0,0) #this line makes the robot walk 1 meter in x direction 

    #nao.Crouch() #this line makes the robot crouch 
    nao.InitLandMark(switch=True, period = 500)
    for i in range(0, 30):
        sleep(0.5)

        detected, timestamp, markerInfo = nao.DetectLandMark()
        print "Detected:" , (detected)
        print "Timestamp:", (timestamp)
        print "markerInfo:", (markerInfo)
        distnace, angle = compute_landmark_location(detected, timestamp, markerInfo)
   
if __name__ == "__main__":
    test()    