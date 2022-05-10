# -*- coding: utf-8 -*-
import nao_nocv_2_1 as nao  # with this line you import all the functions of the naolibrary and are able to call them with “nao”
# import matplotlib.pyplot as plt
import cv2
from time import sleep


nao.InitProxy("192.168.0.115")  # with this line you initialize all the proxies, and indicate the IP-adres. In this case this is 127.0.0.1, because this is your home ip-adress.
# nao.InitPose()              # this line makes the robot stand up
# nao.Walk(1, 0, 0)           # this line makes the robot walk 1 meter in x direction
# nao.Crouch()                # this line makes the robot crouch


# loop over colours stepsize 5
# for i in range(0, 255, 5):
#     for ii in range(0, 255, 5):
#         for iii in range(0, 255, 5):
#             nao.EyeLED([i, ii, iii])
#             sleep(0.01)

# init video and get image
nao.InitVideo(resolution_id=0)

# get image
img = nao.GetImage()

# cv2.imshow("frame", img)
# key=cv2.waitKey(1)    

# show image using pyplot
print("Type: ", type(img))
print("Image: ", img)

# convert image to numpy array
# ('Type: ', <type 'str'>)
# ('Image: ', '.... img ....')

# cv.SetData(cv_im, pi.tostring())
# plt.imshow(img)

