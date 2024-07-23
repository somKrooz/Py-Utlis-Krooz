import socket
import threading

#init the socket
host = "localhost"
port  = 8000
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def start():
    print(f"Server Starting on {host}:{port}")
    socket.bind((host, port))
    socket.listen(1)

    while True:
        client, address = socket.accept()
        print(f"Connected with {str(address)}")
        threading.Thread(target=handle_client, args=(client,)).start()
    
def handle_client(cli_soc):
    with cli_soc:
        data = b""
        while True:
            message = cli_soc.recv(2048)
            if not message:
                break
            data += message
            print(data.decode('utf-8'))

thread = threading.Thread(target=start)
thread.start()