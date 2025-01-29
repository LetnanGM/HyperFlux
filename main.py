import os
import sys
import time
import subprocess
from module.l4 import *
from module.l7 import *
from module.method import *
from Tools.main import *
from colorama import Fore, init
init(autoreset=True)

def check_main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
    {Fore.LIGHTGREEN_EX}                


                                     ___ _            
        /\  /\_   _ _ __   ___ _ __ / __\ |_   ___  __
       / /_/ / | | | '_ \ / _ \ '__/ _\ | | | | \ \/ /
      / __  /| |_| | |_) |  __/ | / /   | | |_| |>  < 
      \/ /_/  \__, | .__/ \___|_| \/    |_|\__,_/_/\_\
              |___/|_|                                
                ╔════════════════════════╗
                ║   [INFO] version 3.0   ║    
                ╚════════════════════════╝            
                     
""")
    print(Fore.LIGHTGREEN_EX,"[INFO] Enter the continue...")
    
def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.LIGHTGREEN_EX,"""


                                    ___ _            
       /\  /\_   _ _ __   ___ _ __ / __\ |_   ___  __
      / /_/ / | | | '_ \ / _ \ '__/ _\ | | | | \ \/ /
     / __  /| |_| | |_) |  __/ | / /   | | |_| |>  < 
     \/ /_/  \__, | .__/ \___|_| \/    |_|\__,_/_/\_\
             |___/|_|                                

            ╔════════════════════════╗
            ║        [method]        ║          
            ║   Type to see command  ║
            ╚════════════════════════╝            
                     
""")


def main():
    while True:
        logo()
        select = input(f"""{Fore.BLUE}
╔═══[root@ZOIC]~$
╚══> """)
                                        
        if select == "method" or select.lower() == "h":
            method_main()

        elif select == "layer7" or select.lower() == "l7":
            layer7()

        elif select == "layer4" or select.lower() == "l4":
            layer4()

        elif select == "Tools" or select.lower() == "t":
            Tools_main()

if __name__ == "__main__":
    check_main()
    main()
