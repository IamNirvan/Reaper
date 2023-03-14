import socket

SERVER_IP = "192.168.1.176"
PORT = "4678"

# Create the socket using "with" to automatically close the socket
with (socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
    # Bind the IP address to the port
    sock.bind(SERVER_IP, PORT)
    sock.listen(1)
    
    # When a connection is accepted, an instance representing 
    # the client and server's connection and the address of the client
    connection, client_ip = sock.accept()

    with connection:
        while True:
            # Data can only be sent as binary. Prefix it with 'b'
            connection.send(b"Hehehe...")
            break

        