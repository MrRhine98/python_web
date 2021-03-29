import socket
import re
import time
import multiprocessing
import sys

class WSGIServer(object):
    def __init__(self, port, app, static_path):
        # create socket
        self.application = app
        self.static_path = static_path
        self.port = port
        self.headers = ""
        self.status = ""
        self.socket_main = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_main.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # binding
        local_info = ("", port)
        self.socket_main.bind(local_info)

        # listen
        self.socket_main.listen(128)


    def service_client(self, new_socket):
        """return data to client"""

        # recieve request
        request = new_socket.recv(1024).decode('utf-8')
        request_lines = request.splitlines()
        print("-"*40)
        print(request_lines)

        # locate target html file
        ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
        if ret:
            dir_html = ret.group(1)
            print(dir_html)
            if dir_html == "/":
                print("inininininin")
                print(self.static_path)
                dir_html = "/baidu.html"
                #if dir_html == " "      
        
        # read html file
        # if dir does not end with .py, then it can be considered static file
        if not dir_html.endswith(".py"):
            try:
                print("----->Opening file<--------")
                print(self.static_path + dir_html)
                f = open(self.static_path + dir_html, "r")

            except:
                print("------>not found<----------")
                data_header = "HTTP/1.1 404 NOT FOUND\r\n"
                data_header += "\r\n"
                data_body = "404 not found"

            else:
                print("------->resembling<--------")
                data_body= f.read()
                data_header = "HTTP/1.1 200 OK\r\n"
                data_header += "\r\n"		
                f.close()

        else:
            # if dir ends with .py, then it can be seen as dynamic file

            env = dict()
            env['PATH_INFO'] = dir_html
            data_body = self.application(env, self.set_response_header)
            data_header = f"HTTP/1.1 {self.status}\r\n"
            for temp in self.headers:
            	data_header += f"{temp[0]}:{temp[1]}\r\n"
            data_header += "\r\n"
        # send data(header and body) to browser

        data = data_header + data_body
        print("-----> data compelete")
        new_socket.send(data.encode('utf-8'))
        print("-----> data sent")

        # close
        new_socket.close()
        print("-----> socket closed")

    def set_response_header(self, status, headers):
    	self.status = status
    	self.headers = headers
    	


    def run(self):
        while True:
            # wait for connection
            socket_client, addr_client = self.socket_main.accept()

            p = multiprocessing.Process(target=self.service_client, args=(socket_client,))

            # work
            p.start()
            socket_client.close()

        self.socket_main.close()

def main():
    if len(sys.argv) == 3:
    	try:
    		port = int(sys.argv[1])
    		frame_app_name = sys.argv[2]
    	except Exception as ret:
    		print("Invalid input!")
    		return
    else:
    	print("1")
    	print("please run the file in the form of:")
    	print("python3 xxx.py (port) (frame:app)")

    ret = re.match(r"([^:]+):(.*)", frame_app_name)
    print(frame_app_name)
    if ret:
    	frame_name = ret.group(1)
    	app_name = ret.group(2)
    else:
    	print("2")
    	print("please run the file in the form of:")
    	print("python3 xxx.py (port) (frame:app)")
    	return


    with open("./web_server.conf") as f:
    	conf_info = eval(f.read())
    	# conf_info is a dict
    sys.path.append(conf_info['dynamic_path'])  
    frame = __import__(frame_name)  # frame point to the package
    app = getattr(frame, app_name)  # app point to the function

    server = WSGIServer(port, app, conf_info['static_path'])
    server.run()


if __name__ == "__main__":
	main()
