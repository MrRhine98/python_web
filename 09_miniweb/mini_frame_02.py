import time

def login():
	return "Login-------%s" % time.ctime()

def register():
	return "Register-----%s" % time.ctime()

def application(name):
	if name == "/login.py":
		return login()
	elif name == "/register.py":
		return register()
	else:
		return "Not Found"
