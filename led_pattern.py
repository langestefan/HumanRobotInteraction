import assignment_2.nao_nocv_2_1 as nao
from definitions import marvin, bender

from time import sleep



def main():
    nao.InitProxy(marvin['ip_address'])
    # nao.InitPose()


    # LED pattern

    color_range = range(50, 100, 5)

    while True:
        for i in color_range:
            # nao.EyeLED(color=[10, 10, i], interpol_time=0.1)
            nao.EarLED(i//1, interpol_time=0.1)
            sleep(0.1)

        for i in color_range[::-1]:
            # nao.EyeLED(color=[10, 10, i], interpol_time=0.1)
            nao.EarLED(i//1, interpol_time=0.1)
            sleep(0.1)





    # nao.Crouch()


if __name__ == '__main__':
    main()