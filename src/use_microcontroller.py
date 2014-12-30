__author__ = 'Per'
from class_microcontroller import Microcontroller
from class_port import Port
from class_output import Output


PortB = Port("PortB", 0, 8)

PortB_outputs = PortB.define_list_of_outputs()
PortC = Port("PortC", 1, 6)

PortC_outputs = PortC.define_list_of_outputs()
PortD = Port("PortD", 2, 6)

PortD_outputs = PortD.define_list_of_outputs()
listOfPorts = [PortB, PortC, PortD]



Atmega_controller = Microcontroller("Crumb168 V2.3 AVR ATmega Modul", "m168def.inc", listOfPorts)  # definiert Atmega_controller mit Port B, C und D


dict_of_electricity_on_or_off_for_every_port = Atmega_controller.get_electrizity_on_or_off_for_every_port()

print(dict_of_electricity_on_or_off_for_every_port)