from requests import post
from sqlalchemy import false, true
import assignment_2.nao_nocv_2_1 as nao
from definitions import marvin, bender

from time import sleep
import time

from statemachine import StateMachine, State


def flashing_leds(duration_sec=5):
    max_intensity = 250
    timestep = 0.5
    post = True

    while true:
        # for timing
        time_start = time.time()

        nao.EarLED(max_intensity/255, interpol_time=timestep, POST = post)
        sleep(timestep)
        nao.EarLED(0, interpol_time=timestep, POST = post)
            

        # for timing
        time_end = time.time()

        if time_end - time_start > duration_sec:
            break

def breathing_leds(duration_sec=60):

    intensity_range = range(10, 250, 20)
    timestep = 0.2
    post = True

    while true:
        # for timing
        time_start = time.time()

        for i in intensity_range:
            # nao.EyeLED(color=[10, 10, i], interpol_time=0.1)
            nao.EarLED(i/200, interpol_time=timestep, POST = post)
            nao.EyeLED(color=[0, 0, i], interpol_time=timestep, POST = post)
            sleep(timestep)

        # breathing pause
        time.sleep(2)

        for i in intensity_range[::-1]:
            # nao.EyeLED(color=[10, 10, i], interpol_time=0.1)
            nao.EarLED(i/200, interpol_time=timestep, POST = post)
            nao.EyeLED(color=[0, 0, i], interpol_time=timestep, POST = post)
            sleep(timestep)
        
        # for timing
        time_end = time.time()

        if time_end - time_start > duration_sec:
            break



class NaoStates(StateMachine):
    # states
    idle = State('Idle', initial=True)                  # initial state
    scanning = State('Scanning')                        # start scanning for a person
    detecting = State('Detecting')                      # detected a person
    approaching = State('Approaching')                  # approaching the person
    getting_attention = State('GettingAttention')       # getting attention

    # state transitions
    startscan = idle.to(scanning)                       # start scanning for a person from the idle state
    detected = scanning.to(detecting)                   # detected a person while scanning
    approach = detecting.to(approaching)                # approaching the person after detected
    approach_pause = approaching.to(idle)               # when we approached the person, pause for a while at certain distance
    get_attention = approaching.to(getting_attention)   # we should start the choreograph here

    # callbacks
    def on_startscan(self):
        print('Starting to scan for a person') 

        # breathing led pattern
        breathing_leds()

    def on_detected(self):
        print('Detected a person')

        # turn facetracking on
        
        # turn eyes green, flashing

    def on_approach(self):
        print('Approaching the person')



def main():

    # initialize the state machine
    nao_states = NaoStates()

    # print current state
    print("Current state: {0}".format(nao_states.current_state))

    # init proxy
    nao.InitProxy(marvin['ip_address'])
    # nao.InitProxy(bender['ip_address'])

    # start scanning
    nao_states.startscan()


    # # nao.InitPose()


    # # LED pattern

    # color_range = range(50, 100, 5)

    # nao.Crouch()


if __name__ == '__main__':
    main()