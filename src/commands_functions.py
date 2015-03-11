__author__ = 'Per'

from binary_class import Binary
from class_port import Port
from class_output import Output
from class_microcontroller import Microcontroller

def binary_number_into_eight_bit(binary_number):
    new_binary_number = []
    counter_binary = list(binary_number)
    while len(counter_binary) < 8:
        new_binary_number.append("0")
        counter_binary.append("0")
    new_binary_number.append(binary_number)
    return "".join(new_binary_number)

binary_number_class = Binary(2, 1)
binary_number = binary_number_class.ausrechnen()
print(binary_number)

new_bina = binary_number_into_eight_bit(binary_number)
print(new_bina)


code = ["7", "24", "42"] # assembler sourcecode in numbers



PortB = Port("PortB", 0, 8)

PortB_outputs = PortB.define_list_of_outputs()
PortC = Port("PortC", 1, 6)

PortC_outputs = PortC.define_list_of_outputs()
PortD = Port("PortD", 2, 6)

PortD_outputs = PortD.define_list_of_outputs()

listOfPorts = [PortB, PortC, PortD]
dict_of_registers = {"r16" : "00000000", "r17" : "00000000", "r18" : "00000000", "r19" : "00000000", "r20" : "00000000", "r21": "00000000"}

Atmega_controller = Microcontroller("Crumb168 V2.3 AVR ATmega Modul", "m168def.inc", listOfPorts, dict_of_registers)  # definiert Atmega_controller mit Port B, C und D

def ldi(register, binary_number):   # number = 7
    Atmega_controller.Dict_of_registers[register] = binary_number

ldi("r16", "00110011")
print(Atmega_controller.Dict_of_registers)