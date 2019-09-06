class I2C():
	def __init__(self, smbus):
		"""
		Wrapper class for the smbus
		:param smbus: the smbus to send and receive data from smbus.SMBus(1)
		"""
		self.bus = smbus

	def write_to(self, address, offset, value):
		self.bus.write_byte_data(address, offset, value)

	def read_from(self, address, offset):
		value = self.bus.read_byte_data(address, offset)
		return value

	def read(self, address):
		return self.bus.read_byte(address)

	def scan(self):
		devices = list()
		for address in range(255):
			try:
				self.bus.read_byte(address) #try to read byte
				devices.append(address)
			except:  # exception if read_byte fails
				pass
		return devices