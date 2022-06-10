import assignment_2.nao_nocv_2_1 as nao
from definitions import marvin



def main():
    nao.InitProxy(marvin['ip_address'])
    nao.InitPose()


if __name__ == '__main__':
    main()