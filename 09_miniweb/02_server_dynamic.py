import socket
import re
import time
import multiprocessing
import mini_frame

class WSGIServer(object):
    def __init__(self):
        # create socket
        self.socket_main = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_main.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # binding
        local_info = ("", 8080)
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
                dir_html = "/html/baidu.html"
                #if dir_html == " "      
        
        # read html file
        # if dir does not end with .py, then it can be considered static file
        if not dir_html.endswith(".py"):
            try:
                f = open("." + dir_html, "r")

            except:
                data_header = "HTTP/1.1 404 NOT FOUND\r\n"
                data_header += "\r\n"
                data_body = "404 not found"

            else:
                data_body= f.read()
                data_header = "HTTP/1.1 200 OK\r\n"
                data_header += "\r\n"		
                f.close()

        else:
            # if dir ends with .py, then it can be seen as dynamic file
            data_header = "HTTP/1.1 200 OK\r\n"
            data_header += "\r\n"
            data_body = mini_frame.application(dir_html)

        # send data(header and body) to browser

        data = data_header + data_body
        new_socket.send(data.encode('utf-8'))

        # close
        new_socket.close()

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
    server = WSGIServer()
    server.run()


if __name__ == "__main__":
	main()
