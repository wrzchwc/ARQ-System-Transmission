from random import seed, random

from bitstring import BitArray


def transmit(packet: BitArray, probability: float) -> BitArray:
    seed()
    for bit in range(packet.len):
        tmp = random()
        if tmp > probability:
            packet.invert(bit)
    return packet
