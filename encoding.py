from typing import List

from bitstring import BitArray


def encode(data: str, encoding: str) -> List[BitArray]:
    message = list(data)
    encoded_packets = generate_parity_bits(message, encoding)
    return encoded_packets


def generate_parity_bits(data: list, encoding: str) -> List[BitArray]:
    ready_packets = []
    for d in data:
        tmp = BitArray(bytearray(d, encoding))
        if tmp.count(True) % 2 == 1:
            tmp.append(BitArray(uint=1, length=1))
        else:
            tmp.append(BitArray(uint=0, length=1))
        ready_packets.append(tmp)
    return ready_packets
