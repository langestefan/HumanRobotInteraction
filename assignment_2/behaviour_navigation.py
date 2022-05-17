import abc
import numpy as np

class BehaviourRobot(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, name):
        self.name = name
        self.sonar_angle_left = np.radians(30)
        self.sonar_angle_right = np.radians(-30)   

    @abc.abstractmethod
    def FTarget(self, target_distance, target_angle):
        pass

    @abc.abstractmethod
    def FObstacle(self, obs_distance, obs_angle):
        pass

    @abc.abstractmethod
    def FOrienting(self, target_distance, robot):
        pass

    @abc.abstractmethod
    def compute_turnrate(self, target_dist, target_angle, sonar_distance_left, sonar_distance_right, robot=None):
        pass

    @abc.abstractmethod
    def compute_velocity(self, target_distance, target_angle_robot):
        pass

    def FStochastic(self):
        """ FStochastic adds noise to the turnrate force. This is just to make the simulation more realistic. """
        Kstoch = 0.03
        Fstoch = Kstoch * np.random.randint(1, 100)/100.0
        return Fstoch

