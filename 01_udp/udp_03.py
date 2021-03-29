import socket

def main():
	# create a socket
	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	# bind local information
	local_addr = ('', 6666)
	udp_socket.bind(local_addr)
	
	# recieve data
	recv_data, src_info = udp_socket.recvfrom(1024)

	# print data
	print(f"{str(src_info)}:{recv_data.decode('utf-8')}")
	# close socket
	udp_socket.close()


if __name__ == "__main__":
	main()
