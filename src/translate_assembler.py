__author__ = 'Per'

from binary_class import Binary

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



registers = ["7", "24", "42"] # assembler sourcecode in numbers