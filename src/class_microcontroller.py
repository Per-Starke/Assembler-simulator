# 15.12.14 Per Starke

from class_port import Port

class Microcontroller(object):

    def __init__(self, name, code,  list_of_ports, dict_of_registers):
        self.Name = name
        self.Code = code
        self.List_of_ports = list_of_ports
        self.Dict_of_registers = dict_of_registers

    # def create_list_of_registers(self):
    #     list_of_registers = []
    #     for i in range (1, self.Number_of_registers):
    #         list_of_registers.append


    def get_electrizity_on_or_off_for_every_port(self):
        dict_of_ports_and_electrizity_lists = {}
        for port in self.List_of_ports:
            list_of_electrizity_turned_on_or_off = port.get_electrizity_turned_on_or_off_for_list_of_outputs_of_ports()
            dict_of_ports_and_electrizity_lists[port] = list_of_electrizity_turned_on_or_off
        return dict_of_ports_and_electrizity_lists

