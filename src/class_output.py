__author__ = 'Per'

class Output(object):
    def __init__(self, number_in_port):
        self.Number_in_port = number_in_port

    binaryCode = "00000001"
    def get_strom_an_oder_aus(self):

        number_of_output = self.Number_in_port
        binary_number_for_output =   int(binaryCode[number_of_output])
        if binary_number_for_output == 1:
            stromAn = True
        elif binary_number_for_output == 0:
            stromAn = False
        else:
            stromAn = None
            print("invalid binary number")
        return stromAn

output1 = Output(7)
print(output1.get_strom_an_oder_aus())

