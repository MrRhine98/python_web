import threading
import time

def say(args):
	print(f'HAHA{args}')
	time.sleep(1)

def main():
	for i in range(5):
		t = threading.Thread(target=say, args=(i,))

		t.start()

if __name__ == "__main__":
	main()		