import socket
''' This is a tcp client machine'''
def main():
	# create socket
	socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# dest info
	server_ip = input("IP:")
	while True:
		try:
			server_port = int(input("Port:"))
			break
		except:
			print("Invalid port! Please re-enter\n")


	server_addr = (server_ip, server_port)
	# connect to sever
	socket_tcp.connect(server_addr)

	# send and receive
	file_name = input("\nEnter the file name to download:")
	socket_tcp.send(file_name.encode("utf-8"))

	recv_data = socket_tcp.recv(1024)
	if recv_data:
		with open(file_name, 'wb') as f:
			f.write(recv_data)

	# close socket
	socket_tcp.close()

if __name__ == "__main__":
	main()