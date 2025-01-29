import os
from colorama import Fore, init
init(autoreset=True)

def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.LIGHTGREEN_EX,"""
                    
                  ╔╦╗┌─┐┌─┐┬  ┌─┐
                   ║ │ ││ ││  └─┐
                   ╩ └─┘└─┘┴─┘└─┘
     
            ╔════════════════════════╗
            ║        [!help]         ║          https://rvlt.gg/PnjMbQwH 
            ║   Type to see command  ║
            ╚════════════════════════╝            
                     
""")
    
def Tools_main():
    while True:
        logo()
        select = input(Fore.BLUE,"""
╔═══[root@ZOIC]~$
╚══> """)
                                        
        if select == "!help" or select.lower() == "h":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.LIGHTGREEN_EX,"""
                                      
                            ┬┬ ┬┌─┐┬  ┌─┐
                            │├─┤├┤ │  ├─┘
                            o┴ ┴└─┘┴─┘┴  
                                                                                    
                ╔═════════════════════════════════╗
                ║                                 ║
                ║  - port  |  PortScanner         ║
                ║                                 ║
                ║  - PLS PROJECT STAR             ║
                ║  - GOD BLESS YOU                ║
                ║                                 ║  
                ╚═════════════════════════════════╝

""")
            input("")


        elif select == "port" or select.lower() == "p":

            ip_address = input(Fore.BLUE,"""
╔═══[root@IP]~$
╚══> """)
            
            os.system(f"nmap {ip_address}")

            input(Fore.LIGHTGREEN_EX,"[ZOIC] Enter the continue...")
            
if __name__ == "__main__":
    Tools_main()
