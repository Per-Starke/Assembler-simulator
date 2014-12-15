# 15.12.14 Per Starke
class Port(object):
    def __init__(self, port_name,  nr_of_outputs_of_port):
        self.Port_name = port_name
        self.Nr_of_outputs_of_port = nr_of_outputs_of_port

    def name(self):
        return self.Name

    def nr_of_outputs_of_port(self):
        return self.Nr_of_outputs_of_port
#
# PortD = Port("PortD", 8)
# PortD.Nr_of_outputs_of_port -= 2
# print(PortD.Nr_of_outputs_of_port)