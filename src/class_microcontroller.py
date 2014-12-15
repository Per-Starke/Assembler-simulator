# 15.12.14 Per Starke

class Microcontroller(object):

    def __init__(self, name, nr_of_ports, nr_of_outputs):
        self.Name = name
        self.Nr_Of_Ports = nr_of_ports
        self.Nr_Of_Outputs = nr_of_outputs

    list_of_possible_ports = ["PortB", "PortC", "PortD"]
    def define_outputs(self, port, nr_of_outputs):
