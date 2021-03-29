import gevent
import time
from gevent import monkey

monkey.patch_all()

def f(n):
	for i in range(n):
		print(gevent.getcurrent(), i)
		time.sleep(0.5)

gevent.joinall([
	gevent.spawn(f, 5),
	gevent.spawn(f, 5),
	gevent.spawn(f, 5)])
