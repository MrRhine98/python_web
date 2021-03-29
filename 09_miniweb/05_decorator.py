def set_func(func):
	def call_func(*args, **kwargs):
		print("1111")
		print("2222")
		func(*args, **kwargs)
	return call_func


@set_func
def test(*args, **kwargs):
	print("3333%d" % args)

test()

# result
'''
1111
2222
3333
'''