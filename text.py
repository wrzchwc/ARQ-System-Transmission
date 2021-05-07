# filepath = 'txt/sampleACAD.txt'
# output = 'txt/data.txt'
#
# data = []
#
# with open(filepath) as file:
#     for line in file:
#         for name in line.split():
#             data.append(name)
#
# with open(output, 'w') as file:
#     for name in data:
#         file.write(name + '\n')
data = '0000000001111010'
polynomial = '111010101'


def crc_remainder(input_bitstring, polynomial_bitstring, initial_filler):
    """Calculate the CRC remainder of a string of bits using a chosen polynomial.
    initial_filler should be '1' or '0'.
    """
    polynomial_bitstring = polynomial_bitstring.lstrip('0')
    len_input = len(input_bitstring)
    initial_padding = (len(polynomial_bitstring) - 1) * initial_filler
    input_padded_array = list(input_bitstring + initial_padding)
    while '1' in input_padded_array[:len_input]:
        cur_shift = input_padded_array.index('1')
        for i in range(len(polynomial_bitstring)):
            input_padded_array[cur_shift + i] \
                = str(int(polynomial_bitstring[i] != input_padded_array[cur_shift + i]))
    return ''.join(input_padded_array)[len_input:]


def crc_check(input_bitstring, polynomial_bitstring, check_value):
    """Calculate the CRC check of a string of bits using a chosen polynomial."""
    polynomial_bitstring = polynomial_bitstring.lstrip('0')
    len_input = len(input_bitstring)
    initial_padding = check_value
    input_padded_array = list(input_bitstring + initial_padding)
    while '1' in input_padded_array[:len_input]:
        cur_shift = input_padded_array.index('1')
        for i in range(len(polynomial_bitstring)):
            input_padded_array[cur_shift + i] \
                = str(int(polynomial_bitstring[i] != input_padded_array[cur_shift + i]))
    return '1' not in ''.join(input_padded_array)[len_input:]


print(crc_check(data, polynomial, crc_remainder(data, polynomial, '0')))
