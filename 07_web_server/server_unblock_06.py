import socket

client_socket_list = list()

socket_main = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_main.setblocking(False)
# binding
local_info = ("", 8080)
socket_main.bind(local_info)

# listen
socket_main.listen(128)

while True:
	try:
		new_socket, new_addr = socket_main.accept()
	except Exception as ret:
		print("no client")
	else:
		new_socket.setblocking(False)
		client_socket_list.append(new_socket)

	for client_socket in client_socket_list:
		try:
			recv_data = client_socket.recv(1024)
		except:
			print("no data")
		else:
			if recv_data:
				print("data recieved")
			else:
				client_socket_list.remove(client_socket)
				client_socket.close()
