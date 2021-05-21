from random import seed, random

from bitstring import BitArray


def transmit(packet: BitArray, probability: float) -> BitArray:
    tmp = packet
    seed()
    for bit in range(tmp.len):
        if random() > probability:
            tmp.invert(bit)
    return tmp
