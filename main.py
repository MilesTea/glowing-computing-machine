class FlatIterator:
	def __init__(self, any_object):
		self.any_object = any_object
		self.length = len(any_object)

	def __iter__(self):
		self.counter = 0
		self.counter_inner = 0
		self.flat_list = list()
		while self.counter_inner < self.length:
			if isinstance(self.any_object[self.counter_inner], list):
				self.inner_iterator = FlatIterator(self.any_object[self.counter_inner])
				for item in self.inner_iterator:
					self.flat_list.append(item)
			else:
				self.flat_list.append(self.any_object[self.counter_inner])
			self.counter_inner += 1
		self.any_object = self.flat_list
		self.length = len(self.any_object)
		return self

	def __next__(self):
		if self.counter >= self.length:
			raise StopIteration
		value = self.any_object[self.counter]
		self.counter += 1
		return value





def flat_generator(raw_list):
	counter = 0
	length = len(raw_list)
	while counter < length:
		if isinstance(raw_list[counter], list):
			for item in flat_generator(raw_list[counter]):
				yield item
			counter += 1
		else:
			yield raw_list[counter]
			counter += 1



nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

for item in FlatIterator(nested_list):
	print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)

for item in flat_generator(nested_list):
	print(item)

flat_list = [item for item in flat_generator(nested_list)]
print(flat_list)

