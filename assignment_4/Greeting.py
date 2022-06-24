# Choregraphe simplified export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.36, 0.72, 1.12, 1.56, 1.72, 2.04])
keys.append([-0.349904, -0.175413, 0.0724282, -0.09203, -0.0154342, -0.164301])

names.append("HeadYaw")
times.append([0.36, 0.72, 0.96, 1.12, 1.28, 1.48, 1.72, 2.04])
keys.append([-0.0156179, -0.0135287, -0.101865, 0.0859812, -0.101865, 0.0859812, -0.0173475, -0.0123995])

names.append("LAnklePitch")
times.append([0.36, 0.72, 1.32, 2.04])
keys.append([0.0957674, -0.154976, 0.0901653, 0.0896555])

names.append("LAnkleRoll")
times.append([0.36, 0.72, 1.32, 2.04])
keys.append([-0.185333, -0.136484, -0.078447, -0.123031])

names.append("LElbowRoll")
times.append([0.36, 0.72, 1.32, 2.04])
keys.append([-0.425005, -0.68766, -0.425288, -0.416156])

names.append("LElbowYaw")
times.append([0.36, 0.72, 1.32, 2.04])
keys.append([-1.20474, -1.56381, -1.20557, -1.19838])

names.append("LHand")
times.append([0.36, 0.72, 1.32, 2.04])
keys.append([0.305394, 0.62, 0.314203, 0.306419])

names.append("LHipPitch")
times.append([0.36, 0.72, 1.32, 2.04])
keys.append([0.120194, -0.12728, 0.138378, 0.133664])

names.append("LHipRoll")
times.append([0.36, 0.72, 1.32, 2.04])
keys.append([0.187996, 0.11049, 0.0247833, 0.1])

names.append("LHipYawPitch")
times.append([0.36, 0.72, 1.32, 2.04])
keys.append([-0.179863, -0.179436, -0.179863, -0.177764])

names.append("LKneePitch")
times.append([0.36, 0.72, 1.32, 2.04])
keys.append([-0.0878086, 0.41107, -0.0891823, -0.0806209])

names.append("LShoulderPitch")
times.append([0.36, 0.72, 1.32, 2.04])
keys.append([1.41011, 1.77151, 1.40624, 1.46352])

names.append("LShoulderRoll")
times.append([0.36, 0.72, 1.32, 2.04])
keys.append([0.241407, 0.518363, 0.246933, 0.18874])

names.append("LWristYaw")
times.append([0.36, 0.72, 1.32, 2.04])
keys.append([-0.111101, -0.111101, -0.108112, 0.0977037])

names.append("RAnklePitch")
times.append([0.36, 0.72, 1.32, 2.04])
keys.append([0.0901653, -0.116542, 0.0957674, 0.0912732])

names.append("RAnkleRoll")
times.append([0.36, 0.72, 1.32, 2.04])
keys.append([0.078447, 0.139636, 0.185333, 0.13748])

names.append("RElbowRoll")
times.append([0.36, 0.56, 0.96, 1.32, 2.04])
keys.append([0.431716, 0.429253, 0.998328, 0.428422, 0.413016])

names.append("RElbowYaw")
times.append([0.36, 0.72, 1.12, 1.32, 2.04])
keys.append([1.21446, 2.02109, 2.02008, 1.91888, 1.19382])

names.append("RHand")
times.append([0.36, 0.72, 0.96, 1.12, 1.32, 2.04])
keys.append([0.315043, 0.81, 0.84, 0.65, 0.53724, 0.3])

names.append("RHipPitch")
times.append([0.36, 0.72, 1.32, 2.04])
keys.append([0.138378, -0.073674, 0.120194, 0.124909])

names.append("RHipRoll")
times.append([0.36, 0.72, 1.32, 2.04])
keys.append([-0.0247833, -0.115008, -0.187996, -0.1])

names.append("RHipYawPitch")
times.append([0.36, 0.72, 1.32, 2.04])
keys.append([-0.179863, -0.179436, -0.179863, -0.177764])

names.append("RKneePitch")
times.append([0.36, 0.72, 1.32, 2.04])
keys.append([-0.0891823, 0.316046, -0.0878086, -0.0875715])

names.append("RShoulderPitch")
times.append([0.36, 0.72, 1.12, 1.32, 2.04])
keys.append([1.41886, 1.14145, 1.42942, 1.4546, 1.46675])

names.append("RShoulderRoll")
times.append([0.36, 0.72, 1.12, 1.32, 2.04])
keys.append([-0.237396, -0.238199, -0.237396, -0.229732, -0.18534])

names.append("RWristYaw")
times.append([0.36, 0.72, 1.12, 1.32, 2.04])
keys.append([-0.0875347, 0.912807, 0.90059, 0.783567, 0.108709])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  # motion = ALProxy("ALMotion", IP, 9559)
  motion = ALProxy("ALMotion")
  motion.angleInterpolation(names, keys, times, True)
except BaseException, err:
  print err
