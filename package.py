class Package:

	def __init__(self):
		self.id = None
		self.address = ""
		self.city = ""
		self.state = ""
		self.zip_code = ""
		self.deadline = None
		self.weight = 0
		self.loading_time = None
		self.delivery_time = None
		self.delivery_status =""

	def set_id(self, id):
		self.id = id

	def get_id(self):
		return self.id

	def set_address(self, address):
		self.address = address
		
	def get_address(self):
		return self.address

	def set_city(self, city):
		self.city = city
		
	def get_city(self):
		return self.city

	def set_state(self, state):
		self.state = state

	def get_state(self):
		return self.state

	def set_zip_code(self, zip_code):
		self.zip_code = zip_code

	def get_zip_code(self):
		return self.zip_code

	def set_deadline(self, deadline):
		self.deadline = deadline
	
	# For deadline, EOD is 05:00:00 PM
	def get_deadline(self):
		return self.deadline

	def set_weight(self, weight):
		self.weight = weight

	def get_weight(self):
		return self.weight

	def set_loading_time(self, loading_time):
		self.loading_time = loading_time

	def get_loading_time(self):
		return self.loading_time

	def set_delivery_time(self, delivery_time):
		self.delivery_time = delivery_time

	def get_delivery_time(self):
		return self.delivery_time

	def set_delivery_status(self, current_time):

		delayed = self.get_id() == 6 or self.get_id() == 25 or self.get_id() == 28 or self.get_id() == 32
	
		if current_time < self.loading_time and not delayed:
			self.delivery_status = "At the hub"

		elif self.loading_time <= current_time and current_time < self.delivery_time:
			self.delivery_status = "En route"

		elif current_time >= self.delivery_time:
			self.delivery_status = "Delivered"

		else:
			self.delivery_status = "Delayed"

	def get_delivery_status(self):
		return self.delivery_status

	def __repr__(self):
		return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.id, self.address, self.city, self.state, self.zip_code,
														   self.deadline, self.weight, self.loading_time,
														   self.delivery_time, self.delivery_status)
		
	def __str__(self):
		return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.id, self.address, self.city, self.state, self.zip_code,
														   self.deadline, self.weight, self.loading_time,
														   self.delivery_time, self.delivery_status)

