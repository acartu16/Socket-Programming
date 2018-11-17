name = dict()
clients1 = dict()

class clients():
    def __init__(self):
        self.list_sockets = list()
        self.list_addr = list()

    def add_client(self,socket,addr):
        self.list_sockets.append(socket)
        self.list_addr.append(addr)

    def print_clients(self):
        print(self.list_sockets)