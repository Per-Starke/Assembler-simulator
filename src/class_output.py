__author__ = 'Per'

class Output(object):
    def __init__(self, number_in_port):
        self.Number_in_port = number_in_port

    binaryCode = "00000001"
    stromAn = None
    def get_strom_an_oder_aus(self):
        number_of_output = self.Number+1
        binary_number_for_output =  binary[- (number_of_output)]
        
