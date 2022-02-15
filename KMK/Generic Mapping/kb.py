import board
import busio

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.matrix import DiodeOrientation
from kmk.matrix import intify_coordinate as ic

class KMKKeyboard(_KMKKeyboard):
    row_pins = [board.GP11, board.GP12, board.GP13, board.GP14, board.GP15]
    col_pins = [board.GP16, board.GP17, board.GP18, board.GP19, board.GP20, board.GP21]
    diode_orientation = DiodeOrientation.COLUMNS

    #i2c = busio.I2C(scl=board.GP9, sda=board.GP8)

    #tx_l = board.GP0
    #rx_l = board.GP1

    #tx_r = board.GP4
    #rx_r = board.GP5

    coord_mapping = []
    coord_mapping.extend(ic(0, x) for x in range(12))
    coord_mapping.extend(ic(1, x) for x in range(12))
    coord_mapping.extend(ic(2, x) for x in range(12))
    coord_mapping.extend(ic(3, x) for x in range(12))
    # And now, to handle R3, which at this point is down to just six keys
    coord_mapping.extend(ic(4, x) for x in range(3, 9))
