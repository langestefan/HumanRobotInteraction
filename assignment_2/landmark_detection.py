import nao_nocv_2_1 as nao
#from nao_nocv_2_1 import InitLandMark , DetectLandMark
from time import sleep

nao.InitProxy("127.0.0.1")
#nao.InitProxy("192.168.0.115")
#def test_landmark_detection():
nao.InitPose() #this line makes the robot stand up 
nao.Walk(1,0,0) #this line makes the robot walk 1 meter in x direction 
nao.Crouch() #this line makes the robot crouch 
nao.InitLandMark(switch=True, period = 500)
""" for i in range(0, 5):
    detected, timestamp, markerInfo = nao.DetectLandMark()
    print ("detected:",detected)
    print ("timestamp:",timestamp)
    print ("markerInfo:",markerInfo)

    sleep(1) """
