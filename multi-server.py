import socket
import threading


port = int(input("Enter port to start server: "))
print(f'''

 <!> BASIC INSTRUCTIONS

-> The server is running with port {port}

-> Use the system ip address to get connected to the server

-> To find the ip address open command prompt and type "ipconfig"

-> Client : Enter ip address of the server with port - {port}

-> Remote : Enter ip and port - {port} in apk


''')

clients = []

def broadcast_message(message, sender_socket=None):
    # Broadcast the message to all connected clients
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                client.close()
                clients.remove(client)

def handle_client(client_socket, address):
    clients.append(client_socket)

    while True:
        try:
            # Receive message from client
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break

            # Broadcast message to all other clients
            broadcast_message(message, client_socket)

        except Exception as e:
            break

    clients.remove(client_socket)
    client_socket.close()

def start_server(host='0.0.0.0'):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    
    while True:
        client_socket, address = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, address))
        client_handler.start()

if __name__ == "__main__":
    start_server()
    broadcasr_message()
