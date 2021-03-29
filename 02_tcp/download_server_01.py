import socket


# def get_file(file_name):
	# search for file_name

	# if exists, return data

	# if not, return void string

def main():
	# socket setup
	socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	local_info = ('', 6667)
	socket_tcp.bind(local_info)
	socket_tcp.listen(128)

	socket_client, addr_client = socket_tcp.accept()

	# receive file name and read file
	file_name = socket_client.recv(1024).decode('utf-8')
	# data_file = get_file(file_name)
	data_file = "get_file(file_name)"
	# send file
	socket_client.send(data_file.encode('utf-8'))
	# close socket
	socket_client.close()
	socket_tcp.close()

if __name__ == "__main__":
	main()