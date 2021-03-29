
def line(k, b):
	def create_y(x):
		print(k*x + b)
	return create_y

line_1 = line(1, 2)
line_1(1)
line_1(2)


x = 300
def test1():
	x = 200
	def test2():
		nonlocal x
		print("->%d" % x)  # x = 200
		x = 100
		print("->%d" % x)  # x = 100
	return test2

t1 = test1()
t1()