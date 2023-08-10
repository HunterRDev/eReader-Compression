'''Split Game Boy Advance e-Reader binaries into their component VPK files.'''

import os
from bitstring import BitArray
CARD_TYPE = 'Animal Crossing'
# CARD_TYPE could be expanded to other cards later;
# only Animal Crossing is currently supported.
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) + '/cards'
IN_DIR = BASE_DIR + '/bin/'
OUT_DIR = BASE_DIR + '/vpk/'
for file in os.listdir(IN_DIR):
    if file.endswith(".bin"):
        full_path = IN_DIR + file
        a = BitArray(filename=full_path)

        # vpk0 = 0x76706B30. vpk0 is the header for each chunk of data we want
        for chunk_num, chunk in enumerate(
                a.split('0x76706B30', bytealigned=True)):
            card_extension = '.vpk'
            note = '_'
            # skip chunk 0 (when batch processing *.vpk files).
            # it's a header rather than a compressed VPK chunk
            if chunk_num == 0:
                card_extension = '.header'
            if CARD_TYPE == 'Animal Crossing':
                if chunk_num == 1:
                    # hunch, bigger because of graphics data
                    note = note + "GBA"
                if chunk_num == 2:
                    note = note + "GC"
            if note == '_':
                note = ''
            out_name = OUT_DIR + file[:-4] + '_' + \
                str(chunk_num) + note + card_extension
            open(out_name, 'wb').write(chunk.tobytes())
