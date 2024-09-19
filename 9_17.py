import socket
mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))#域名和端口号

request = 'GET /page1.txt HTTP/1.0\r\nHost: data.pr4e.org\r\n\r\n'
mysock.send(request.encode())
response = mysock.recv(4096)
print(response.decode())
mysock.close()