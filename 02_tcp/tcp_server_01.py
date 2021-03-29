import socket
"""This is a server """

def main():
	# create tcp socket 
	socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# local info
	server_port = 6666
	# binding
	socket_tcp.bind(("", server_port))
	socket_tcp.listen(128)
	# wait for connection requisit
	client_socket, client_addr = socket_tcp.accept()

	recv_data = client_socket.recv(1024)
	print(recv_data.decode('utf-8'))

	client_socket.send("Got it".encode('utf-8'))
	client_socket.close()
	socket_tcp.close()
	# 

if __name__ == "__main__":
	main()