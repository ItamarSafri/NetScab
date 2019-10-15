import socket
import os
import sys
from datetime import datetime
import time
import multiprocessing



ip_addr = []
live_hosts = []
final = {}

print('-'*60)
start = input('Type in the fist address: ')
end = input('Type in the last address: ')
print('-'*60)



def iplist(start_ip, end_ip):

    start = list(map(int, start_ip.split(".")))
    end = list(map(int, end_ip.split(".")))
    temp = start
    if start[0] > end [0]:
        sys.exit("End IP can't be greater than start IP")
    ip_addr.append(start_ip)
    while temp != end:
        start[3] += 1

        for i in [3,2,1]:
            if temp[i] >= 256:
                break
        ip_addr.append('.'.join(map(str, temp)))


def testip():
    print('-'*60)
    print('Scanning')
    print('-'*60)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    global live_hosts
    t1 = datetime.now()

    for ip in ip_addr:
        try:
            socket.gethostbyaddr(ip)
            print('[+] ', ip, 'UP   | ',socket.gethostbyaddr(ip)[0])
            live_hosts.append(ip)
        except socket.herror:
            continue

    t2 = datetime.now()
    
    t1 = t1.replace(microsecond=0)
    t2 = t2.replace(microsecond=0)

    total = t2-t1
    print('-'*60)
    print('Scan completed')
    print('Found ', len(live_hosts), ' Live hosts in {}'.format(total))
    print('-'*60)
    
    s.close

def portscanner():
    global live_hosts
    global final
    open_ports = []
    
    p = input('Type in the port range: ')
    p = p.split('-')
    p = list(map(int, p))

    print('-'*60)
    print('Scanning for open ports')
    print('-'*60)

    time.sleep(2)
    
    for ip in live_hosts:
        print('Host: ', socket.gethostbyaddr(ip)[0])
        print('Addr: ', ip)
        for port in range(p[0],p[1]):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((ip, port))
            if result == 0:
                print('[+] Port {}:    Open'.format(port))
                open_ports.append(port)
        final = {ip : open_ports}
        print('-'*60)

    print(final)

    s.close


def main():
    iplist(start, end)
    testip()
    scan = input('Scan for open ports? y/n ')

    if scan == 'y' or scan == 'Y':
        portscanner()
    else:
        sys.exit('Thank you for using the scanner')
    sys.exit('Thank you for using the scanner')

    
if __name__ == "__main__":
    main()
