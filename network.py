import socket
from concurrent import futures
from tkinter import *
from socket import *
import time
import os
import platform
from datetime import datetime
import tkinter as tk
from alive_progress import alive_bar
import time

from tkinter import messagebox






def pingsweep():
    net = input("Enter the Network Address: ")
    net1 = net.split('.')
    a = '.'

    net2 = net1[0] + a + net1[1] + a + net1[2] + a
    st1 = int(input("Enter the Starting Number: "))
    en1 = int(input("Enter the Last Number: "))
    en1 = en1 + 1
    oper = platform.system()

    if (oper == "Windows"):
        ping1 = "ping -n 1 "
    elif (oper == "Linux"):
        ping1 = "ping -c 1 "
    else:
        ping1 = "ping -c 1 "
    t1 = datetime.now()
    print("Scanning in Progress:")

    for ip in range(st1, en1):
        addr = net2 + str(ip)
        comm = ping1 + addr
        response = os.popen(comm)

        for line in response.readlines():
            if (line.count("TTL")):
                break
            if (line.count("TTL")):
                print(addr, "--> Live")

    t2 = datetime.now()
    total = t2 - t1
    print("Scanning completed in: ", total)
    print("Mission completed")




def networkscanner():
    startTime = time.time()
    if __name__ == '__main__':
        target = input('Enter the host to be scanned: ')
        t_IP = gethostbyname(target)
        print('Starting scan on host: ', t_IP)

        for i in range(50,500):
            s = socket(AF_INET, SOCK_STREAM)

            conn = s.connect_ex((t_IP, i))
            if(conn == 0):
                print('Port %d: OPEN' % (i,))
            s.close()
    print('Time taken:', time.time() - startTime)
    print("Mission completed")



def listeningport():
    def check_port(targetIp, portNumber, timeout):
        TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        TCPsock.settimeout(timeout)
        try:
            TCPsock.connect((targetIp, portNumber))
            return (portNumber)
        except:
            return

    def port_scanner(targetIp, timeout):
        threadPoolSize = 500
        portsToCheck = 10000

        executor = futures.ThreadPoolExecutor(max_workers=threadPoolSize)
        checks = [
            executor.submit(check_port, targetIp, port, timeout)
            for port in range(0, portsToCheck, 1)
        ]

        for response in futures.as_completed(checks):
            if (response.result()):
                print('Listening on port: {}'.format(response.result()))
                print("Mission completed")

    def main():
        targetIp = input("Enter the target IP address: ")
        timeout = int(input("How long before the connection times out: "))
        port_scanner(targetIp, timeout)

    if __name__ == "__main__":
        main()

def loadingpage():
    with alive_bar(1000, force_tty=True) as bar:
        for i in range(1000):
            time.sleep(.005)
            if i and i % 200 == 0:
                print('Loading...')
            bar()

def closeprogram():
    print(os.system('TSKILL netwok'))


def ipfinder():

    window = Tk()

    window.title("Network Tool")
    window.geometry("480x480")


    program = Frame(window)
    program.grid()
    text = Label(program, text="Welcome to our Network Tool. With this program, you can use the following data.")
    text.grid(padx=35, pady=20)

    text = 0

    def PingSweep(a):
        print(a)
        
    def NetworkScanner(arp):
        print(arp)
    def ListeningPorts(brr):
        print(brr)


    button1 = Button(program, text="Ping Sweep", width=30, command=lambda: PingSweep(pingsweep()))
    button1.grid(padx=105, pady=20)

    button2 = Button(program, text="Network Scanner", width=30, command=lambda: NetworkScanner(networkscanner()))
    button2.grid(padx=105, pady=20)
    button3 = Button(program, text="Listening Ports", width=30, command=lambda: ListeningPorts(listeningport()))
    button3.grid(padx=105, pady=20)




    # Lb1 = Listbox(program)
    # Lb1.insert(1, "Ping Sweep")
    # Lb1.insert(2, "Network Scanner")
    # Lb1.insert(3, "Listening Port")
    # Lb1.grid(padx=150, pady=60)

    window.mainloop()


print(loadingpage())
print(ipfinder())






