import assignment_2.braitenberg_vehicles as brait_vehicle
import assignment_2.pygame_helpers as pygame_helpers
import assignment_2.NavigationSimulation as NavigationSimulation

def main():
    # select a Braitenberg robot
    # robot_select = "BraitenbergLove"
    # robot_select = "BraitenbergCoward"
    # robot_select = "BraitenbergExplore"
    # robot_select = "BraitenbergAggressive"

    # select challenge 3 robot to test navigation simulation in pygame
    robot_select = "NavigationSimulation"

    # braitenberg vehicles
    if robot_select == "BraitenbergLove":
        robot = brait_vehicle.BraitenbergLove()
    elif robot_select == "BraitenbergCoward":
        robot = brait_vehicle.BraitenbergCoward()
    elif robot_select == "BraitenbergExplore":
        robot = brait_vehicle.BraitenbergExplore()
    elif robot_select == "BraitenbergAggressive":
        robot = brait_vehicle.BraitenbergAggressive()
    elif robot_select == "NavigationSimulation":
        robot = NavigationSimulation.AutonomousRobot()
    else:
        print("Unknown robot! Check settings!")
        return

    # challenge 3 real world navigation part 
    # elif robot_select == "BehaviourNavigation":
    #     robot = ... # from realworld navigation implementation

    obstables = True if robot_select == "NavigationSimulation" else False
        
    # after everything is defined we run the main loop for infinity
    pygame_helpers.mainloop(robot, draw_obstacles=obstables)


if __name__ == '__main__':
    main()