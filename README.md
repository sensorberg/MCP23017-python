# MCP23017-python
MCP23017 GPIO-Expander Python Library for RaspberryPi
[MCP23017 Datasheet](http://ww1.microchip.com/downloads/en/devicedoc/20001952c.pdf)

current implemented features 
*  set pin mode INPUT or OUTPUT
*  set pin mode of all pins
*  digital write pin HIGH or LOW
*  digital read pin state
*  digital read pin state of all pins
*  enable interrupt on a pin
*  enable interrupt on all pins
*  enable interrupt mirroring of BANK_A and BANK_B
*  read interrupt flags to see which pin triggered the interrupt
*  read the interrupt capture value of the pin when the interrupt happened