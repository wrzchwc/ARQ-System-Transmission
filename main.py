from decoding import actual_number_of_errors, check_control_sum, decode
from encoding import encode
from transmission import transmit

# encodings used to encode and decode packets
encoding = 'utf-8'
# probability of lack of error on a single bit in a packet
probability = 0.9
# path to the file, where experiment results are stored
filepath = 'txt/results'
# path to file, where experimental data is stored
filepath_data = 'txt/sampleFICT.txt'


def main():
    data = list(str(input('Enter message: ')))
    encoded_packets = encode(data, encoding)
    retransmissions = 0
    received_data = []

    for encoded_packet in encoded_packets:
        tmp = transmit(encoded_packet, probability)
        while not check_control_sum(tmp):
            retransmissions += 1
            tmp = transmit(tmp, probability)
        received_data.append(decode(tmp))

    print(f'Retransmissions: {retransmissions}')
    actual_number_of_errors(data, received_data, filepath)


if __name__ == "__main__":
    main()
