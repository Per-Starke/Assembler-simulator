__author__ = 'Per'

def get_binary_code():
        binary_code = "00000001"
        if len(binary_code) == 8:
            return binary_code



class Output(object):
    def __init__(self, number_in_port):
        self.Number_in_port = number_in_port



    def get_strom_an_oder_aus(self):
        binary_code = get_binary_code()
        number_of_output = self.Number_in_port
        binary_number_for_output =   int(binary_code[number_of_output])
        if binary_number_for_output == 1:
            stromAn = True
        elif binary_number_for_output == 0:
            stromAn = False
        else:
            stromAn = None
            print("invalid binary number")

        print ("Energy at output" , self.Number_in_port , ":" , stromAn)
        return stromAn




output1 = Output(7)
output1.get_strom_an_oder_aus()