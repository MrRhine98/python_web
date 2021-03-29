import time



def login():
	return "Login-------%s" % time.ctime()

def register():
	return "Register-----%s" % time.ctime()

URL_FUNC_DICT = {
	"/login.py": login,
	"/register.py": register
}

def application(environ, start_response):
	start_response("200 OK", [('Content-Type', 'text/html;charset=utf-8')])
	file_name = environ["PATH_INFO"]
	

	return URL_FUNC_DICT[file_name]()

	'''
	if file_name == "/login.py":
		return login()
	elif file_name == "/register.py":
		return register()
	else:
		return 'hello world'
	if name == "/login.py":
		return login()
	elif name == "/register.py":
		return register()
	else:
		return "Not Found"
'''