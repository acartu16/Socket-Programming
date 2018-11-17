# Project-1,TCP Socket
#Tugay ACAR / 150160511

from socket import *
from threading import Thread
import time
#arrnge Server IP and Port
serverIP="192.168.43.44"
Port=11111
clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverIP,Port))


#firstly i take a nickname to recognize itself
nickname = input("Enter nicknname : ")
clientSocket.send(nickname.encode())
welcome = clientSocket.recv(1024)
print(welcome.decode('utf-8'))

read_flag = 1
write_flag = 1

def receive():
    #to reveive messages from server
    while True:
        try:
            msg = clientSocket.recv(1024)
            print(msg.decode('utf-8'))
        except OSError:  # Possibly client has left the chat.
            break

def send():
    #to send messages to server and then the other clients
    msg = input('')
    timestamp = ' '+str(time.ctime(time.time()))
    msg = msg + timestamp
    clientSocket.send(msg.encode())
    if msg == "{quit}":
        clientSocket.close()
        exit(0)

while True:
    #i wrote an algorithm like that
    if write_flag==1:
        send_thread = Thread(target=send)
        send_thread.start()
        time.sleep(1)
        write_flag=0
        read_flag=1
        continue
    if read_flag==1:
        receive_thread = Thread(target=receive)
        receive_thread.start()
        time.sleep(1)
        read_flag =0
        write_flag = 1
        continue














