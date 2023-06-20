import data.constants as dc

DEST_CONVERSION = {
    'a': (dc.COLOR_YELLOW, 'a'),
    'b': (dc.COLOR_YELLOW, 'b'),
    'c': (dc.COLOR_YELLOW, 'c'),
    'd': (dc.COLOR_YELLOW, 'd'),
    'e': (dc.COLOR_GREEN, 'a'),
    'f': (dc.COLOR_GREEN, 'b'),
    'g': (dc.COLOR_GREEN, 'c'),
    'h': (dc.COLOR_GREEN, 'd'),
    'i': (dc.COLOR_RED, 'a'),
    'j': (dc.COLOR_RED, 'b'),
    'k': (dc.COLOR_RED, 'c'),
    'l': (dc.COLOR_RED, 'd'),
    'm': (dc.COLOR_BLUE, 'a'),
    'n': (dc.COLOR_BLUE, 'b'),
    'o': (dc.COLOR_BLUE, 'c'),
    'p': (dc.COLOR_BLUE, 'd'),
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