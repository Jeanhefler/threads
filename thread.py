import threading
import socket
import time

def server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 12345))
    server.listen(1)
    print("thread 1 aguardando conexao...")
    while(True):
        client, client_adrees = server.accept()
        print("conexao estabelecida com thread 2")
        client.close()

def client():
    print("thread 2 aguardando conexao...")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 12345))
    print("conexao estabelecida com thread 1")

tr1 = threading.Thread(target=server)
tr2 = threading.Thread(target=client)

tr1.start()
tr2.start()
