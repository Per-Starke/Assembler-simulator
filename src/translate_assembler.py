__author__ = 'Per'

from binary_class import Binary

def binary_number_into_eight_digits(binary_number):
    new_binary_number = []
    while len(binary_number) < 8:
        new_binary_number.append("0")
        for number in binary_number:
            new_binary_number.append(number)
    return (new_binary_number)

binary_number_class = Binary(2, 24)
binary_number = binary_number_class.ausrechnen()
print(binary_number)


new_bina = binary_number_into_eight_digits(binary_number)
print(new_bina)



registers = ["7", "24", "42"] # Assembler sourcecode in numbers
