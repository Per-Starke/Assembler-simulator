__author__ = 'Per'


def get_binary_code():             # that function will change again when scanning the assembler works
<<<<<<< HEAD
        binary_code = "00000001"        # it returns a binary number as a string
        if len(binary_code) == 8:        # binary number's lenghts must be 8! I'm working with 8-bit
            return binary_code
=======
        binary_code = "11001100"  # it returns a binary number AS A STRING!
        binary_code2 = "11110000"
        binary_code3 = "00000111"
        list_of_binary_codes = [binary_code, binary_code2, binary_code3]
        if len(binary_code) == 8 & len(binary_code2) == 8 & len(binary_code3) == 8:        # binary number's lenghts must be 8! I'm working with 8-bit
            return list_of_binary_codes
        else:
            print("W R O N G    B I N A R Y    N U M B E R")
            return "00000000"
>>>>>>> d9f1d9a9a2fc46f315e529489df850d3c922cff6




class Output(object):                               # one output in the port's
    def __init__(self, number_in_port):
        self.Number_in_port = number_in_port        # has a number in the port, e.g. PortB0, PortC4, PortD5 etc.


    def number_in_port(self):                       # returns the number_in_port
        return self.Number_in_port

<<<<<<< HEAD
    def get_strom_an_oder_aus(self):                # tells this output whether it's 1 or 0 (falling bacuk upon binary number)
        binary_code = get_binary_code()             # call's get_binary_code
        binary_number_for_output =   int(binary_code[self.Number_in_port])  # get's the number of the binary code (0/1) for the output
        if binary_number_for_output == 1:           # if number is 1
            stromAn = True                          # electrizity is turned on
        elif binary_number_for_output == 0:         # if it's 0
            stromAn = False                         # it's turned off
        else:                                       # else...
            stromAn = None                          # the binary number is wrong. binary only contains 0 and 1
            print("invalid binary number")

        print ("Electrizity at output" , self.Number_in_port , ":" , stromAn)        # tells whether electrizity is turned on or off
        return stromAn                              # returns a boolean for StromAn
=======
    def get_strom_an_oder_aus(self, number):                                        # does the binary number tell THIS output to be on or off?
        binary_code_list = get_binary_code()
        binary_code = binary_code_list[number]
                                             # call's get_binary_code
        binary_number_for_output =   int(binary_code[self.Number_in_port])  # get's the number of the binary code (0/1) for the output
        if binary_number_for_output == 1:                                   # if number is one
            stromAn = True                                                  # electrizity is turned on
        elif binary_number_for_output == 0:                                 # if it's 0
            stromAn = False                                                 # it's turned off
        else:                                                               # else...
            stromAn = None                                                  # the binary number is wrong. binary only contains 0 and 1
            print("invalid binary number")

        return stromAn                              # returns a boolean
>>>>>>> d9f1d9a9a2fc46f315e529489df850d3c922cff6



