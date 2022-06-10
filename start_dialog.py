#Simple dialog in Python
# -*- encoding: UTF-8 -*-

# from ipaddress import ip_address
from naoqi import ALProxy
import assignment_2.nao_nocv_2_1 as nao
import os, sys

from statemachine import StateMachine, State

# for relative imports to work in notebooks
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from definitions import marvin

def main(robot_ip, robot_port, topf_path):
    # nao.InitProxy(robot_ip)
    # nao.Say("Hey user, what is your name?")

    dialog_p = ALProxy('ALDialog', robot_ip, robot_port)
    dialog_p.setLanguage("English")

    # Load topic - absolute path is required
    topf_path = topf_path.decode('utf-8')
    topic = dialog_p.loadTopic(topf_path.encode('utf-8'))

    # Start dialog
    dialog_p.subscribe('myModule')

    # Activate dialog
    dialog_p.activateTopic(topic)

    raw_input(u"Press 'Enter' to exit.")

    # Deactivate topic
    dialog_p.deactivateTopic(topic)

    # Unload topic
    dialog_p.unloadTopic(topic)

    # Stop dialog
    dialog_p.unsubscribe('myModule')
    

if __name__ == '__main__':
    # get dialog filenames
    dialog_filenames_path = 'dialog_file_name.txt'

    # list all dialog files
    files = [f.strip() for f in open(dialog_filenames_path, 'r').readlines()]
    
    # ends with .top
    topf_path = [f for f in files if f.endswith('.top')]
    dlgf_path = [f for f in files if f.endswith('.dlg')]

    # dialog location
    topics = {
        'BiddingFarewell': 'BiddingFarewell_enu.top',
        'GetAttention': 'GetAttention_enu.top',
        'Brain_exercise:': 'Brain_exercise_enu.top',
        'InquiryReminder': 'InquiryReminder_enu.top',
        'Small_talk_1_enu': 'Small_talk_1_enu.top'
    }

    # select topic here
    topic = topics['BiddingFarewell']
    print("Using topic: ", topic)

    # get dialog file path on Nao robot
    nao_base_path = '/home/nao/group_05/'

    # dialog topic
    dialog_topic = os.path.join(nao_base_path, topic)  # Absolute path of the dialog topic file (on the robot).
    print("Dialog location: {0}".format(dialog_topic))

    # robot ip/port
    robot_ip = marvin['ip_address'] 
    port = 9559 # Robot port number

    main(robot_ip, port, dialog_topic)
