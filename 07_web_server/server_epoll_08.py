import socket
import re
import select

def service_client(new_socket, request):
	"""return data to client"""

	# recieve request
	# request = new_socket.recv(1024).decode('utf-8')
	request_lines = request.splitlines()
	print("-"*40)
	print(request_lines)

	# locate target html file
	ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
	if ret:
		dir_html = ret.group(1)
		print(dir_html)
		if dir_html == "/":
			dir_html = "/html/baidu.html"
		#if dir_html == " "
	# read html file
	try:
		f = open("." + dir_html, "r")
		
	except:
		data_body = "404 not found"
		data_header = "HTTP/1.1 404 NOT FOUND\r\n"
		data_header += "Content-Length:%d\r\n" % len(data_body)
		data_header += "\r\n"
		

	else:
		data_body= f.read()
		data_header = "HTTP/1.1 200 OK\r\n"
		data_header += "Content-Length:%d\r\n" % len(data_body)
		data_header += "\r\n"		
		f.close()
	
	

	# send data(header and body) to browser
	
	data = data_header + data_body
	new_socket.send(data.encode('utf-8'))

def main():
	"""general control"""
	# create socket
	socket_main = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket_main.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	socket_main.setblocking(False)

	# binding
	local_info = ("", 8080)
	socket_main.bind(local_info)

	# listen
	socket_main.listen(128)

	# create an epoll object
	epl = select.epoll()
	epl.register(socket_main.fileno(), select.EPOLLIN)

	fd_event_dict = dict()
	while True:
		fd_event_list = epl.poll()	# block here untill event happen
		# [(fd, event)]
		for fd, event in fd_event_list:
			if fd == socket_main.fileno():
				new_socket, addr_client = socket_main.accept()
				epl.register(new_socket.fileno(), select.EPOLLIN)
				fd_event_dict[new_socket.fileno()] = new_socket

			elif event == select.EPOLLIN:
				recv_data = fd_event_dict[fd].recv(1024).decode('utf-8')
			
				if recv_data:
					service_client(fd_event_dict[fd], recv_data)
				else:
					fd_event_dict[fd].close()
					epl.unregister(fd)
					del fd_event_dict[fd]

	socket_main.close()

if __name__ == "__main__":
	main()
