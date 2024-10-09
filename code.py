# Write your code here :-)
print("Starting")

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.handlers.sequences import send_string
from kmk.handlers.sequences import simple_key_sequence
from kmk.modules.holdtap import HoldTap
from kmk.modules.sticky_mod import StickyMod
from kmk.modules.combos import Combos, Chord
from kmk.modules.mouse_keys import MouseKeys

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())
keyboard.modules.append(HoldTap())
keyboard.modules.append(StickyMod())
keyboard.modules.append(Combos())

keyboard.col_pins = (board.GP1, board.GP2, board.GP5, board.GP7, board.GP28, board.GP27,
                     board.GP21, board.GP17, board.GP9, board.GP10, board.GP13, board.GP15)
keyboard.row_pins = (board.GP0, board.GP16, board.GP18, board.GP20, board.GP22)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# operators and keywords
NEQ  = send_string('!=')
PTR  = send_string('->')
RETN = send_string('return ')
LAM  = send_string('lambda ')

BRAND = send_string('Sweet Spot Keyboard')

# provided using an IDE or a powerful text editor as vscode that features code completion
# key sequences
key_sequences = {
    'newline':          simple_key_sequence((KC.END, KC.ENT)),                  # moving the cursor to the end then enter
    'statement_c':      simple_key_sequence((KC.END, KC.SCLN, KC.ENT)),         # making current line a C statement, also valid in C++, Java and C#
    'block_c':          simple_key_sequence((KC.END, KC.ENT, KC.LCBR, KC.ENT)), # C style syntactic code block
    'block_java':       simple_key_sequence((KC.END, KC.SPC, KC.LCBR, KC.ENT)), # Java style syntactic code block
    'block_python':     simple_key_sequence((KC.END, KC.COLN, KC.ENT)),         # Python syntactic code block
    'vscode_shortcuts': simple_key_sequence((KC.LCTL(KC.K), KC.LCTL(KC.S))),    # control-k, control-s,
}

# layer modifiers and holdtap keys
SPC_L1 = KC.LT(1, KC.SPC, prefer_hold=False)    # space when tapped, layer1 when held
ESC_L2 = KC.LT(2, KC.ESC, prefer_hold=False)    # esc when tapped, layer2 when held
TAB_L2 = KC.LT(2, KC.TAB, prefer_hold=False)    # tab when tapped, layer2 when held

E_SFT = KC.HT(KC.E, KC.LSFT, prefer_hold=False) # e when tapped, left shift when held
I_SFT = KC.HT(KC.I, KC.RSFT, prefer_hold=False) # i when tapped, right shift when held

F_CTL = KC.HT(KC.F, KC.LCTL, prefer_hold=False) # f when tapped, left control when held
J_CTL = KC.HT(KC.J, KC.RCTL, prefer_hold=False) # j when tapped, right control when held

W_ALT = KC.HT(KC.W, KC.LALT, prefer_hold=False) # w when tapped, left alt when held
O_ALT = KC.HT(KC.O, KC.RALT, prefer_hold=False) # o when tapped, right alt when held

A_WIN = KC.HT(KC.A, KC.LWIN, prefer_hold=False)  # a when tapped, left win when held
SC_WIN = KC.HT(KC.SCLN, KC.RWIN, prefer_hold=False) # ; when tapped, right win when held

SW = KC.SM(kc=KC.TAB, mod=KC.LALT)  # switch between windows, same as alt held then tapping tab

BLOCK = key_sequences['block_python'] # syntactic code block in layer0

combos.combos = [
    # format: Chord((key1, key2), key_sequence),
    # note: key1 and key2 must be in the keyboard.keymap below
    Chord((K_L3, KC.S), key_sequences['vscode_shortcuts']),  # tapping k and s simultaneously implements corresponding key sequence

]

_______ = KC.NO

keyboard.keymap = [
    # layer0
    [BRAND,   KC.GRV,  BLOCK,   KC.ENT,  KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.LPRN, KC.EQL,  KC.MINS, KC.BSLS,
     KC.TAB,  KC.Q,    W_ALT,   E_SFT,   KC.R,    KC.T,    KC.Y,    KC.U,    I_SFT,   O_ALT,   KC.P,    KC.BSPC,
     KC.CAPS, A_WIN,   KC.S,    KC.D,    F_CTL,   KC.G,    KC.H,    J_CTL,   KC.K,    KC.L,    SC_WIN,  KC.QUOT,
     KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, _______,
     _______, KC.DEL,  KC.LCTL, ESC_L2,  SPC_L1,  _______, SPC_L1,  TAB_L2,  KC.RWIN, KC.INS,  _______, _______,],

    # layer1
    [KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.F5,   KC.F6,   KC.F7,   KC.F8,   KC.RPRN, KC.NO,   KC.NO,   KC.NO,
     SW,      KC.NO,   KC.NO,   KC.UP,   KC.LCBR, KC.NO,   KC.PERC, KC.CIRC, KC.AMPR, KC.ASTR, PTR,     KC.DEL,
     KC.NO,   KC.NO,   KC.LEFT, KC.DOWN, KC.RGHT, KC.LBRC, NEQ,     KC.EXLM, KC.AT,   KC.HASH, KC.DLR,  KC.NO,
     KC.LALT, KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   _______,
     _______, KC.NO,   KC.NO,   KC.NO,   KC.NO,   _______, KC.NO,   KC.NO,   KC.NO,   KC.NO,   _______, _______,],

    # layer2
    [KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.F9,   KC.F10,  KC.F11,  KC.F12,  KC.NO,   KC.NO,   KC.NO,   KC.NO,
     SW,      KC.NO,   KC.NO,   KC.PGUP, KC.RCBR, KC.NO,   KC.N5,   KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.NO,
     KC.NO,   KC.NO,   KC.HOME, KC.PGDN, KC.END,  KC.RBRC, KC.N0,   KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.NO,
     KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   _______,
     _______, KC.NO,   KC.NO,   KC.NO,   KC.NO,   _______, KC.NO,   KC.NO,   KC.NO,   KC.NO,   _______, _______,],

     # layer3
    [KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,
     KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,
     KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,
     KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   KC.NO,   _______,
     _______, KC.NO,   KC.NO,   KC.NO,   KC.NO,   _______, KC.NO,   KC.NO,   KC.NO,   KC.NO,   _______, _______,]
]

if __name__ == '__main__':
    keyboard.go()
