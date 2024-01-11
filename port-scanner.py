#!/usr/bin/python3
import socket

def port_scan(target_host_ip, port):
    sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    sock.settimeout(5)

    try:
        sock.connect((target_host_ip , port))
        print(f'[+] Port {port} is open for connection')
    except socket.error:
        pass
    finally:
        sock.close()


if __name__ == "__main__":
    target_host_ip = input('Enter the IP of host: ')
    initial_port = int(input('Enter intial port number: '))
    ending_port = int(input('Enter ending port number: '))

    print(f'Scanning {target_host_ip} to look for open ports . . .')

    for port in range(initial_port , ending_port + 1):
        port_scan(target_host_ip , port)
