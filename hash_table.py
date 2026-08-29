class HashTable:

	def __init__(self, initial_capacity=10):
		self.hash_list = []
		for bucket in range(initial_capacity):
			self.hash_list.append([])

	def hash_function(self, package_id):
		return package_id % len(self.hash_list)

	# def insert(self, key, value):
	# 	hash_index = self.hash_function(key)
	# 	self.hash_list[hash_index].append(value)

	def insert(self, key, value):
		hash_index = self.hash_function(key)
		bucket = 0
		key_found = False
		while not key_found and bucket < len(self.hash_list):
			if bucket == hash_index and value not in self.hash_list[hash_index]:
				self.hash_list[hash_index].append(value)
				key_found = True
			bucket += 1

	def lookup(self, package_id):
		# Add error control for non-integers
		result = None
		hash_index = self.hash_function(package_id)
		for i in range(len(self.hash_list[hash_index])):
			if self.hash_list[hash_index][i].get_id() == package_id:
				result = self.hash_list[hash_index][i]
		return result

	def __repr__(self):
		hash_string = "Package ID, Address, State, Zipcode, Deadline, Weight (kg), Loading time, Delivery Time, Status\n"
		for i in range(len(self.hash_list)):
			hash_string += "Bucket: " + str(i) + "\n"
			j = 0
			while j < len(self.hash_list[i]):
				hash_string += str(self.hash_list[i][j]) + "\n"
				j += 1
			hash_string += "\n"
		return hash_string

	def __str__(self):
		# return str(self.hash_list)
		hash_string = "Package ID, Address, State, Zipcode, Deadline, Weight (kg), Loading time, Delivery Time, Status\n"
		for i in range(len(self.hash_list)):
			j = 0
			while j < len(self.hash_list[i]):
				hash_string += str(self.hash_list[i][j]) + "\n"
				j += 1
			hash_string += "\n"
		return hash_string