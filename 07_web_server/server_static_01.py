import socket

def service_client(new_socket):
	"""return data to client"""

	# recieve request
	request = new_socket.recv(1024)
	print(request)

	# send data(header and body) to browser
	data_header = "HTTP/1.1 200 OK\r\n"
	data_header += "\r\n"
	data_body = "<h1>hahahahaha</h1>"
	data = data_header + data_body

	new_socket.send(data.encode('utf-8'))

	# close
	new_socket.close()

def main():
	"""general control"""
	# create socket
	socket_main = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket_main.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	# binding
	local_info = ("", 8080)
	socket_main.bind(local_info)

	# listen
	socket_main.listen(128)

	while True:
		# wait for connection
		socket_client, addr_client = socket_main.accept()

		# work
		service_client(socket_client)

	socket_main.close()

if __name__ == "__main__":
	main()
