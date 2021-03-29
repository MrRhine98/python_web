import socket
from collections import defaultdict

def download_mod(socket_client):
	data_send = '\nCurrent mod: download\n what would you like to download?\n(enter exit to quit)'.encode('utf-8')
	socket_client.send(data_send)
	while True:
		data_recv = socket_client.recv(1024).decode('utf-8')
		if data_recv in ['Chat', 'Exit']:
			return data_recv
		data_send = 'Received!'

def default_mod(socket_client):
	# send the help string
	data_send = '\nCurrent mod: chat\n Enter message:\n(enter exit to quit)'.encode('utf-8')
	socket_client.send(data_send)
	while  True:
		# wait here for message
		data_recv = socket_client.recv(1024).decode('utf-8')
		if data_recv in ['Download', 'Exit']:
			return data_recv
		data_send = 'Received!'.encode('utf-8')
		socket_client.send(data_send)

def main():
	# setup socket
	socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	local_addr = ('', 6666)
	socket_tcp.bind(local_addr)
	socket_tcp.listen(128)
	socket_client, addr_client = socket_tcp.accept()

	state = 'default'
	mod_dict = defaultdict(lambda : default_mod(socket_client))
	mod_dict['Download'] = lambda : download_mod(socket_client)
	while state != 'Exit':
		# receive data
		print(state)
		state = mod_dict[state]

	socket_client.close() 
	socket_tcp.close()


	



if __name__ == "__main__":
	main()