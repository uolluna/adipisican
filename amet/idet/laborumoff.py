import socket

host = 'example.com'
port = 80

# Translate the host/port argument into a sequence of 5-tuples
# that contain all the necessary arguments for creating a socket
# connected to that service.
addrinfo = socket.getaddrinfo(host, port, family=0, type=0, proto=0, flags=0)

# addrinfo is a list of 5-tuples, each containing the necessary
# arguments for creating a socket.
for addr in addrinfo:
    family, socktype, proto, canonname, sockaddr = addr
    try:
        # Create a socket object
        s = socket.socket(family, socktype, proto)
        # Connect to the service
        s.connect(sockaddr)
        # Do something with the socket
        # ...
        break
    except socket.error as e:
        print(f"Error: {e}")
