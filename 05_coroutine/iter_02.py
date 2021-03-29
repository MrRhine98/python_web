from collections import Iterable
from collections import Iterator
import time

class Classmate(object):
	def __init__(self):
		self.names = list()
		self.count = 0

	def add(self, name):
		self.names.append(name)


	# make classmate class iterable
	def __iter__(self):
		return self

	def __next__(self):
		if self.count < len(self.names):
			ret = self.names[self.count]
			self.count += 1
			return ret
		else:
			raise StopIteration

classmate = Classmate()

classmate.add("alice")
classmate.add("bob")
classmate.add("cload")

# print("Is classmate iterable:", isinstance(classmate, Iterable))
# classmate_iterator = iter(classmate)
# print("Is iterator:", isinstance(classmate_iterator, Iterator))

# print(next(classmate_iterator))
for name in classmate:
	time.sleep(1)
	print(name)