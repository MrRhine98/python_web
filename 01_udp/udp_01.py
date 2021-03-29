import socket

def main():
		# create a socket
	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

		# send and recieving data
	dest_addr = ("192.168.0.103", 8080)
	udp_socket.sendto(b"hello world", dest_addr)

		# close socket
	udp_socket.close()


if __name__ == "__main__":
	main()
