from decoding import actual_number_of_errors, check_control_sum, decode
from encoding import encode
from transmission import transmit
from bitstring import BitArray

# encodings used to encode and decode packets
encoding = 'utf-8'
# probability of lack of error on a single bit in a packet
probability = 0.9
# path to the file, where experiment results are stored
filepath_results = 'results.txt'


def main():
    data = list(str(input('Enter message')))
    encoded_packets = encode(data, encoding)
    retransmissions = 0
    received_data = []

    for encoded_packet in encoded_packets:
        copy = str(encoded_packet)
        tmp = transmit(encoded_packet, 0.8)

        while not check_control_sum(tmp):
            retransmissions += 1
            encoded_packet = BitArray(copy)
            tmp = transmit(encoded_packet, 0.8)

        received_data.append(decode(tmp))

        actual_number_of_errors(data, received_data, filepath_results)
        with open(filepath_results, 'a') as results:
            results.write(f'{retransmissions}\n')


main()
