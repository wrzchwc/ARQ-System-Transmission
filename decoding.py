from typing import List
from bitstring import BitArray


def actual_number_of_errors(source: list, current: list, filepath: str):
    incorrect = 0
    really_incorrect = 0

    for i in range(len(source)):
        if source[i] != current[i]:
            incorrect += 1
    for i in range(len(source)):
        if source[i] != '?' and current[i] == '?':
            really_incorrect += 1

    print(
        f'Packets (considered): {len(source)} ({len(source) - really_incorrect} correct, {really_incorrect} incorrect)')
    print(f'Packets (really): {len(source)} ({len(source) - incorrect} correct, {incorrect} incorrect)')

    # with open(filepath, 'a') as file:
    #     file.write(f' {len(source) - incorrect} {incorrect}\n')


# determines whether packet was sent correctly or not by comparing newly calculated control sum with the received one
def check_control_sum(packet: BitArray) -> bool:
    if packet[-9:-1].count(True) % 2 != packet[-1:].uint:
        return False
    return True


def decode(packet: BitArray) -> str:
    try:
        return bytes.decode(packet[-9:-1].bytes, 'utf-8')
    except UnicodeDecodeError:
        return '?'
