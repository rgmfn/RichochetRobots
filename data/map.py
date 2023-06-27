import data.constants as dc

DEST_CONVERSION = {
    'a': (dc.YELLOW, 'spade'),
    'b': (dc.YELLOW, 'diamond'),
    'c': (dc.YELLOW, 'club'),
    'd': (dc.YELLOW, 'heart'),
    # 'e': (dc.GREEN, 'spade'),
    # 'f': (dc.GREEN, 'diamond'),
    # 'g': (dc.GREEN, 'club'),
    # 'h': (dc.GREEN, 'heart'),
    # 'i': (dc.RED, 'spade'),
    # 'j': (dc.RED, 'diamond'),
    # 'k': (dc.RED, 'club'),
    # 'l': (dc.RED, 'heart'),
    # 'm': (dc.BLUE, 'spade'),
    # 'n': (dc.BLUE, 'diamond'),
    # 'o': (dc.BLUE, 'club'),
    # 'p': (dc.BLUE, 'heart'),
}
WALL_CONVERSION = {
    '<': 'left',
    '>': 'right',
    '^': 'top',
    'v': 'bottom',
}

def load_map(file_name: str) -> (dict, dict):
    dests: dict = {}
    walls: dict = {}

    with open(file_name, 'r') as file:
        for iy, line in enumerate(file):
            for ix, ch in enumerate(line):
                if ch in DEST_CONVERSION.keys():
                    dests[(iy, ix)] = DEST_CONVERSION[ch]
                elif ch in '<>v^':
                    walls[(iy, ix)] = WALL_CONVERSION[ch]
                    
    return dests, walls