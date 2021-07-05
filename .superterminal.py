import subprocess
import platform
import socket
import time
import os
import sys
import requests
import wget
import urllib

path = '/'
login_uname  = open(".username")
l_u = login_uname.read()
print("""Welcome to Zamarakam SuperTerminal [V 1.0] 
type 'help' (without quotients) for lists of commands and their usage""")

while True:
    sucode = input(l_u + ' # ')
    if sucode == 'zget':
        url = input("URL: ")
        filename = wget.download(url, os.path.expanduser('~/Downloads'))
        print("")
        
        
    if sucode == 'help':
        print("""
        zget: downloads files. (Stored in the Downloads folder)
        md: creates a folder. (Don't Make a folder the same name also add the name after entering the command)
        dr: removes a folder. (Add the name after entering the command)
        rsd: restarts the super terminal
        clear: clears the screen
        exit: goes back to home.
                """)
    if sucode == 'rsd':
        os.system("python3.8 superterminal.py")
        print("restarting...")
        exit()
    if sucode == 'md':
        os.mkdir(input("Enter Name to create folder: "))
        print("Folder Created ")
    if sucode == 'dr':
        os.rmdir(input("Enter Name to delete folder: "))
        print("Folder deleted")
    if sucode == 'clear':
        os.system('clear')
    if sucode == 'wclear':
        os.system('cls')
    if sucode == 'exit':
        exec(open(".home.py").read())