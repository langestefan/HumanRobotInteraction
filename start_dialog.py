#Simple dialog in Python
# -*- encoding: UTF-8 -*-

# from ipaddress import ip_address
from naoqi import ALProxy
import os, sys

# for relative imports to work in notebooks
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from definitions import marvin

def main(robot_ip, robot_port, topf_path):
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

    # dialog location
    base_path = '/home/nao/group_05/'
    dialog_name = 'mydialog_enu.top'

    # dialog topic
    dialog_topic = os.path.join(base_path, dialog_name)  # Absolute path of the dialog topic file (on the robot).
    print("Dialog location: {0}".format(dialog_topic))

    # robot ip/port
    robot_ip = marvin['ip_address'] 
    port = 9559 # Robot port number

    main(robot_ip, port, dialog_topic)
