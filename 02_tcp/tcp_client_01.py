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
			print("Invalid port! Please re-enter")


	server_addr = (server_ip, server_port)
	# connect to sever
	socket_tcp.connect(server_addr)

	# send and receive
	send_data = input("Enter message:")
	socket_tcp.send(send_data.encode("utf-8"))

	# close socket
	socket_tcp.close()

if __name__ == "__main__":
	main()