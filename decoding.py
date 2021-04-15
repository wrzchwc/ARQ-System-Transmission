from typing import List
from bitstring import BitArray


def decode(packets: List[BitArray], encoding: str, filepath: str):
    data = ""
    incorrect = 0

    for packet in packets:
        if (packet[:-1].count(True) % 2) != packet[-1:].uint:
            incorrect += 1
            data += '?'
        else:
            try:
                data = data + bytes.decode(packet[:-1].bytes, encoding)
            except UnicodeDecodeError:
                incorrect += 1
                data += '?'

    # print(f'Odebrano pakietow: {len(packets)} ({len(packets) - incorrect} poprawnych, 'f'{incorrect} niepoprawnych).')
    # print(f'Odebrana wiadomosc: {data}')

    with open(filepath, 'a') as file:
        file.write(f'{len(packets)} {len(packets) - incorrect} {incorrect}')

    return data


def actual_number_of_errors(source: str, current: str, filepath: str):
    incorrect = 0

    for i in range(len(source)):
        if source[i] != current[i]:
            incorrect += 1

    # print(f'Realnie odebrano pakietow: {len(source)} ({len(source) - incorrect} poprawnych, '
    #       f''f'{incorrect} niepoprawnych).')

    with open(filepath, 'a') as file:
        file.write(f' {len(source) - incorrect} {incorrect}\n')
