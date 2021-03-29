import time

URL_FUNC_DICT = dict()

def route(url):
	def set_func(func):
		URL_FUNC_DICT[url] = func
		def call_func(*args, **kwargs):
			return func(*args, **kwargs)
		return call_func
	return set_func

@route("/login.py")
def login():
	return "Login-------%s" % time.ctime()

@route("/register.py")
def register():
	return "Register-----%s" % time.ctime()


def application(environ, start_response):
	start_response("200 OK", [('Content-Type', 'text/html;charset=utf-8')])
	file_name = environ["PATH_INFO"]
	
	try:
		return URL_FUNC_DICT[file_name]()
	except Exception as ret:
		return "Error: %s" % str(ret)

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