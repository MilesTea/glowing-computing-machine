class FlatIterator:
	def __init__(self, any_object):
		self.any_object = any_object
		self.counter = 0					# внутренний счётчик экземпляра
		self.created = False				# создан ли от этого экземпляра другой экземпляр

	def __iter__(self):
		self.counter = 0
		return self

	def __next__(self):

		# условие для завершения цикла итераций
		if self.counter == len(self.any_object):
			raise StopIteration

		value = self.any_object[self.counter]
		if isinstance(value, list):
			value, is_over = self.split()
			return value
		else:
			self.counter += 1
			return value

	def split(self):												# отвечает за создание экземпляра внутри экземпляра
		if isinstance(self.any_object, list):
			if not self.created:	# проверка, чтобы случайно не перезаписать существующий экземпляр
				self.inner_flat = FlatIterator(self.any_object[self.counter])
				self.created = True

			value, is_over = self.inner_flat.split()

			if is_over:
				self.counter += 1
				self.created = False

			if self.counter == len(self.any_object):
				is_over = True
			else:
				is_over = False

			return value, is_over

		else:
			value = self.any_object
			is_over = True		# сообщает экземпляру выше о том, что можно переходить к созданию следующего экземпляра
			return value, is_over




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

