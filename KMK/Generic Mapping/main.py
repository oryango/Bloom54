import board

from kb import KMKKeyboard
from kmk.consts import UnicodeMode
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitType
from kmk.extensions.media_keys import MediaKeys
from kmk.handlers.sequences import send_string

keyboard = KMKKeyboard()

# split
split = Split(
    data_pin=board.GP0,
    data_pin2=board.GP1,
    uart_flip=False
    )

keyboard.modules = [Layers(), split, MediaKeys()]
keyboard.unicode_mode = UnicodeMode.WINC


# Examples of Custom keycodes
MACRO1 = KC.LCTL(KC.C)  # Copy
MACRO2 = KC.LCTL(KC.V)  # Paste
MACRO3 = KC.LCTL(KC.X)  # Cut

TABOUT = KC.LALT(KC.TAB)  # Alt + Tab
LYRSPC = KC.LT(4, KC.SPC)  # Go to layer 4 if held down but prints space if tapped
BLANK = KC.NO  # Custom name for KC.NO

EMOTE_TXT = send_string('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
EMOTE_CRY = send_string(';-;')

# For other keycodes check the link below:
# https://github.com/KMKfw/kmk_firmware/blob/master/docs/keycodes.md

keyboard.keymap = [

    [  # Layer 0 - BASE/QWERTY LAYER
        KC.ESC,     KC.N1,      KC.N2,      KC.N3,      KC.N4,      KC.N5,          KC.N6,      KC.N7,      KC.N8,      KC.N9,      KC.N0,      KC.BSPC,
        KC.TAB,     KC.Q,       KC.W,       KC.E,       KC.R,       KC.T,           KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,       KC.DEL,
        KC.LCTL,    KC.A,       KC.S,       KC.D,       KC.F,       KC.G,           KC.H,       KC.J,       KC.K,       KC.L,       KC.SCLN,    KC.QUOT,
        KC.LSFT,    KC.Z,       KC.X,       KC.C,       KC.V,       KC.B,           KC.N,       KC.M,       KC.COMM,    KC.DOT,     KC.SLSH,    KC.RSFT,
                                            KC.RGUI,    KC.MO(1),   KC.ENT,         KC.SPC,     KC.MO(2),   KC.RALT,
    ],

    [  # Layer 1 - NUM/NAVIGATION LAYER
        KC.TILD,    KC.EXLM,    KC.AT,      KC.HASH,    KC.DLR,     KC.PERC,        KC.CIRC,    KC.AMPR,    KC.ASTR,    KC.LPRN,    KC.RPRN,    KC.BSPC,
        KC.GRV,     KC.N1,      KC.N2,      KC.N3,      KC.N4,      KC.N5,          KC.N6,      KC.N7,      KC.N8,      KC.N9,      KC.N0,      KC.TRNS,
        KC.PGUP,    KC.LEFT,    KC.UP,      KC.DOWN,    KC.RGHT,    KC.LBRC,        KC.RBRC,    KC.N4,      KC.N5,      KC.N6,      KC.PLUS,    KC.PIPE,
        KC.PGDN,    KC.HOME,    KC.END,     KC.INS,     KC.PSCR,    KC.LCBR,        KC.RCBR,    KC.N1,      KC.N2,      KC.N3,      KC.MINS,    KC.TRNS,
                                            KC.TRNS,    KC.TRNS,    KC.TRNS,        KC.TRNS,    KC.MO(3),  KC.N0,
    ],

    [  # Layer 2 - UTILITY/SYMBOL LAYER
        KC.F1,      KC.F2,      KC.F3,      KC.F4,      KC.F5,      KC.F6,          KC.F7,      KC.F8,      KC.F9,      KC.F10,     KC.F11,     KC.F12,
        KC.TILD,    KC.EXLM,    KC.AT,      KC.HASH,    KC.DLR,     KC.PERC,        KC.CIRC,    KC.AMPR,    KC.ASTR,    KC.LPRN,    KC.RPRN,    KC.TRNS,
        KC.CAPS,    KC.MUTE,    KC.VOLD,    KC.VOLU,    KC.PGUP,    KC.UNDS,        KC.PLUS,    KC.HOME,    KC.PSCR,    KC.SLCK,    KC.PAUS,    KC.BSLS,
        KC.MSTP,    KC.MPLY,    KC.MPRV,    KC.MNXT,    KC.PGDN,    KC.MINS,        KC.EQL,     KC.END,     KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,
                                            KC.TRNS,    KC.MO(3),   KC.TRNS,        KC.TRNS,    KC.TRNS,    KC.TRNS,
    ],

    [  # Layer 3 - EMOJI/PLACEHOLDER LAYER
        BLANK,      BLANK,      KC.N2,      KC.N3,      KC.N4,      KC.N5,          KC.N6,      KC.N7,      KC.N8,      KC.N9,      KC.N0,      KC.BSPC,
        BLANK,      KC.Q,       KC.W,       KC.E,       KC.R,       EMOTE_TXT,      BLANK,       KC.U,       KC.I,       KC.O,       KC.O,       KC.P,
        KC.LCTL,    KC.A,       KC.S,       KC.D,       KC.F,       EMOTE_CRY,      EMOTE_CRY,  KC.J,       KC.K,       KC.L,       KC.SCLN,    KC.QUOT,
        KC.LSFT,    KC.Z,       KC.X,       KC.C,       KC.V,       KC.B,           KC.N,       KC.M,       KC.COMM,    KC.DOT,     KC.SLSH,    KC.RSFT,
                                            KC.TRNS,    KC.TRNS,    KC.TRNS,        KC.TRNS,    KC.TRNS,    KC.TRNS,
    ]
]

if __name__ == '__main__':
    keyboard.go()
