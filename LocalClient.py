import socket

Server_ip = '172.24.249.179'
port = 9999

client = socket.socket()

client.connect((Server_ip, port))
print('-----Server Connect-----')

client.send(b'Hi I am Client')
print('-----Message Send-----')

msg = client.recv(1024)
print('-----Message Receive-----')
print(msg)

client.close()