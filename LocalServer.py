import socket
import os

server = socket.socket()
server.bind(('172.24.249.179', 9999))
server.listen(1)

path_dir = "C:\Users\jump0\OneDrive\바탕 화면\Network_Project"
file_list = os.listdir(path_dir)
print(file_list)

# b_key = bytes(key, 'utf-8')

# print('-----Server Ready-----')

# client, address = server.accept()
# print('-----Client Connect-----')

# msg = client.recv(1024)
# print('-----Message Recieve-----')
# print(msg)

# client.sendall(b_key)
# print('-----Message Send-----')

# client.close()
# server.close()