# 15.12.14 Per Starke

from class_port import Port

class Microcontroller(object):

    def __init__(self, name, list_of_ports):
        self.Name = name
        self.List_of_ports = list_of_ports

    # def define_outputs_of_all_ports(self):
    #     j = 0
    #     for port in self.List_of_ports:
    #         list_of_nr_of_outputs_of_ports = [listOfPorts[j]]
    #         j += 1
    #     i = 0
    #     for port in self.List_of_ports:
    #         port.nr_of_outputs_of_port = list_of_nr_of_outputs_of_ports[i]
    #         i += 1

PortB = Port("PortB", 8)
PortC = Port("PortC", 6)
PortD = Port("PortD", 6)
listOfPorts = [PortB, PortC, PortD]
Atmega_controller = Microcontroller("Crumb168 V2.3 AVR ATmega Modul", listOfPorts)

print(PortB.nr_of_outputs_of_port)
print(PortC.nr_of_outputs_of_port)