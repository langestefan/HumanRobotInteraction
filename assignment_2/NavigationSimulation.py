from behaviour_navigation import BehaviourRobot
import numpy as np

# Autonomous robot behaviour for challenge 3
class AutonomousRobot(BehaviourRobot):
    def __init__(self):
        BehaviourRobot.__init__(self, "AutonomousRobot")

    # Ftar = -sin(head-target)
    def FTarget(self, target_distance, target_angle):
        Ftar = np.sin(target_angle)
        return Ftar

    def FObstacle(self, obs_distance, obs_angle):
        too_far = 7.5 # cm
        sigma = 5 # 0.01
        beta = 8

        print("obs_distance: ", obs_distance)
        print("obs_angle: ", obs_angle)

        if obs_distance < too_far:
            Fobs = np.exp(-(obs_angle)**2/(2*sigma**2))*(obs_angle) * np.exp(-obs_distance/beta)
        else:
            Fobs=0
        return Fobs

    def FOrienting(self, target_distance,robot):
        #do something useful here
        Forient= - np.exp(-target_distance)*np.sin(robot.phi)
        return Forient

    def compute_velocity(self, sonar_distance_left, sonar_distance_right):
        max_velocity = 2.0
        max_distance = 10.0 #m
        min_distance = 3.0 #m

        if sonar_distance_left>max_distance and sonar_distance_right > max_distance:
            velocity = max_velocity
        elif sonar_distance_left<min_distance or sonar_distance_right < min_distance:
            velocity = max_velocity / max(sonar_distance_left,sonar_distance_right) + 1
        elif sonar_distance_left<sonar_distance_right:
            velocity = max_velocity*sonar_distance_left/max_distance
        else:
            velocity = max_velocity*sonar_distance_right/max_distance

        print sonar_distance_left, sonar_distance_right

        return velocity

    # target_angle = target - robot_head
    def compute_turnrate(self, target_dist, target_angle, sonar_distance_left, sonar_distance_right, robot):
        max_turnrate = 0.5 #rad/s # may need adjustment!

        delta_t = 0.5 # may need adjustment!
        sonar_angle_left = np.radians((np.degrees(robot.phi) - 30))
        sonar_angle_right = np.radians((np.degrees(robot.phi) + 30))
        
        Fobs_left = self.FObstacle(sonar_distance_left, sonar_angle_left)
        Fobs_right = self.FObstacle(sonar_distance_right, sonar_angle_right)
        Ftarget = self.FTarget(target_dist, target_angle)
        Forient = self.FOrienting(target_dist, robot)
        Fstoch = self.FStochastic()

        # print all the forces
        print("Fobs_left: ", Fobs_left)
        print("Fobs_right: ", Fobs_right)

        # force weights
        w_obs = 1
        w_target = 0.15
        w_orient = 1.5
        w_stoch = 0.5
        
        Fobs = -1*Fobs_left if Fobs_left > Fobs_right else Fobs_right

        FTotal = w_target * Ftarget + \
                    w_obs * Fobs + \
                    w_orient * Forient + \
                    w_stoch * Fstoch     
                
        # turnrate: d phi(t) / dt = sum( forces ) 
        turnrate =  FTotal*delta_t
        
        #normalise turnrate value
        if turnrate>max_turnrate:
            turnrate = 1.0
        else:
            turnrate = turnrate/max_turnrate

        return turnrate       