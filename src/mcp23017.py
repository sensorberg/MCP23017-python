IODIRA   = 0x00  # Pin direction register
IODIRB   = 0x01  # Pin direction register
IPOLA    = 0x02
IPOLB    = 0x03
GPINTENA = 0x04
GPINTENB = 0x05
DEFVALA  = 0x06
DEFVALB  = 0x07
INTCONA  = 0x08
INTCONB  = 0x09
IOCONA   = 0x0A
IOCONB   = 0x0B
GPPUA    = 0x0C
GPPUB    = 0x0D

INTFA    = 0x0E
INTFB    = 0x0F
INTCAPA  = 0x10
INTCAPB  = 0x11
GPIOA    = 0x12
GPIOB    = 0x13
OLATA    = 0x14
OLATB    = 0x15
ALL_OFFSET = [IODIRA, IODIRB, IPOLA, IPOLB, GPINTENA, GPINTENB, DEFVALA, DEFVALB, INTCONA, INTCONB, IOCONA, IOCONB, GPPUA, GPPUB, GPIOA, GPIOB, OLATA, OLATB]

BANK_BIT    = 7
MIRROR_BIT  = 6
SEQOP_BIT   = 5
DISSLW_BIT  = 4
HAEN_BIT    = 3
ODR_BIT     = 2
INTPOL_BIT  = 1

GPA0 = 0
GPA1 = 1
GPA2 = 2
GPA3 = 3
GPA4 = 4
GPA5 = 5
GPA6 = 6
GPA7 = 7
GPB0 = 8
GPB1 = 9
GPB2 = 10
GPB3 = 11
GPB4 = 12
GPB5 = 13
GPB6 = 14
GPB7 = 15
ALL_GPIO = [GPA0, GPA1, GPA2, GPA3, GPA4, GPA5, GPA6, GPA7, GPB0, GPB1, GPB2, GPB3, GPB4, GPB5, GPB6, GPB7]

HIGH = 0xFF
LOW = 0x00

INPUT = 0xFF
OUTPUT = 0x00

class MCP23017:
	"""
	MCP23017 class to handle ICs register setup

	RegName  |ADR | bit7    | bit6   | bit5   | bit4   | bit3   | bit2   | bit1   | bit0   | POR/RST
	--------------------------------------------------------------------------------------------------
	IODIRA   | 00 | IO7     | IO6    | IO5    | IO4    | IO3    | IO2    | IO1    | IO0    | 1111 1111
	IODIRB   | 01 | IO7     | IO6    | IO5    | IO4    | IO3    | IO2    | IO1    | IO0    | 1111 1111
	IPOLA    | 02 | IP7     | IP6    | IP5    | IP4    | IP3    | IP2    | IP1    | IP0    | 0000 0000
	IPOLB    | 03 | IP7     | IP6    | IP5    | IP4    | IP3    | IP2    | IP1    | IP0    | 0000 0000
	GPINTENA | 04 | GPINT7  | GPINT6 | GPINT5 | GPINT4 | GPINT3 | GPINT2 | GPINT1 | GPINT0 | 0000 0000
	GPINTENB | 05 | GPINT7  | GPINT6 | GPINT5 | GPINT4 | GPINT3 | GPINT2 | GPINT1 | GPINT0 | 0000 0000
	DEFVALA  | 06 | DEF7    | DEF6   | DEF5   | DEF4   | DEF3   | DEF2   | DEF1   | DEF0   | 0000 0000
	DEFVALB  | 07 | DEF7    | DEF6   | DEF5   | DEF4   | DEF3   | DEF2   | DEF1   | DEF0   | 0000 0000
	INTCONA  | 08 | IOC7    | IOC6   | IOC5   | IOC4   | IOC3   | IOC2   | IOC1   | IOC0   | 0000 0000
	INTCONB  | 09 | IOC7    | IOC6   | IOC5   | IOC4   | IOC3   | IOC2   | IOC1   | IOC0   | 0000 0000
	IOCON    | 0A | BANK    | MIRROR | SEQOP  | DISSLW | HAEN   | ODR    | INTPOL | -      | 0000 0000
	IOCON    | 0B | BANK    | MIRROR | SEQOP  | DISSLW | HAEN   | ODR    | INTPOL | -      | 0000 0000
	GPPUA    | 0C | PU7     | PU6    | PU5    | PU4    | PU3    | PU2    | PU1    | PU0    | 0000 0000
	GPPUB    | 0D | PU7     | PU6    | PU5    | PU4    | PU3    | PU2    | PU1    | PU0    | 0000 0000


	"""

	def __init__(self, address, i2c):
		self.i2c = i2c
		self.address = address

	def set_all_output(self):
		""" sets all GPIOs as OUTPUT"""
		self.i2c.write_to(self.address, IODIRA, 0x00)
		self.i2c.write_to(self.address, IODIRB, 0x00)

	def set_all_input(self):
		""" sets all GPIOs as INPUT"""
		self.i2c.write_to(self.address, IODIRA, 0xFF)
		self.i2c.write_to(self.address, IODIRB, 0xFF)

	def pin_mode(self, gpio, mode):
		"""
		Sets the given GPIO to the given mode INPUT or OUTPUT
		:param gpio: the GPIO to set the mode to
		:param mode: one of INPUT or OUTPUT
		"""
		pair = self.get_offset_gpio_tuple([IODIRA, IODIRB], gpio)
		self.set_bit_enabled(pair[0], pair[1], True if mode is INPUT else False)

	def digital_write(self, gpio, direction):
		"""
		Sets the given GPIO to the given direction HIGH or LOW
		:param gpio: the GPIO to set the direction to
		:param direction: one of HIGH or LOW
		"""
		pair = self.get_offset_gpio_tuple([OLATA, OLATB], gpio)
		self.set_bit_enabled(pair[0], pair[1], True if direction is HIGH else False)

	def digital_read(self, gpio):
		"""
		Reads the current direction of the given GPIO
		:param gpio: the GPIO to read from
		:return:
		"""
		pair = self.get_offset_gpio_tuple([GPIOA, GPIOB], gpio)
		bits = self.i2c.read_from(self.address, pair[0])
		return HIGH if (bits & (1 << pair[1])) > 0 else LOW

	def digital_read_all(self):
		"""
		Reads the current direction of the given GPIO
		:param gpio: the GPIO to read from
		:return:
		"""
		return [self.i2c.read_from(self.address, GPIOA),
		        self.i2c.read_from(self.address, GPIOB)]

	def set_interrupt(self, gpio, enabled):
		"""
		Enables or disables the interrupt of a given GPIO
		:param gpio: the GPIO where the interrupt needs to be set, this needs to be one of GPAn or GPBn constants
		:param enabled: enable or disable the interrupt
		"""
		pair = self.get_offset_gpio_tuple([GPINTENA, GPINTENB], gpio)
		self.set_bit_enabled(pair[0], pair[1], enabled)

	def set_all_interrupt(self, enabled):
		"""
		Enables or disables the interrupt of a all GPIOs
		:param enabled: enable or disable the interrupt
		"""
		self.i2c.write_to(self.address, GPINTENA, 0xFF if enabled else 0x00)
		self.i2c.write_to(self.address, GPINTENB, 0xFF if enabled else 0x00)

	def set_interrupt_mirror(self, enable):
		"""
		Enables or disables the interrupt mirroring
		:param enable: enable or disable the interrupt mirroring
		"""
		self.set_bit_enabled(IOCONA, MIRROR_BIT, enable)
		self.set_bit_enabled(IOCONB, MIRROR_BIT, enable)

	def read_interrupt_captures(self):
		"""
		Reads the interrupt captured register. It captures the GPIO port value at the time the interrupt occurred.
		:return: a tuple of the INTCAPA and INTCAPB interrupt capture as a list of bit string
		"""
		return (self._get_list_of_interrupted_values_from(INTCAPA),
		        self._get_list_of_interrupted_values_from(INTCAPB))

	def _get_list_of_interrupted_values_from(self, offset):
		list = []
		interrupted = self.i2c.read_from(self.address, offset)
		bits = '{0:08b}'.format(interrupted)
		for i in reversed(range(8)):
			list.append(bits[i])

		return list

	def read_interrupt_flags(self):
		"""
		Reads the interrupt flag which reflects the interrupt condition. A set bit indicates that the associated pin caused the interrupt.
		:return: a tuple of the INTFA and INTFB interrupt flags as list of bit string
		"""
		return (self._read_interrupt_flags_from(INTFA),
		        self._read_interrupt_flags_from(INTFB))

	def _read_interrupt_flags_from(self, offset):
		list = []
		interrupted = self.i2c.read_from(self.address, offset)
		bits = '{0:08b}'.format(interrupted)
		for i in reversed(range(8)):
			list.append(bits[i])

		return list

	def read(self, offset):
		return self.i2c.read_from(self.address, offset)

	def write(self, offset, value):
		return self.i2c.write_to(self.address, offset, value)

	def get_offset_gpio_tuple(self, offsets, gpio):
		if offsets[0] not in ALL_OFFSET or offsets[1] not in ALL_OFFSET:
			raise TypeError("offsets must contain a valid offset address. See description for help")
		if gpio not in ALL_GPIO:
			raise TypeError("pin must be one of GPAn or GPBn. See description for help")

		offset = offsets[0] if gpio < 8 else offsets[1]
		_gpio = gpio % 8
		return (offset, _gpio)

	def set_bit_enabled(self, offset, gpio, enable):
		stateBefore = self.i2c.read_from(self.address, offset)
		value = (stateBefore | self.bitmask(gpio)) if enable else (stateBefore & ~self.bitmask(gpio))
		self.i2c.write_to(self.address, offset, value)

	def bitmask(self, gpio):
		return 1 << (gpio % 8)
