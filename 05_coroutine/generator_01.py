

def create_num(total_num):
	a, b = 0, 1
	current_num = 0
	while current_num < total_num:
		# print(a)
		yield a				# if key word yield exists, it is a generator instead of a function
		a, b = b, a+b
		current_num += 1

obj = create_num(10) 	# create a generator object

for num in obj:
	print(num)

# next(obj)				# run the generator