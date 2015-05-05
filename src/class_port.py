# 15.12.14 Per Starke
from class_output import Output


class Port(object):             # one of the port's of the microcontroller
    def __init__(self, port_name, port_nr,  nr_of_outputs_of_port):
        self.Port_name = port_name                      # has a name (PortB, PortC, PortD etc.)
<<<<<<< HEAD
        self.Nr_of_outputs_of_port = nr_of_outputs_of_port  # and a number of outputs (max. 8 due to 8bit)
=======
        self.Port_nr = port_nr
        self.Nr_of_outputs_of_port = nr_of_outputs_of_port  # and a number of outputs (max. 8)
>>>>>>> d9f1d9a9a2fc46f315e529489df850d3c922cff6

    def name(self):                      # returns the name
        return self.Name

    def nr_of_outputs_of_port(self):            # returns the number of outputs
        return self.Nr_of_outputs_of_port

    def define_list_of_outputs(self):           # makes a list of the outputs (type: class/Output)
        counter = 8-self.nr_of_outputs_of_port()                            # counter to tell which number the Output will receive to number all way through
        list_of_outputs = []                    # the empty list of the outputs
<<<<<<< HEAD
        for _ in range(0, self.Nr_of_outputs_of_port):      # for every output (range 0 to number of outputs)...
            output = Output(counter)                        # output is an Output with number counter
=======
        for i in range(0, self.Nr_of_outputs_of_port):      # for every output (range 0 to number of outputs)...
            output = Output(counter)                        # output is an Output with number "counter"
>>>>>>> d9f1d9a9a2fc46f315e529489df850d3c922cff6
            list_of_outputs.append(output)                  # add this output to the list of outputs
            counter += 1
        return list_of_outputs

    def get_electrizity_turned_on_or_off_for_list_of_outputs_of_ports(self):       # get's whether the electricity is turned on or off for the whole list of outputs
        list_of_outputs_of_port = self.define_list_of_outputs()                    # list of outputs uses define list of outputs to create a list with the Port's outputs
        counter = len(list_of_outputs_of_port)-1
        list_of_outputs_electrizity_on_or_off = []

        for output in list_of_outputs_of_port:                                         # for every output in the list of outputs (classes!)
            onOrOff = list_of_outputs_of_port[counter].get_strom_an_oder_aus(self.Port_nr)                   # get's whether electrizity is turned on or off
            counter -= 1
            list_of_outputs_electrizity_on_or_off.append(onOrOff)
        return list_of_outputs_electrizity_on_or_off


 # remember: Output 7 6 5 4 3 2 1 0
 #           binary 0 0 0 0 0 0 0 1
 #   Output 0 is "on"





