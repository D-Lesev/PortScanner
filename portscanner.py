import socket
from IPy import IP


ip_address = input("[+] Enter IP to scan: ")
port = 80

try:
    sock = socket.socket()
    sock.connect((ip_address, port))
    print("[+] Port 80 is open")
except:
    print("[-] Port 80 is closed")
