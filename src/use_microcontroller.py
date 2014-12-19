__author__ = 'Per'
from class_microcontroller import Microcontroller
from class_port import Port
from class_output import Output

print("\n")

output7 = Output(7)   # definiert den ersten Output, dieser ist der 7. des Ports (bzw. der 8. ab 1)
output7.get_strom_an_oder_aus()   # ist der Strom bei output1 an oder aus?
PortB = Port("PortB", 8)          # PortB hat 8 Ausgänge

PortB_outputs = PortB.define_list_of_outputs()
PortC = Port("PortC", 6)          # PortC hat 6 Ausgänge

PortC_outputs = PortC.define_list_of_outputs()
PortD = Port("PortD", 6)          # PortD hat 6 Ausgänge

PortD_outputs = PortD.define_list_of_outputs()
listOfPorts = [PortB, PortC, PortD]   # Liste der Ports für den Controller Atmega_controller



Atmega_controller = Microcontroller("Crumb168 V2.3 AVR ATmega Modul", listOfPorts)  # definiert Atmega_controller mit Port B, C und D


print("\n")
print(PortB.nr_of_outputs_of_port())
print(PortC.nr_of_outputs_of_port())
print(PortD.nr_of_outputs_of_port())
print("\n")
print(PortB_outputs)
print(PortC_outputs)
print(PortD_outputs)
print("\n")
y = PortB.get_electrizity_turned_on_or_off_for_list_of_outputs_of_ports()
print("\n")
print(y)

list = Atmega_controller.get_electrizity_on_or_off_for_every_port()
print(list)