# Choregraphe bezier export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.24, 0.52, 0.64, 0.84, 1, 1.2, 1.36, 1.52, 1.96])
keys.append([[-0.671952, [3, -0.0933333, 0], [3, 0.0933333, 0]], [-0.0244346, [3, -0.0933333, 0], [3, 0.04, 0]], [-0.502655, [3, -0.04, 0], [3, 0.0666667, 0]], [-0.195477, [3, -0.0666667, 0], [3, 0.0533333, 0]], [-0.502655, [3, -0.0533333, 0], [3, 0.0666667, 0]], [-0.195477, [3, -0.0666667, 0], [3, 0.0533333, 0]], [-0.502655, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.195477, [3, -0.0533333, 0], [3, 0.146667, 0]], [-0.439823, [3, -0.146667, 0], [3, 0, 0]]])

names.append("HeadYaw")
times.append([0.24, 1.96])
keys.append([[-0.016916, [3, -0.0933333, 0], [3, 0.573333, 0]], [-0.016916, [3, -0.573333, 0], [3, 0, 0]]])

names.append("LAnklePitch")
times.append([0.52, 0.68, 0.84, 1, 1.16, 1.32, 1.48, 1.64, 1.8, 1.96])
keys.append([[-0.142704, [3, -0.186667, 0], [3, 0.0533333, 0]], [-0.182588, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.142704, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.182588, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.142704, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.182588, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.142704, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.182588, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.142704, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.182588, [3, -0.0533333, 0], [3, 0, 0]]])

names.append("LAnkleRoll")
times.append([0.52, 0.68, 0.84, 1, 1.16, 1.32, 1.48, 1.64, 1.8, 1.96])
keys.append([[-0.110406, [3, -0.186667, 0], [3, 0.0533333, 0]], [-0.110406, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.110406, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.110406, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.110406, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.110406, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.110406, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.110406, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.110406, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.110406, [3, -0.0533333, 0], [3, 0, 0]]])

names.append("LElbowRoll")
times.append([0.36, 0.68, 0.84, 1, 1.16, 1.32, 1.48, 1.64, 1.8, 1.96, 2.12])
keys.append([[-1.49226, [3, -0.133333, 0], [3, 0.106667, 0]], [-1.50021, [3, -0.106667, 0], [3, 0.0533333, 0]], [-1.30027, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-1.50021, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-1.30027, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-1.50021, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-1.30027, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-1.50021, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-1.30027, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-1.50021, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-1.30027, [3, -0.0533333, 0], [3, 0, 0]]])

names.append("LElbowYaw")
times.append([0.68, 1, 1.32, 1.64, 1.96])
keys.append([[-1.42053, [3, -0.24, 0], [3, 0.106667, 0]], [-1.42053, [3, -0.106667, 0], [3, 0.106667, 0]], [-1.42053, [3, -0.106667, 0], [3, 0.106667, 0]], [-1.42053, [3, -0.106667, 0], [3, 0.106667, 0]], [-1.42053, [3, -0.106667, 0], [3, 0, 0]]])

names.append("LHand")
times.append([0.36, 0.68, 0.84, 1, 1.16, 1.32, 1.48, 1.64, 1.8, 1.96, 2.12])
keys.append([[0.63, [3, -0.133333, 0], [3, 0.106667, 0]], [0.27, [3, -0.106667, 0.14], [3, 0.0533333, -0.07]], [0, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0.24, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0.28, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0.26, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0.24, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0, [3, -0.0533333, 0], [3, 0, 0]]])

names.append("LHipPitch")
times.append([0.52, 0.68, 0.84, 1, 1.16, 1.32, 1.48, 1.64, 1.8, 1.96])
keys.append([[-0.489305, [3, -0.186667, 0], [3, 0.0533333, 0]], [-0.665714, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.489305, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.665714, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.489305, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.665714, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.489305, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.665714, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.489305, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.665714, [3, -0.0533333, 0], [3, 0, 0]]])

names.append("LHipRoll")
times.append([0.52, 0.68, 0.84, 1, 1.16, 1.32, 1.48, 1.64, 1.8, 1.96])
keys.append([[0.075208, [3, -0.186667, 0], [3, 0.0533333, 0]], [0.075208, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0.075208, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0.075208, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0.075208, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0.075208, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0.075208, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0.075208, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0.075208, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0.075208, [3, -0.0533333, 0], [3, 0, 0]]])

names.append("LHipYawPitch")
times.append([0.52, 0.68, 0.84, 1, 1.16, 1.32, 1.48, 1.64, 1.8, 1.96])
keys.append([[-0.205514, [3, -0.186667, 0], [3, 0.0533333, 0]], [-0.226991, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.205514, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.226991, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.205514, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.226991, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.205514, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.226991, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.205514, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.226991, [3, -0.0533333, 0], [3, 0, 0]]])

names.append("LKneePitch")
times.append([0.52, 0.68, 0.84, 1, 1.16, 1.32, 1.48, 1.64, 1.8, 1.96])
keys.append([[0.645772, [3, -0.186667, 0], [3, 0.0533333, 0]], [0.819114, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0.645772, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0.819114, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0.645772, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0.819114, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0.645772, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0.819114, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0.645772, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0.819114, [3, -0.0533333, 0], [3, 0, 0]]])

names.append("LShoulderPitch")
times.append([0.28, 0.6, 0.76, 0.92, 1.08, 1.24, 1.4, 1.56, 1.72, 1.88, 2.04])
keys.append([[0.945968, [3, -0.106667, 0], [3, 0.106667, 0]], [1.15541, [3, -0.106667, -0.059729], [3, 0.0533333, 0.0298645]], [1.21475, [3, -0.0533333, 0], [3, 0.0533333, 0]], [1.15541, [3, -0.0533333, 0], [3, 0.0533333, 0]], [1.21475, [3, -0.0533333, 0], [3, 0.0533333, 0]], [1.15541, [3, -0.0533333, 0], [3, 0.0533333, 0]], [1.21475, [3, -0.0533333, 0], [3, 0.0533333, 0]], [1.15541, [3, -0.0533333, 0], [3, 0.0533333, 0]], [1.21475, [3, -0.0533333, 0], [3, 0.0533333, 0]], [1.15541, [3, -0.0533333, 0], [3, 0.0533333, 0]], [1.21475, [3, -0.0533333, 0], [3, 0, 0]]])

names.append("LShoulderRoll")
times.append([0.28, 0.6, 0.92, 1.24, 1.56, 1.88])
keys.append([[0.223402, [3, -0.106667, 0], [3, 0.106667, 0]], [-0.11049, [3, -0.106667, 0], [3, 0.106667, 0]], [-0.11049, [3, -0.106667, 0], [3, 0.106667, 0]], [-0.11049, [3, -0.106667, 0], [3, 0.106667, 0]], [-0.11049, [3, -0.106667, 0], [3, 0.106667, 0]], [-0.11049, [3, -0.106667, 0], [3, 0, 0]]])

names.append("LWristYaw")
times.append([0.36, 0.68, 1, 1.32, 1.64, 1.96])
keys.append([[-0.630064, [3, -0.133333, 0], [3, 0.106667, 0]], [0.101202, [3, -0.106667, 0], [3, 0.106667, 0]], [0.101202, [3, -0.106667, 0], [3, 0.106667, 0]], [0.101202, [3, -0.106667, 0], [3, 0.106667, 0]], [0.101202, [3, -0.106667, 0], [3, 0.106667, 0]], [0.101202, [3, -0.106667, 0], [3, 0, 0]]])

names.append("RAnklePitch")
times.append([0.52, 0.68, 0.84, 1, 1.16, 1.32, 1.48, 1.64, 1.8, 1.96])
keys.append([[-0.187106, [3, -0.186667, 0], [3, 0.0533333, 0]], [-0.233125, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.187106, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.233125, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.187106, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.233125, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.187106, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.233125, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.187106, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.233125, [3, -0.0533333, 0], [3, 0, 0]]])

names.append("RAnkleRoll")
times.append([0.52, 0.68, 0.84, 1, 1.16, 1.32, 1.48, 1.64, 1.8, 1.96])
keys.append([[0.124296, [3, -0.186667, 0], [3, 0.0533333, 0]], [0.124296, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0.124296, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0.124296, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0.124296, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0.124296, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0.124296, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0.124296, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0.124296, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0.124296, [3, -0.0533333, 0], [3, 0, 0]]])

names.append("RElbowRoll")
times.append([0.36, 0.56, 0.72, 0.88, 1.04, 1.2, 1.36, 1.52, 1.68, 1.84, 2])
keys.append([[1.49226, [3, -0.133333, 0], [3, 0.0666667, 0]], [1.48649, [3, -0.0666667, 0.00576827], [3, 0.0533333, -0.00461462]], [1.30027, [3, -0.0533333, 0], [3, 0.0533333, 0]], [1.48649, [3, -0.0533333, 0], [3, 0.0533333, 0]], [1.30027, [3, -0.0533333, 0], [3, 0.0533333, 0]], [1.48649, [3, -0.0533333, 0], [3, 0.0533333, 0]], [1.30027, [3, -0.0533333, 0], [3, 0.0533333, 0]], [1.48649, [3, -0.0533333, 0], [3, 0.0533333, 0]], [1.30027, [3, -0.0533333, 0], [3, 0.0533333, 0]], [1.48649, [3, -0.0533333, 0], [3, 0.0533333, 0]], [1.30027, [3, -0.0533333, 0], [3, 0, 0]]])

names.append("RElbowYaw")
times.append([0.56, 0.88, 1.2, 1.52, 1.84])
keys.append([[1.33914, [3, -0.2, 0], [3, 0.106667, 0]], [1.33914, [3, -0.106667, 0], [3, 0.106667, 0]], [1.33914, [3, -0.106667, 0], [3, 0.106667, 0]], [1.33914, [3, -0.106667, 0], [3, 0.106667, 0]], [1.33914, [3, -0.106667, 0], [3, 0, 0]]])

names.append("RHand")
times.append([0.36, 0.56, 0.72, 0.88, 1.04, 1.2, 1.36, 1.52, 1.68, 1.84, 2])
keys.append([[0.63, [3, -0.133333, 0], [3, 0.0666667, 0]], [0.27, [3, -0.0666667, 0.116667], [3, 0.0533333, -0.0933333]], [0, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0.24, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0.28, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0.26, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0.24, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0, [3, -0.0533333, 0], [3, 0, 0]]])

names.append("RHipPitch")
times.append([0.52, 0.68, 0.84, 1, 1.16, 1.32, 1.48, 1.64, 1.8, 1.96])
keys.append([[-0.48632, [3, -0.186667, 0], [3, 0.0533333, 0]], [-0.665798, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.48632, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.665798, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.48632, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.665798, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.48632, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.665798, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.48632, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.665798, [3, -0.0533333, 0], [3, 0, 0]]])

names.append("RHipRoll")
times.append([0.52, 0.68, 0.84, 1, 1.16, 1.32, 1.48, 1.64, 1.8, 1.96])
keys.append([[-0.075124, [3, -0.186667, 0], [3, 0.0533333, 0]], [-0.0643861, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.075124, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.0643861, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.075124, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.0643861, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.075124, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.0643861, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.075124, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.0643861, [3, -0.0533333, 0], [3, 0, 0]]])

names.append("RHipYawPitch")
times.append([0.52, 0.68, 0.84, 1, 1.16, 1.32, 1.48, 1.64, 1.8, 1.96])
keys.append([[-0.205514, [3, -0.186667, 0], [3, 0.0533333, 0]], [-0.226991, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.205514, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.226991, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.205514, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.226991, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.205514, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.226991, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.205514, [3, -0.0533333, 0], [3, 0.0533333, 0]], [-0.226991, [3, -0.0533333, 0], [3, 0, 0]]])

names.append("RKneePitch")
times.append([0.52, 0.68, 0.84, 1, 1.16, 1.32, 1.48, 1.64, 1.8, 1.96])
keys.append([[0.664264, [3, -0.186667, 0], [3, 0.0533333, 0]], [0.843741, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0.664264, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0.843741, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0.664264, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0.843741, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0.664264, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0.843741, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0.664264, [3, -0.0533333, 0], [3, 0.0533333, 0]], [0.843741, [3, -0.0533333, 0], [3, 0, 0]]])

names.append("RShoulderPitch")
times.append([0.28, 0.48, 0.64, 0.8, 0.96, 1.12, 1.28, 1.44, 1.6, 1.76, 1.92])
keys.append([[0.945968, [3, -0.106667, 0], [3, 0.0666667, 0]], [1.15541, [3, -0.0666667, -0.0497742], [3, 0.0533333, 0.0398194]], [1.21475, [3, -0.0533333, 0], [3, 0.0533333, 0]], [1.15541, [3, -0.0533333, 0], [3, 0.0533333, 0]], [1.21475, [3, -0.0533333, 0], [3, 0.0533333, 0]], [1.15541, [3, -0.0533333, 0], [3, 0.0533333, 0]], [1.21475, [3, -0.0533333, 0], [3, 0.0533333, 0]], [1.15541, [3, -0.0533333, 0], [3, 0.0533333, 0]], [1.21475, [3, -0.0533333, 0], [3, 0.0533333, 0]], [1.15541, [3, -0.0533333, 0], [3, 0.0533333, 0]], [1.21475, [3, -0.0533333, 0], [3, 0, 0]]])

names.append("RShoulderRoll")
times.append([0.28, 0.48, 0.8, 1.12, 1.44, 1.76])
keys.append([[-0.223402, [3, -0.106667, 0], [3, 0.0666667, 0]], [0.075124, [3, -0.0666667, 0], [3, 0.106667, 0]], [0.075124, [3, -0.106667, 0], [3, 0.106667, 0]], [0.075124, [3, -0.106667, 0], [3, 0.106667, 0]], [0.075124, [3, -0.106667, 0], [3, 0.106667, 0]], [0.075124, [3, -0.106667, 0], [3, 0, 0]]])

names.append("RWristYaw")
times.append([0.36, 0.56, 0.88, 1.2, 1.52, 1.84])
keys.append([[0.630064, [3, -0.133333, 0], [3, 0.0666667, 0]], [0.110406, [3, -0.0666667, 0], [3, 0.106667, 0]], [0.110406, [3, -0.106667, 0], [3, 0.106667, 0]], [0.110406, [3, -0.106667, 0], [3, 0.106667, 0]], [0.110406, [3, -0.106667, 0], [3, 0.106667, 0]], [0.110406, [3, -0.106667, 0], [3, 0, 0]]])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  # motion = ALProxy("ALMotion", IP, 9559)
  motion = ALProxy("ALMotion")
  motion.angleInterpolationBezier(names, times, keys)
except BaseException, err:
  print err
