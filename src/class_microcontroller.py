# 15.12.14 Per Starke

from class_port import Port

class Microcontroller(object):

    def __init__(self, name, list_of_ports):
        self.Name = name
        self.List_of_ports = list_of_ports

    def get_electrizity_on_or_off_for_every_port(self):
        dict_of_ports_and_electrizity_lists = {}
        for port in self.List_of_ports:
            list_of_electrizity_turned_on_or_off = port.get_electrizity_turned_on_or_off_for_list_of_outputs_of_ports()
            dict_of_ports_and_electrizity_lists[port] = list_of_electrizity_turned_on_or_off
        return dict_of_ports_and_electrizity_lists



