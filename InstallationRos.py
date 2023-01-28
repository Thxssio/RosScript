#!/usr/bin/env python3
#          
#  ______ _    ___   __ _____ _____ _____ ____  
# |__   __| |  | \ \ / // ____/ ____|_   _/ __ \ 
#    | |  | |__| |\ V /| (___| (___   | || |  | |
#    | |  |  __  | > <  \___ \\___ \  | || |  | |
#    | |  | |  | |/ . \ ____) |___) |_| || |__| |
#    |_|  |_|  |_/_/ \_\_____/_____/|_____\____/ Ubuntu install of ROS Noetic
#
# Version: 1.0                    Written by Thxssio (DEX)
#
# 
# Github : https://github.com/thxssio

# imports

import subprocess
import os
import sys
from time import sleep


C = "\033[0m"     # clear (end)
R = "\033[0;31m"  # red (error)
G = "\033[0;32m"  # green (process)
B = "\033[0;36m"  # blue (choice)
Y = "\033[0;33m"  # yellow (info)


def check_root():
    id = int(subprocess.check_output("id -u", shell=True).decode("utf-8"))
    if id != 0:
        print(f"\n{R}(!){C} Execute como root (SUDO)!!\n")
        exit()


def check_distro():
    try:
        lsb_id = subprocess.check_output("lsb_release -i", shell=True).decode("utf-8")
        id = lsb_id.split(":")[-1].lower().strip()
    except Exception:
        id = ""
    return id


def banner():
    print(B)
    print(r"""  
    
 ________ __  ____   __ _____ _____ _____ ____  
 |__   __| |  | \ \ / // ____/ ____|_   _/ __ \ 
    | |  | |__| |\ V /| (___| (___   | || |  | |
    | |  |  __  | > <  \___ \\___ \  | || |  | |
    | |  | |  | |/ . \ ____) |___) |_| || |__| |
    |_|  |_|  |_/_/ \_\_____/_____/|_____\____/
    
    """,end="")
    print(f"{C} Ubuntu install of ROS Noetic\n")
    print(f"     Written by {B}Thxssio{C} (DEX)")



def install():
    # installer script
   

    print("\n   INSTALADOR ✔️")
    cmd1 = r'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
    cmd2 = 'sudo apt install curl'
    cmd3 = 'curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -'
    cmd4 = 'sudo apt update'
    cmd5 = 'sudo apt install ros-noetic-desktop-full'
    cmd6 = 'apt search ros-noetic'
    cmd7 = 'source /opt/ros/noetic/setup.bash'
    cmd8 = r'echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc'
    cmd9 = 'source ~/.bashrc'
    cmd10 = 'sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential'
    cmd11 = 'sudo apt install python3-rosdep'
    cmd12 = 'sudo rosdep init'
    cmd13 = 'sudo rosdep update'

    


    os.system(cmd1)
    print(f"{B}lista de Sources{C} {G}OK{C}")
    sleep(1)
    os.system(cmd2)
    print(f"{B}instalando o Curl{C}  {G}OK{C}")
    sleep(2)
    os.system(cmd3)
    print(f"{B}Executando o Curl{C} {G}OK{C}")
    sleep(1)
    os.system(cmd4)
    print(f"{B}Update{C} {G}OK{C}")
    sleep(2)
    os.system(cmd5)
    print(f"{B}Instalando o ROS{C} {G}OK{C}")  
    sleep(3)    
    os.system(cmd6)
    print(f"{B}Buscando o ROS na maquina{C} {G}OK{C}")
    sleep(3)  
    os.fspath(cmd7)
    print(f"{B}Source no bash{C} {G}OK{C}")
    sleep(3)
    os.system(cmd8)
    print(f"{B}Echo no Source{C} {G}OK{C}")
    sleep(2)
    os.fspath(cmd9)
    print(f"{B}Source no Bashrc{C} {G}OK{C}")
    sleep(2)
    os.system(cmd10)
    print(f"{B}Dependencias{C} {G}OK{C}")
    sleep(2)
    os.system(cmd11)
    print(f"{B}Rosdep{C} {G}OK{C}")
    sleep(2)
    os.system(cmd12)
    print(f"{B}Inicializando o ROS{C} {G}OK{C}")
    sleep(2)
    os.system(cmd13)
    print(f"{B}Atualizando o ROS{C} {G}OK{C}")




if __name__ == "__main__":
    check_root()  # checking root access
    banner()  # shows banner
    try:
        if len(sys.argv) != 2:
            raise Exception("Número inválido de argumentos: Use '-i'")
        if sys.argv[-1] in ["-i", "--install"]:
            install()  # installer
        else:
            raise Exception("Argumento inválido fornecido: use '-i'")
    except Exception as e:
        print(f"\n{R}(!){C} Ocorreu um erro inesperado ao executar o script !!\n")
        print(f"{R}(!){C} ERROR : {R}{e}{C}")
        exit()

