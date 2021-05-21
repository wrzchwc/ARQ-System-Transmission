# This is version of the program using CRC to minimize transmission errors
from bitstring import BitArray
from typing import List
from transmission import transmit
from decoding import actual_number_of_errors

# encoding used to encode and decode packets
encoding = 'utf-16 be'
# probability of lack of error on a single bit in packet, error_probability = 1 - probability
probability = 0.9
# Polynomial used for check value generating
polynomial = '111010101'  # CRC-8: x⁸+x⁷+x⁶+x⁴+x²+1
# path to file, where results will be saved
filepath_results = 'results.txt'


# Source: https://en.wikipedia.org/wiki/Cyclic_redundancy_check
def crc_remainder(input_bitstring, polynomial_bitstring, initial_filler):
    """calculates the CRC remainder of a string of bits using a chosen polynomial.
    initial_filler should be '1' or '0'."""
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


# Source: https://en.wikipedia.org/wiki/Cyclic_redundancy_check
def crc_check(input_bitstring, polynomial_bitstring, check_value):
    """calculates the CRC check of a string of bits using a chosen polynomial."""
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


def encode(data: list, codec: str) -> List[BitArray]:
    """encodes elements of the list into packets"""
    ready_packets = []
    for d in data:
        tmp = BitArray(bytearray(d, codec))
        ready_packets.append(tmp)
    return ready_packets


def decode(packet: BitArray) -> str:
    """decodes [packets using utf-8 encoding"""
    try:
        return bytes.decode(packet[-8:].bytes, 'utf-8')
    except UnicodeDecodeError:
        return '?'


def main():
    data = list(str(input('Enter message: ')))
    encoded_packets = encode(data, encoding)
    retransmissions = 0
    received_data = []
    for encoded_packet in encoded_packets:
        copy = str(encoded_packet)
        check_value = crc_remainder(encoded_packet.bin, polynomial, '0')
        tmp = transmit(encoded_packet, probability)

        while not crc_check(tmp.bin, polynomial, check_value):
            retransmissions += 1
            encoded_packet = BitArray(copy)
            tmp = transmit(encoded_packet, probability)
        received_data.append(decode(tmp))
    actual_number_of_errors(data, received_data, filepath_results)
    with open(filepath_results, 'a') as results:
        results.write(f'{retransmissions}\n')


if __name__ == "__main__":
    main()
