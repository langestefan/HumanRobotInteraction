import nao_nocv_2_1 as nao #with this line you import all the

def main():
    # # test on realy robot
    # nao.InitProxy(marvin['ip_address'])
    # nao.InitPose()
    
    # test on virtual robot
    nao.InitProxy("127.0.0.1") #with this line you initialize all the proxies, and indicate the IP-adres. In this case this is 127.0.0.1, because this is your home ip-adress.

    nao.InitPose() #this line makes the robot stand up

    nao.sleep(5)

    nao.RunMovement("Greeting.py") # check the human and greeting

    nao.sleep(5)

    nao.MoveHead(yaw_val=0, pitch_val=-2)  # eye contact with the human 

    nao.RunMovement("meds_reminder.py") # motion during the meds reminder

    nao.sleep(5)

    nao.RunMovement("excited.py")  # Negtive feedback

    nao.sleep(5)

    nao.GoToPosture("Stand")

    nao.Crouch() #this line makes the robot crouch 

if __name__ == '__main__':
    main()