import nao_nocv_2_1 as nao
from time import sleep

marvin = {'ip_address' : '192.168.0.115', 'colour' :'orange'}
bender = {'ip_address' : '192.168.0.112', 'colour' :'red'}

def main():
    nao.InitProxy(bender['ip_address'])
    nao.InitPose()

    # init sonar
    nao.InitSonar()

    while(True):
        SonarLeft, SonarRight = nao.ReadSonar()
        print("SonarLeft, SonarRight: ", SonarLeft, SonarRight)
        sleep(0.5)

    # rotate the robot in place
    nao.Move(dx=0, dy=0, dtheta=0.5, freq=1)
    nao.Crouch()

if __name__ == "__main__":
    main()

