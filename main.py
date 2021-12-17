class FlatIterator:
	def __init__(self, comp_list):
		self.comp_list = comp_list

	def __iter__(self):
		self.cursor = 0
		self.length = len(self.comp_list)
		self.counter = False
		return self

	def __next__(self):

		if self.cursor >= self.length:
			raise StopIteration

		if isinstance(self.comp_list[self.cursor], list):
			value = self.unpack()
			return value
		else:
			value = self.comp_list[self.cursor]
			self.cursor += 1
			return value

	def unpack(self):
		if self.counter < len(self.comp_list[self.cursor]):
			value = self.comp_list[self.cursor][self.counter]
			self.counter += 1
			if self.counter == len(self.comp_list[self.cursor]):
				self.counter = 0
				self.cursor += 1
			return value


nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]
for item in FlatIterator(nested_list):
	print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)