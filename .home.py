import time
import os
import socket
import psutil
import sys

battery = psutil.sensors_battery()
login_passwd  = open(".password")
login_uname  = open(".username")
l_p = login_passwd.read()
l_u = login_uname.read()
print(""""

███████╗░█████╗░███╗░░░███╗░█████╗░██████╗░░█████╗░██╗░░██╗░█████╗░███╗░░░███╗  ░█████╗░░██████╗
╚════██║██╔══██╗████╗░████║██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔══██╗████╗░████║  ██╔══██╗██╔════╝
░░███╔═╝███████║██╔████╔██║███████║██████╔╝███████║█████═╝░███████║██╔████╔██║  ██║░░██║╚█████╗░
██╔══╝░░██╔══██║██║╚██╔╝██║██╔══██║██╔══██╗██╔══██║██╔═██╗░██╔══██║██║╚██╔╝██║  ██║░░██║░╚═══██╗
███████╗██║░░██║██║░╚═╝░██║██║░░██║██║░░██║██║░░██║██║░╚██╗██║░░██║██║░╚═╝░██║  ╚█████╔╝██████╔╝
╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝  ░╚════╝░╚═════╝░
""")

print("Zamarakam Version is v1.2")
print("Welcome " + l_u)
print("")
print("The Date is: " + time.strftime("%y/%m/%d"))
print("")
print("Battery Left: ", battery.percent)
print("""
[1] Open Google
[2] Open Text Editor
[3] Open File Explorer
[4] Open BIOS
[5] Open Terminal
[6] Open SuperTerminal
[7] Shutdown Zamarakam
""")
select = input("[?]: ")

if select == '1':
    exec(open(".browse.py").read())
if select == '2':
    exec(open(".editor.py").read())
if select == '3':
    exec(open(".explorer.py").read())
if select == '4':
    while True:
        b_login = input(str("Enter Password for " + l_u + " to open BIOS: "))
        if b_login == l_p:
            print("BIOS is opening")
            host_name = socket.gethostname()
            host_ip = socket.gethostbyname(host_name)
            print("[1] USERNAME: " + l_u)
            print("[2] PASSWORD: " + l_p)
            print("HOST NAME: " + host_name)
            print("LOCAL IPS: " + host_ip)
            edit_b = input("Enter [?] to change setting: ")
            if edit_b == '1':
                edit_u = input("New Username: ")
                with open('.username', 'w') as f:
                    f.writelines(edit_u)
                print("Username is changed to " + edit_u)
                input("Enter to close window: ")
            if edit_b == '2':
                edit_p = input("New Password: ")
                with open('.password', 'w') as f:
                    f.writelines(edit_p)
                print("Password is changed to " + edit_p)
                input("Enter to close window: ")

        else:
            print("Wrong Password for: " + l_u)
if select == '5':
    exec(open(".Terminal.py").read())
if select == '6':
    input(str("Enter Password for " + l_u + " to open SuperTerminal: "))
    exec(open(".superterminal.py").read())
if select == '7':
    sys.exit(input("Press enter to close Zamarakam: "))