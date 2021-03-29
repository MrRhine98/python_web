import time
from greenlet import greenlet

def task1():
	while True:
		print("-----1-----")
		t2.switch()
		time.sleep(0.2)
		

def task2():
	while True:
		print("-----2-----")
		t1.switch()
		time.sleep(0.2)
		

# global variable t1 and t2
t1 = greenlet(task1)
t2 = greenlet(task2)
t1.switch()
		

