

def create_num(total_num):
	a, b = 0, 1
	current_num = 0
	while current_num < total_num:
		ret = yield a
		print("Send in:", ret)	
		a, b = b, a+b
		current_num += 1

obj = create_num(20) 	# create a generator object

ret = next(obj)
print(ret)
ret = obj.send("hhhh")
print(ret)
