class FlatIterator:
	def __init__(self, any_object):
		self.any_object = any_object

	def __iter__(self):
		self.counter = 0  			# курсор по начальному списку
		self.counter_inner = 0  	# курсор по "плоскому" списку
		self.length = len(self.any_object) 	# длина начального списка
		self.flat_list = list()		# "плоский" список
		while self.counter_inner < self.length:
			if isinstance(self.any_object[self.counter_inner], list):
				self.inner_iterator = FlatIterator(self.any_object[self.counter_inner])
				for some_item in self.inner_iterator:
					self.flat_list.append(some_item)
			else:
				self.flat_list.append(self.any_object[self.counter_inner])
			self.counter_inner += 1
		self.flat_list_length = len(self.flat_list)  # длина "плоского" списка
		return self

	def __next__(self):
		if self.counter >= self.flat_list_length:
			raise StopIteration
		value = self.flat_list[self.counter]
		self.counter += 1
		return value


def flat_generator(raw_list):
	counter = 0
	length = len(raw_list)
	while counter < length:
		if isinstance(raw_list[counter], list):
			for some_item in flat_generator(raw_list[counter]):
				yield some_item
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
