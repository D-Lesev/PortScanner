import socket
from IPy import IP



def check_ip(ip):
    """
    Check if the argument is IP or a website.
    If it is IP it will simply return the IP otherwise it will convert the address to IP and return it

        - IP() is a third party library which check if the argument we enter to our function is IP or website
        - socket.gethostbyname() - return IP address from a website

    :param ip: IP or website
    :return: always return IP address
    """

    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)


def get_banner(sock_obj):
    """
    Receiving what service is running on the specific port.
    :param sock_obj: socket object that we created
    :return: return the service from the specific port. 1024 bytes are enough to receive the message from the server.
            Also, the received msg is encoded in bytes. We need to decoded here, before sending it back.
    """

    return sock_obj.recv(1024).decode()


def scan_port(ip_addr, port):
    """
    Creating socket with the given IP address and port.
    Setting the timeout to 0.3 sec in order to jump to another port. This is done because it can take
    a lot of time or get stuck on one port and not moving further. Also setting the seconds to low could jump some ports
    and not receiving response from them.
    Then we get the service running from the port.
    We encapsulated all function in try/except block.
    The ports which are closed we pass them.

    :param ip_addr: IP address received from the function
    :param port: Port received from the function
    :return: return msg if the port is open/closed and the service running
    """

    try:
        sock = socket.socket()
        sock.settimeout(0.3)
        sock.connect((ip_addr, port))

        try:
            banner = get_banner(sock)
            print(f"[+] Port {port} is open : {banner.strip()}")
        except:
            print(f"[+] Port {port} is open")
    except:
        pass


def scan(target, ports):
    """
    Receiving ip address or website and list with ports.
    It will check if it is IP or website and send to scan_port() for further action.
    If will check if the list has one or multiple ports.
    Depend on the above check, it will decide if the user wants to scan one ot multiples ports.
    :param target: IP address/website
    :param ports: list with port/s
    """

    print(f"\n[-- Scanning target] {target}")

    new_ip = check_ip(target)

    if len(ports) == 1:
        scan_port(new_ip, ports[0])
    else:
        for port in range(ports[0], ports[1] + 1):
            scan_port(new_ip, port)


def run(targets, ports_to_scan):
    """
    Check if targets are more than one or multiple.
    Depend on that it will send the target or targets in for loop along with the list of ports from the user
    After that it will scan all targets with the ports from the user
    :param targets: list with IP address or websites
    :param ports_to_scan: list with ports
    """

    if len(targets) > 1:
        for target in targets:
            strip_target = target.strip()
            scan(strip_target, ports_to_scan)
    else:
        strip_target = targets[0].strip()
        scan(strip_target, ports_to_scan)

