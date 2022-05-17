from behaviour_navigation import BehaviourRobot
import numpy as np

# Braitenberg vehicle: LOVE
class BraitenbergLove(BehaviourRobot):
    def __init__(self):
        BehaviourRobot.__init__(self, "BraitenbergLove") 

    def FTarget(self, target_distance, target_angle):
        # do something useful here
        Ftar =- np.sin(-target_angle)
        return Ftar

    def FObstacle(self, obs_distance, obs_angle):
        too_far = 10 #cm

        if obs_distance < too_far:
            Fobs = 0
        else:
            Fobs = 0
        return Fobs

    def FOrienting(self):
        Forient=0
        return Forient

    def compute_velocity(self, target_distance, target_angle_robot):
        max_velocity = 4
        max_distance = 20 
        min_distance = 1 

        if target_distance >= max_distance:
            velocity = max_velocity
        else:
            if target_distance >=8:
                velocity = target_distance/8
            else:
                velocity = 0
        
        return velocity    

    def compute_turnrate(self, target_dist, target_angle, sonar_distance_left, sonar_distance_right, robot=None):
        max_turnrate = 0.349 # rad/s 
        delta_t = 1.0 
        
        Fobs_left = self.FObstacle(sonar_distance_left, self.sonar_angle_left)
        Fobs_right = self.FObstacle(sonar_distance_right, self.sonar_angle_right)

        FTotal = self.FTarget(target_dist, target_angle) + \
                Fobs_left + \
                Fobs_right + \
                self.FOrienting() + \
                self.FStochastic()

        # turnrate: d phi(t) / dt = sum( forces ) 
        turnrate =  FTotal*delta_t
        
        # normalize turnrate value
        if turnrate>max_turnrate:
            turnrate=1.0
        else:
            turnrate=turnrate/max_turnrate + 1

        return turnrate        

# Braitenberg vehicle: COWARD
class BraitenbergCoward(BehaviourRobot):
    def __init__(self):
        BehaviourRobot.__init__(self, "BraitenbergCoward")

    def FTarget(self, target_distance, target_angle):
        Ftar =- np.sin(-target_angle)
        return Ftar

    def FObstacle(self, obs_distance, obs_angle):
        too_far = 10 # cm

        if obs_distance < too_far:
            Fobs = 0 
        else:
            Fobs = 0

        return Fobs

    def FOrienting(self):
        Forient = 0
        return Forient

    def compute_velocity(self, target_distance, target_angle_robot):
        max_velocity = 1.0
        # modify the distance threshold here
        max_distance = 20 #m
        min_distance = 1 #m

        if target_distance >= max_distance:
            velocity = max_velocity
        else:   
            velocity = max_distance-target_distance + 1
        
        return velocity 

    def compute_turnrate(self, target_dist, target_angle, sonar_distance_left, sonar_distance_right, robot=None):
        max_turnrate = 0.349 # rad/s # may need adjustment!

        delta_t = 0.2 # may need adjustment!
        
        Fobs_left = self.FObstacle(sonar_distance_left, self.sonar_angle_left)
        Fobs_right = self.FObstacle(sonar_distance_right, self.sonar_angle_right)

        FTotal = self.FTarget(target_dist, target_angle) + \
                Fobs_left + \
                Fobs_right + \
                self.FOrienting() + \
                self.FStochastic()
                
        # turnrate: d phi(t) / dt = sum( forces ) 
        turnrate =  FTotal*delta_t
        
        # normalize turnrate value
        if turnrate>max_turnrate:
            turnrate=1.0
        else:
            turnrate=turnrate/max_turnrate

        max_distance = 20.0 # m

        if target_dist<max_distance:
            turnrate = turnrate - np.sign(target_angle)*(np.pi * 0.2)

        return turnrate
        
# Braitenberg vehicle: EXPLORE
class BraitenbergExplore(BehaviourRobot):
    def __init__(self):
        BehaviourRobot.__init__(self, "BraitenbergExplore")

    def FTarget(self, target_distance, target_angle):
        Ftar =- np.sin(-target_angle)
        return Ftar

    def FObstacle(self, obs_distance, obs_angle):
        too_far = 10 # cm

        if obs_distance < too_far:
            Fobs = 0 
        else:
            Fobs = 0

        return Fobs

    def FOrienting(self):
        Forient = 0
        return Forient

    def compute_velocity(self, target_dist, target_angle_robot):
        max_velocity = 1.0
        max_distance = 20 # m

        if target_dist > max_distance:
            velocity = max_velocity
        else:
            velocity = target_dist * max_velocity / max_distance

        return velocity

    def compute_turnrate(self, target_dist, target_angle, sonar_distance_left, sonar_distance_right, robot=None):
        max_turnrate = 0.349 #rad/s # may need adjustment!

        delta_t = 1 # may need adjustment!
        sonar_angle_left = np.radians(30)
        sonar_angle_right = np.radians(-30)
        max_distance = 20 #m
        
        Fobs_left = self.FObstacle(sonar_distance_left, sonar_angle_left)
        Fobs_right = self.FObstacle(sonar_distance_right, sonar_angle_right)

        FTotal = self.FTarget(target_dist, target_angle) + \
                Fobs_left + \
                Fobs_right + \
                self.FOrienting() + \
                self.FStochastic()
                
        # turnrate: d phi(t) / dt = sum( forces ) 
        turnrate =  FTotal*delta_t * target_dist / max_distance
        # turnrate =  FTotal*delta_t
        if target_dist > max_distance:
            turnrate = 0
        
        #normalise turnrate value
        if turnrate>max_turnrate:
            turnrate=1.0
        else:
            turnrate=turnrate/max_turnrate

        return turnrate


# Braitenberg vehicle: AGGRESSIVE
class BraitenbergAggressive(BehaviourRobot):
    def __init__(self):
        BehaviourRobot.__init__(self, "BraitenbergAggressive")

    def FTarget(self, target_distance, target_angle):
        Ftar =- np.sin(-target_angle)
        return Ftar

    def FObstacle(self, obs_distance, obs_angle):
        too_far = 10 # cm

        if obs_distance < too_far:
            Fobs = 0 
        else:
            Fobs = 0

        return Fobs

    def FOrienting(self):
        Forient = 0
        return Forient

    # Aggresive mode: if distance is small:
    def compute_velocity(self, target_distance, target_angle_robot):
        max_velocity = 1.0
        max_distance = 20 # m
        min_distance = 1 # m

        if target_distance >= max_distance:
            velocity = max_velocity
        else:
            velocity = max_distance-target_distance + 1

        return velocity

    def compute_turnrate(self, target_dist, target_angle, sonar_distance_left, sonar_distance_right, robot=None):
        max_turnrate = 0.349 # rad/s 
        delta_t = 0.2 
        
        Fobs_left = self.FObstacle(sonar_distance_left, self.sonar_angle_left)
        Fobs_right = self.FObstacle(sonar_distance_right, self.sonar_angle_right)

        FTotal = self.FTarget(target_dist, target_angle) + \
                Fobs_left + \
                Fobs_right + \
                self.FOrienting() + \
                self.FStochastic()
                
        # turnrate: d phi(t) / dt = sum( forces ) 
        turnrate =  FTotal*delta_t
        
        #normalise turnrate value
        if turnrate>max_turnrate:
            turnrate = 1.0
        else:
            turnrate = turnrate/max_turnrate

        return turnrate