
from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('localhost',serverPort))
serverSocket.listen(1)

print ("The server is ready to receive")

while True:
	connectionSocket, address = serverSocket.accept()
	sentence = connectionSocket.recv(1024).decode()
	capSentence = sentence.upper()
	connectionSocket.send(capSentence.encode())
	connectionSocket.close()
