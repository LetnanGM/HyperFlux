import os
import sys
from colorama import Fore, init
init(autoreset=True)

def method_main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.LIGHTGREEN_EX, """
                              
                       ┌┬┐┌─┐┌┬┐┬ ┬┌─┐┌┬┐
                       │││├┤  │ ├─┤│ │ ││
                       ┴ ┴└─┘ ┴ ┴ ┴└─┘─┴┘ 
                                                                                    
            ╔═════════════════════════════════════╗
            ║                                     ║
            ║  - layer7  |  show l7 module        ║
            ║  - layer4  |  show l4 module        ║
            ║  - Tools   |  show Tools module     ║
            ║                                     ║
            ╚═════════════════════════════════════╝
 
""")
    
    input("[HyperFlux] Enter the continue...")