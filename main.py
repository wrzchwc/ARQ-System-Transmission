from decoding import decode, actual_number_of_errors
from encoding import encode
from transmission import transmit

# encodings used to encode and decode packets
encoding = 'utf-8'
# probability of lack of error on a single bit in a packet
probability = 90
# path to the file, where experiment results are stored
filepath = 'txt/results'
# path to file, where experimental data is stored
datapath = 'txt/sampleFICT.txt'


def main():
    with open(datapath) as file:
        for line in file:
            data = str(line).rstrip()
            encoded_packets = encode(data, encoding)
            transmitted_packets = transmit(encoded_packets, probability)
            received_data = decode(transmitted_packets, encoding, filepath)
            actual_number_of_errors(data, received_data, filepath)


if __name__ == "__main__":
    main()
