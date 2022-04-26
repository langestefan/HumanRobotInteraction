import nao_nocv_2_1 as nao  # with this line you import all the functions of the naolibrary and are able to call them with “nao”
nao.InitProxy("127.0.0.1")  # with this line you initialize all the proxies, and indicate the IP-adres. In this case this is 127.0.0.1, because this is your home ip-adress.
nao.InitPose()              # this line makes the robot stand up
nao.Walk(1, 0, 0)           # this line makes the robot walk 1 meter in x direction
nao.Crouch()                # this line makes the robot crouch