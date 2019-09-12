# MCP23017-python
This is a Python Library for the MCP23017 GPIO-Expander intender for use with on a RaspberryPi.

You can see the MCP23017 Datasheet [here](http://ww1.microchip.com/downloads/en/devicedoc/20001952c.pdf).

## Features

Currently implemented features:
*  Set pin mode INPUT or OUTPUT
*  Set pin mode of all pins
*  Setting digital write pin to HIGH or LOW
*  Reading the digital state of a specific pin
*  Reading the state of all digital pins
*  Enabling an interrupt on a specific pin
*  Enabling interrupts on all pins
*  Enabling interrupt mirroring of BANK_A and BANK_B
*  Reading interrupt flags to see which pin triggered the interrupt
*  Reading the interrupt capture value of the pin when the interrupt happened

Not implemented: 
*  Explicit methods for setting additional interupt configuration options (e.g. the ODR bit) - these can be manually set, however.

## Getting started

Setup a MCP23017 object
```
from mcp23017 import *
from i2c import I2C
import smbus

i2c = I2C(smbus.SMBus(1))  # creates a I2C Object as a wrapper for the SMBus
mcp = MCP23017(0x20, i2c)   # creates an MCP object with the given address
```
For additional examples of calls, see the [test_mcp23017.py](https://git.sensorberg.io/embedded/mcp23017-python/blob/master/test_mcp23017.py) file.
