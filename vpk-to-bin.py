'''Combines VPK files into a single .bin file for use with the e-Reader.'''

import os
import glob
import warnings
import bitstring
CARD_ID_DELIMITER = '_'
CHUNKS_PER_CARD = 3
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) + '/cards'
IN_DIR = BASE_DIR + '/vpk/'
OUT_DIR = BASE_DIR + '/bin/'

directory = os.listdir(IN_DIR)
groups = set()
for file in directory:
    card_id = file.partition(CARD_ID_DELIMITER)[0]
    groups.add(card_id)

for group in groups.copy():
    card_glob = glob.glob(IN_DIR + group + "*")

    if len(card_glob) < CHUNKS_PER_CARD:
        length_warn = "less than" + \
            str(CHUNKS_PER_CARD) + \
            " files/folders with similar names found; check the vpk folder."
    if len(card_glob) > CHUNKS_PER_CARD:
        length_warn = "more than" + \
            str(CHUNKS_PER_CARD) + \
            " files/folders with similar names found; check the vpk folder."
    if len(card_glob) != CHUNKS_PER_CARD:
        warnings.warn(length_warn)
        groups.discard(group)

# Combining VPK to .bin
for group in groups.copy():
    print(group)
    header_num = 0
    head_path = glob.glob(IN_DIR + group + "_" + str(header_num) + "*")[0]
    print(head_path)
    card = bitstring.BitArray(filename=head_path)
    print("head len: ", hex(card.len))
    for num in range(1, CHUNKS_PER_CARD):
        chunk_path = glob.glob(IN_DIR + group + "_" + str(num) + "*")[0]
        print(glob.glob(IN_DIR + group + "_" + str(num) + "*"))
        print(chunk_path)
        chunk = bitstring.Bits(filename=chunk_path)
        print("chunk lenth: ", chunk.length)
        card.append(chunk)
        print("fl cl: ", card.length, " ", hex(card.length),
              " ", int(str(card.length), 16) / 2)

    # Attempting to automatically add some padding, but likely need to manually add more
    proper_length = 0x81c
    print("prop len: ", proper_length, hex(proper_length))
    pad_length = int(proper_length - (card.length / 8))
    print("card l: ", card.length, " ", hex(card.length))
    print("pad l: ", pad_length, "\n")
    print(b"\00" * pad_length)
    card.append(b"\00" * pad_length)
    out_name = OUT_DIR + group + ".bin"
    open(out_name, 'wb').write(card.tobytes())
