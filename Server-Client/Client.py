import socket

host = 'localhost'
port = 8000

message = "Krooz is Wilding"

def SendData():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(message.encode())
    s.close()

SendData()
