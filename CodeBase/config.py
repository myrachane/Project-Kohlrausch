from machine import Pin

NAME = "Kohlrausch"

COL_PINS = [0, 1, 2]
ROW_PINS = [3, 4, 5]

NUM_COLS = len(COL_PINS)
NUM_ROWS = len(ROW_PINS)

LAYER_SWITCH_PIN = 10

I2C_SDA = 26
I2C_SCL = 27
I2C_FREQ = 100000
OLED_ADDR = 0x3C

NUM_LAYERS = 4
DEFAULT_LAYER = 0

DEBOUNCE_MS = 20
LAYER_SWITCH_DEBOUNCE_MS = 300

SCAN_INTERVAL_MS = 5

MACRO_FILE = "/macros.json"

HID_INIT_DELAY_S = 1

HID_MAX_KEYS_PER_REPORT = 3

LAYER_NAMES = [
    "Default",
    "Media",
    "Tools",
    "Custom",
]

LAYER_KEYMAP = {
    (0, 0): [65],
    (0, 1): [66],
    (0, 2): [67],
    (1, 0): [68],
    (1, 1): [69],
    (1, 2): [70],
    (2, 0): [71],
    (2, 1): [72],
    (2, 2): [73],
}
