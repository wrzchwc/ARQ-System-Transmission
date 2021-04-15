from bitstring import BitArray
from typing import List
from random import seed, random, gauss


def transmit(packets: List[BitArray], probability: float) -> List[BitArray]:
    seed()
    for packet in packets:
        for bit in range(packet.len):
            if random() > probability:
                packet.invert(bit)
    return packets
