import unittest
from test import smbusmock
from .context import *

class TestI2c(unittest.TestCase):

	def test_i2c_init(self):
		smbus = smbusmock.MBusMock()
		i2c = I2C(smbus)
		self.assertEqual(i2c.bus, smbus)


	def test_write_read_data(self):
		i2c = I2C(smbusmock.MBusMock())
		self.assertEqual(i2c.read_from(0x20, 0x01), 0xff)
		i2c.write_to(0x20, 0x01, 0x00)
		self.assertEqual(i2c.read_from(0x20, 0x01), 0x00)

	def test_read(self):
		i2c = I2C(smbusmock.MBusMock())
		self.assertEqual(i2c.read(0x20), 0xff)

	def test_scan(self):
		i2c = I2C(smbusmock.MBusMock())
		devices = i2c.scan()
		self.assertEqual(len(devices), 8)
