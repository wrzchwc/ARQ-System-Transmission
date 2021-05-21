from typing import List

from bitstring import BitArray


def encode(data: list, encoding: str) -> List[BitArray]:
    """encodes elements of the list into packets and generates parity bit for each packet"""
    ready_packets = []
    for d in data:
        tmp = BitArray(bytearray(d, encoding))
        if tmp.count(True) % 2 == 1:
            tmp.append(BitArray(uint=1, length=1))
        else:
            tmp.append(BitArray(uint=0, length=1))
        ready_packets.append(tmp)
    return ready_packets
