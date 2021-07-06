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
        os.system("python3.8 .superterminal.py")
        print("restarting...")
        exit()
    if sucode == 'md':
        os.mkdir(input("Enter Name to create folder: "))
        print("Folder Created ")
    if sucode == 'rd':
        if os.path.exists(input("Enter Name to delete folder: ")):
            os.rmdir(input("Enter Name of folder to confirm: "))
            print("Folder deleted")
        else:
            print("The folder does not exist")
    if sucode == 'clear':
        os.system('clear')
    if sucode == 'wclear':
        os.system('cls')
    if sucode == 'exit':
        exec(open(".home.py").read())
    if sucode == 'touch':
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(THIS_FOLDER, input("Please enter filename: "))
        file = open(input("Enter filename to edit it: "), "w") 
        file.write(input("What do you want to write to file: ")) 
        file.close() 
    if sucode == 'rf':
        if os.path.exists(input("Enter file name to delete it: ")):
            os.remove(input("Enter File name to confirm: "))
        else:
            print("The file does not exist")

    if sucode == '':
        pass