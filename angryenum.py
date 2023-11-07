import argparse
import socket
import re
import subprocess
import time
import os
from colorama import Fore
from ftplib import FTP
from pynput.keyboard import Key, Controller

def analyze_vuln(open_port, target):
    if 21 in open_port:
        ftp = FTP(target)
        response = ftp.login('anonymous', 'anonymous')
        
        if "230" in response:  
            print("Anonymous connection available! (ftp)")
        else:
            print("No anonymous connection available (ftp)")

    if 445 in open_port:
        print(f"{Fore.BLUE}[{Fore.WHITE}*{Fore.BLUE}]{Fore.WHITE} Sharing available as anonymous: (smb)")
        os.system(f"smbclient -L //{target} -N")
        
        keyboard = Controller()
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)


    if 80 in open_port:
        print(f"{Fore.BLUE}[{Fore.WHITE}*{Fore.BLUE}]{Fore.WHITE} We detected port 80. What wordlist do you want to use to brute force the directories ?")
        path_directory = input("Your choice -> ")

        if os.path.exists(path_directory):
                subprocess.run(f"gobuster dir --url http://{target}:80/ -w {path_directory} -x db,php,txt,bak -o gobuster_output.txt", shell=True, check=True)
                print(f"{Fore.GREEN}[{Fore.WHITE}*{Fore.GREEN}]{Fore.WHITE} Result in gobuster_output.txt")
  
parser = argparse.ArgumentParser(description="collection of information")
parser.add_argument("-i", "--ip-target", dest="target", help="IP Target", required=True)
args = parser.parse_args()

target = args.target

ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")

if ip_add_pattern.search(target):
    open_port = []
    
    for port in [21, 445, 80]:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        time.sleep(0.5)
        try:
            result = s.connect((target, port))
            print(f"{Fore.GREEN}[{Fore.WHITE}*{Fore.GREEN}]{Fore.WHITE}port {port} is open")
            open_port.append(port)

        except ConnectionRefusedError:
            pass

analyze_vuln(open_port, target)
