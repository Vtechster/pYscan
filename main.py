import socket
import time
import pyfiglet
from colorama import Fore
from colorama import init

init()

ascii_banner = pyfiglet.figlet_format("IP Scanner")
print(ascii_banner, end="")
print(Fore.MAGENTA + "Author:Vtechster\n")

socket.setdefaulttimeout(2)
portList = [21, 22, 23, 25, 53, 80, 110, 135, 137, 138, 139, 143, 443, 465, 587, 989, 990, 993, 995, 3306, 8080, 8443]
mList = {"2": 1024, "3": 65536}


def get_banner(ip, port):
    try:
        s = socket.socket()
        s.connect((ip, port))
        resp = s.recv(4096)
        return resp
    except Exception as x:
        return x


def scan_ip(ip, m):
    if m == 1:
        for i in portList:
            try:
                if is_open(ip, i):
                    print(Fore.GREEN + "IP:{}".format(ip), "PORT:{}".format(i), 'is open.', end=" ")
                    print("Banner:", get_banner(ip, i), "({})".format(socket.getservbyport(i, 'tcp')))
                else:
                    print(Fore.RED + "IP:{}".format(ip), "PORT:{}".format(i), "is closed.")
            except:
                continue
    else:
        if m == 4:
            start = int(input(Fore.MAGENTA + "Enter starting port range: " + Fore.WHITE))
            end = int(input(Fore.MAGENTA + "Enter ending port range: " + Fore.WHITE)) + 1
            print()
        else:
            start = 1
            end = mList[str(m)]
        for i in range(start, end):
            try:
                if is_open(ip, i):
                    print(Fore.GREEN + "IP:{}".format(ip), "PORT:{}".format(i), "is open.", end=" ")
                    print("Banner:", get_banner(ip, i), "({})".format(socket.getservbyport(i, 'tcp')))
                else:
                    print(Fore.RED + "IP:{}".format(ip), "PORT:{}".format(i), "is closed.")
            except:
                continue


def is_open(ip, port):
    s = socket.socket()
    if s.connect_ex((ip, port)) == 0:
        return True
    else:
        return False


def main():
    ip_addr = input("Enter Target IP: " + Fore.WHITE)
    print()
    print(
        Fore.MAGENTA + "Which ports to scan?\n\n1. Common Ports\n2. Reserved Ports(1-1023)\n3. All Ports(1-65535)\n4. Custom Range\n")
    m = int(input("Enter Option: " + Fore.WHITE))
    print()
    scan_ip(ip_addr, m)


if __name__ == "__main__":
    main()
    print(Fore.GREEN + "\nSCAN COMPLETED.\n")
    input(Fore.MAGENTA + "Press Enter to continue...")
