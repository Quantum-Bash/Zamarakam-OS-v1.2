import subprocess
import platform
import socket
import time
import os
import sys
import requests

path = '/'
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
login_uname  = open(".username")
l_u = login_uname.read()
print("""Welcome to Zamarakam Terminal [V 2.0]
type 'help' (without quotients) for lists of commands and their usage""")

while True:
    code = input(l_u + ' $ ')
    if code == 'ping':
        host = input("Enter Website to ping: ")
        number = input('Enter Times to ping: ')
        def ping(host):
            param = '-n' if platform.system().lower() == 'windows' else '-c'
            command = ['ping', param, number, host]
            return subprocess.call(command)
        print(ping(host))
    if code == 'info':
        print("local IPS: " + host_ip)
        print("Host name: " + host_name)
        print("User name: " + l_u)
    if code == 'date':
        print("The date is: " + time.strftime("%y/%m/%d"))
    if code == 'ls':
        dir_list = os.listdir(path)
        print("Files and Directories in '", path, "' :")
        print(dir_list)
    if code == 'ls -c':
        file = input("Enter file path to Read: ")
        dir_list2 = os.listdir(file)
        print("Files and Directories in '", file, "' :")
        print(dir_list2)
    if code == 'exit':
        exec(open(".home.py").read())
    if code == 'shutdown':
        sys.exit("Closing Zamarakam")
    if code == 'echo':
        echo = input("what do you want to echo: ")
        print(echo)
    if code == 'restart':
        os.system("python3.8 Zamarakam.py")
        print("restarting...")
        exit()    
    if code == 'rsd':
        os.system("python3.8 Terminal.py")
        print("restarting...")
        exit()  
    if code == 'clear':
        os.system('clear')
    if code == 'wclear':
        os.system("cls")
    if code == 'help':
        print("""
                 shutdown: Closes Zamarakam.
                 -h: displays help.
                 echo: echoes the word written after asked. 
                 exit: goes back to home
                 info: displays host name, username and local ISP.
                 ls: list files in / (if you are using windows change path = '/' to path = 'C:/')
                 ls -c: lists files in a specified directory. (Write file when prompted)
                 ping: pings a website. (Write website and amount of times to ping when prompted)
                 read: reads files. 
                 restart: restarts zamarakam.
                 rsd: restarts terminal (for me).
                 clear: clears the screen. (linux)
                 wclear: clears the screen. (windows)
            """)
    if code == '':
        pass
    if code == 'read':
        f = open(input("Enter filename to read: "))
        print(f.read())
