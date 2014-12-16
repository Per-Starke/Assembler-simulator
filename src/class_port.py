# 15.12.14 Per Starke
from class_output import Output


class Port(object):             # one of the port's of the microcontroller
    def __init__(self, port_name,  nr_of_outputs_of_port):
        self.Port_name = port_name                      # has a name (PortB, PortC, PortD etc.)
        self.Nr_of_outputs_of_port = nr_of_outputs_of_port  # and a number of outputs (max. 8)

    def name(self):             #returns the name
        return self.Name

    def nr_of_outputs_of_port(self):            # returns the number of outputs
        return self.Nr_of_outputs_of_port

    def define_list_of_outputs(self):           # makes a list of the outputs (type: class/Output)
        counter = 0                             # counter to tell which number the Output will receive 
        list_of_outputs = []
        for i in range(0, self.Nr_of_outputs_of_port):
            output = Output(counter)
            list_of_outputs.append(output)
            counter += 1
        return list_of_outputs

    def get_strom_an_oder_aus_for_list_of_outputs_of_ports(self):
        list_of_outputs_of_port = self.define_list_of_outputs()
        zaehler = 0
        for nr in list_of_outputs_of_port:
            list_of_outputs_of_port[zaehler].get_strom_an_oder_aus()
            zaehler += 1


