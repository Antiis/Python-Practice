#Sockets
import socket
# like dialing a phone (not doing any sending or recieving)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect( ('data.pr4e.org', 80))
cmd='GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
sock.send(cmd)

while True:
    data = sock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
sock.close()
