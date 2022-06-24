# Choregraphe simplified export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.96, 1.4, 1.56])
keys.append([0.0724282, -0.09203, -0.0154342])

names.append("HeadYaw")
times.append([0.2, 0.56, 0.8, 0.96, 1.12, 1.32, 1.56])
keys.append([-0.0122965, -0.0102073, -0.0985437, 0.0893026, -0.0985437, 0.0893026, -0.0140261])

names.append("LAnklePitch")
times.append([0.72, 1.56])
keys.append([-0.0276539, 0.0957674])

names.append("LAnkleRoll")
times.append([0.72, 1.56])
keys.append([-0.184038, -0.185333])

names.append("LElbowRoll")
times.append([0.96, 1.56])
keys.append([-0.425288, -0.416156])

names.append("LElbowYaw")
times.append([0.96, 1.56])
keys.append([-1.20557, -1.19838])

names.append("LHand")
times.append([0.96, 1.56])
keys.append([0.314203, 0.306419])

names.append("LHipPitch")
times.append([0.72, 1.56])
keys.append([-0.0904641, 0.120194])

names.append("LHipRoll")
times.append([0.72, 1.56])
keys.append([0.18719, 0.187996])

names.append("LHipYawPitch")
times.append([0.72, 1.56])
keys.append([-0.18097, -0.179863])

names.append("LKneePitch")
times.append([0.72, 1.56])
keys.append([0.190175, -0.0878086])

names.append("LShoulderPitch")
times.append([0.96, 1.56])
keys.append([1.40624, 1.46352])

names.append("LShoulderRoll")
times.append([0.96, 1.56])
keys.append([0.246933, 0.18874])

names.append("LWristYaw")
times.append([0.96, 1.56])
keys.append([-0.108112, 0.0977037])

names.append("RAnklePitch")
times.append([0.72, 1.56])
keys.append([-0.0199001, 0.0901653])

names.append("RAnkleRoll")
times.append([0.72, 1.56])
keys.append([0.066004, 0.078447])

names.append("RElbowRoll")
times.append([0.96, 1.56])
keys.append([0.428422, 0.413016])

names.append("RElbowYaw")
times.append([0.96, 1.56])
keys.append([1.91888, 1.19382])

names.append("RHand")
times.append([0.96, 1.56])
keys.append([0.53724, 0.3])

names.append("RHipPitch")
times.append([0.72, 1.56])
keys.append([-0.127364, 0.138378])

names.append("RHipRoll")
times.append([0.72, 1.56])
keys.append([-0.0291041, -0.0247833])

names.append("RHipYawPitch")
times.append([0.72, 1.56])
keys.append([-0.18097, -0.179863])

names.append("RKneePitch")
times.append([0.72, 1.56])
keys.append([0.227074, -0.0891823])

names.append("RShoulderPitch")
times.append([0.96, 1.56])
keys.append([1.4546, 1.46675])

names.append("RShoulderRoll")
times.append([0.96, 1.56])
keys.append([-0.229732, -0.18534])

names.append("RWristYaw")
times.append([0.96, 1.56])
keys.append([0.783567, 0.108709])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  # motion = ALProxy("ALMotion", IP, 9559)
  motion = ALProxy("ALMotion")
  motion.angleInterpolation(names, keys, times, True)
except BaseException, err:
  print err
