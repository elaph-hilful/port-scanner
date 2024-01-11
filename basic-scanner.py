#!/usr/bin/python3

import socket

target_host_ip = input('Enter IP for scanning ports: ')
target_host_ports = range(1,1200)

for port in target_host_ports:
    
    sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    sock.settimeout(3)

    res = sock.connect_ex((target_host_ip , port))
    if res == 0 :
        print(f'Port number {port} is open for connection')
        sock.close

