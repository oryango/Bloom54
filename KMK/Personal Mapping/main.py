import board

from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.modules.mouse_keys import MouseKeys

keyboard = KMKKeyboard()

#split
split = Split(
    data_pin=board.GP0,
    data_pin2=board.GP1,
    uart_flip=False
    )

mouse = MouseKeys()
mouse.move_step = 6

keyboard.tap_time = 100

keyboard.modules = [Layers(),split,mouse]


MACRO1 = KC.LCTL(KC.C)
MACRO2 = KC.LCTL(KC.V)
MACRO3 = KC.LCTL(KC.X)
MACRO4 = KC.LCTL(KC.F)

TABOUT = KC.LALT(KC.TAB)
BLANK = KC.NO

LFTCLK = KC.MB_LMB
RGTCLK = KC.MB_RMB

keyboard.keymap = [
        [  #COLEMAK
            KC.ESC,    MACRO1,  MACRO2,  MACRO3,  MACRO4,  TABOUT,                       KC.N6,   KC.N7,   KC.N8,   KC.N9,  KC.N0,  KC.BSPC,
            KC.TAB,    KC.Q,    KC.W,    KC.F,    KC.P,    KC.B,                         KC.J,    KC.L,    KC.U,    KC.Y,   KC.SCLN,KC.BSPC,
            KC.LALT,   KC.A,    KC.R,    KC.S,    KC.T,    KC.G,                         KC.M,    KC.N,    KC.E,    KC.I,   KC.O,   KC.QUOT,
            KC.LSFT,   KC.Z,    KC.X,    KC.C,    KC.D,    KC.V,                         KC.K,    KC.H,    KC.COMM, KC.DOT, KC.SLSH,KC.RSFT,
                                                KC.LCTL,   KC.MO(1),  KC.ENT,  KC.SPC,   KC.RCTL,  KC.MO(2),
        ],

        [  #Layer 1
            KC.ESC,    KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,                      KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,KC.TRNS,KC.BSPC,
            KC.TRNS,   KC.PGUP, KC.W,    KC.UP,   KC.P,    KC.RGUI,                      KC.N0,   KC.N7,   KC.N8,   KC.N9,  KC.PSLS,KC.TRNS,
            KC.TRNS,   KC.PGDN, KC.LEFT, KC.DOWN, KC.RIGHT,KC.LBRC,                      KC.RBRC, KC.N4,   KC.N5,   KC.N6,  KC.EQL, KC.DEL,
            KC.TRNS,   KC.CAPS, KC.HOME, KC.INS,  KC.END,  KC.LPRN,                      KC.RPRN, KC.N1,   KC.N2,   KC.N3,  KC.MINS,KC.TRNS,
                                                KC.TRNS,   KC.TRNS,  KC.TRNS,     KC.TRNS,   KC.TRNS,  KC.TRNS,
        ],

        [  #Layer 2
            KC.ESC,    KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,                      KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,KC.BSPC,
            KC.TRNS,   KC.F10,  KC.F7,   KC.F8,   KC.F9,   KC.GRV,                       BLANK,   LFTCLK,  KC.MS_UP,RGTCLK,  RGTCLK, KC.TRNS,
            KC.TRNS,   KC.F11,  KC.F4,   KC.F5,   KC.F6,   KC.BSLS,                      LFTCLK,  KC.MS_LT,KC.MS_DN,KC.MS_RT,LFTCLK, KC.DEL,
            KC.TRNS,   KC.F12,  KC.F1,   KC.F2,   KC.F3,   KC.LPRN,                      RGTCLK,  BLANK,   BLANK,   BLANK,   RGTCLK,  KC.TRNS,
                                                KC.TRNS,   KC.TRNS,  KC.MO(3),     KC.TRNS,   KC.TRNS,  KC.TRNS,
        ],

        [  #MOUSE MODE
            BLANK,     BLANK,   BLANK,   BLANK,   BLANK,   BLANK,                        BLANK,   BLANK,   BLANK,   BLANK,  BLANK,  BLANK,
            KC.TRNS,   BLANK,   RGTCLK,  KC.MS_UP,LFTCLK,  BLANK,                        KC.Y,    KC.U,    KC.I,    KC.O,   KC.P,   KC.TRNS,
            KC.TRNS,   LFTCLK,  KC.MS_LT,KC.MS_DN,KC.MS_RT,BLANK,                        KC.H,    LFTCLK,  RGTCLK,  KC.L,   KC.PGUP,KC.QUOT,
            KC.TRNS,   RGTCLK,  BLANK,   BLANK,   BLANK,   BLANK,                        KC.N,    KC.M,    KC.COMM, KC.DOT, KC.PGDN,KC.TRNS,
                                                KC.TRNS,   KC.TRNS, KC.TRNS,     KC.TRNS,   KC.TRNS,  KC.TRNS,
        ]
]
if __name__ == '__main__':
    keyboard.go()