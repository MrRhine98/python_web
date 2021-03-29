def set_level(level):
	def set_func(func):
		def call_func():
			if level == 1:
				print("---Authorization:1---")
			elif level == 2:
				print("---Authorization:2---")
			else:
				print("---Error---")
			return func()
		return call_func
	return set_func


@set_level(1)
def test1():
	print("---test1---")
	return "ok"


@set_level(2)
def test2():
	print("---test2---")
	return "ok"

test1()
test2()