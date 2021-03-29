import threading
import time

def say():
	print('HAHA')
	time.sleep(1)

def main():
	for i in range(5):
		t = threading.Thread(target=say)

		t.start()

	num = len(threading.enumerate())
	print(num)

if __name__ == "__main__":
	main()