# Project-1,TCP Socket
#Tugay ACAR / 150160511
from socket import *
import threading
from Clients import *
import time

#Send messages to all of other clients
def broadcast(msg, clients, conn):
    for i in clients.list_sockets:
        if conn != i:
            i.send(msg.encode())

class Server():
    def listen_Client(self, connectionSocket, addr, cc):
        #first i keep a nickname to understand who send message
        nickname = connectionSocket.recv(1024)
        name[connectionSocket] = nickname.decode('utf-8')
        #send a welcome message to only itself
        welcome_message = nickname.decode('utf-8') + ', Welcome to chat room '
        connectionSocket.send(welcome_message.encode())
        #send joining message to all of other clients
        message = nickname.decode('utf-8') + ', joined chat room '
        broadcast(message,cc,connectionSocket)
        while True:
            #server takes an input
            data = connectionSocket.recv(1024)
            # if data(message) != exit, it sends the data to all of other clients
            if data != bytes("exit", "utf8"):
                # we have just one client, the client is alone in server. So i send this message always to the client
                if (len(cc.list_sockets) == 1):
                    msg = 'You are alone in server'.encode()
                    connectionSocket.send(msg)
                #if we have more clients than 1, sen messages to other clients
                data = name[connectionSocket]+': '+data.decode('utf-8')
                broadcast(data, cc,connectionSocket)
            else:
                #if message exit. Client exit
                connectionSocket.send(bytes("exited", "utf8"))
                connectionSocket.close()
                cc.list_sockets.remove(connectionSocket)


    def __init__(self, Port):
        # exceptions for creaitng of socket
        try:
            serverSocket = socket(AF_INET, SOCK_STREAM)
        except:
            exit(1)

        try:
            serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        except:
            exit(1)

        try:
            serverSocket.bind(('', Port))
        except:
            exit(1)

        try:
            serverSocket.listen(45)
        except:
            exit(1)

        print("The server is ready")

        #to keep the clients who connected to server
        client = clients()
        while True:
            #threading a new thread for every client who is joined
            connectionSocket, addr = serverSocket.accept()
            #add clients to our list
            client.add_client(connectionSocket,addr)
            threading.Thread(target=self.listen_Client, args=(connectionSocket, addr, client)).start()
            time.sleep(1)
if __name__ == "__main__":
    Port = 11111
    Server(Port)
