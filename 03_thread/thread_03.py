import threading
import time

num = 0
# 互斥锁
mutex = threading.Lock()

def plus1():
	global num
	
	for i in range(100000):
		mutex.acquire()
		num += 1
		mutex.release()

def plus2():
	global num
	
	for i in range(100000):
		mutex.acquire()
		num += 1
		mutex.release()

def main():
	t1 = threading.Thread(target=plus1)
	t2 = threading.Thread(target=plus2)

	t1.start()
	t2.start()
	time.sleep(2)
	print(num)

if __name__ == "__main__":
	main()