import math
import random

degree = math.pi/180.0 # radians per degree

# Ftar = -sin(head-target)
def FTarget(target_distance, target_angle):

    #do something useful here
    Ftar = math.sin(target_angle)
    #Ftar=0
    return Ftar

def FObstacle(obs_distance, obs_angle):
    too_far=10 #cm
    sigma = 0.01
    beta = 1

    if obs_distance < too_far:
        #do something useful here
        Fobs=math.exp(-(obs_angle)**2/(2*sigma**2))*(obs_angle)*math.exp(-obs_distance/beta) # needs replacing !
        #Fobs=0
    else:
        Fobs=0
    return Fobs

def FStochastic():
    """FStochastic adds noise to the turnrate force. This is just to make the simulation more realistic by adding some noie something useful here"""
    Kstoch=0.03
    
    Fstoch =Kstoch*random.randint(1,100)/100.0
    return Fstoch

def FOrienting(target_distance,robot):
    #do something useful here
    Forient=-math.exp(-target_distance)*math.sin(robot.phi)
    return Forient

def compute_velocity(sonar_distance_left, sonar_distance_right):
    max_velocity = 1.0
    max_distance = 10.0 #m
    min_distance = 1.0 #m

    if sonar_distance_left>max_distance and sonar_distance_right > max_distance:
        velocity = max_velocity
    elif sonar_distance_left<min_distance or sonar_distance_right < min_distance:
        velocity = max_velocity/max(sonar_distance_left,sonar_distance_right) + 0.5
    elif sonar_distance_left<sonar_distance_right:
        velocity = max_velocity*sonar_distance_left/max_distance
    else:
        velocity = max_velocity*sonar_distance_right/max_distance

    
    return velocity

# target_angle = target - robot_head
def compute_turnrate(robot, target_dist, target_angle, sonar_distance_left, sonar_distance_right):
    max_turnrate = 0.349 #rad/s # may need adjustment!

    delta_t = 1 # may need adjustment!
    sonar_angle_left = (robot.phi - 30) * degree 
    sonar_angle_right = (robot.phi + 30) * degree
    
    Fobs_left = FObstacle(sonar_distance_left, sonar_angle_left)
    Fobs_right = FObstacle(sonar_distance_right, sonar_angle_right)

    FTotal = FTarget(target_dist, target_angle) + \
             Fobs_left + \
             Fobs_right + \
             FOrienting(target_dist,robot) + \
             FStochastic()
             
    # turnrate: d phi(t) / dt = sum( forces ) 
    turnrate =  FTotal*delta_t
    
    #normalise turnrate value
    if turnrate>max_turnrate:
        turnrate=1.0
    else:
        turnrate=turnrate/max_turnrate

    return turnrate

if __name__=="__main__":
    pass
