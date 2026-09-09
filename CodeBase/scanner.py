import time
from machine import Pin
from config import COL_PINS, ROW_PINS, NUM_COLS, NUM_ROWS, DEBOUNCE_MS


class Scanner:
    def __init__(self):
        self._row_pins = [Pin(p, Pin.OUT, value=0) for p in ROW_PINS]
        self._col_pins = [Pin(p, Pin.IN, Pin.PULL_UP) for p in COL_PINS]
        self._debounce = [[0] * NUM_COLS for _ in range(NUM_ROWS)]
        self._state = [[False] * NUM_COLS for _ in range(NUM_ROWS)]

    def scan(self):
        pressed = []
        now = time.ticks_ms()
        for r in range(NUM_ROWS):
            self._row_pins[r].value(0)
            for c in range(NUM_COLS):
                held = self._col_pins[c].value() == 0
                if held and self._state[r][c] is False:
                    if time.ticks_diff(now, self._debounce[r][c]) >= DEBOUNCE_MS:
                        self._state[r][c] = True
                        self._debounce[r][c] = now
                        pressed.append((r, c))
                elif not held and self._state[r][c] is True:
                    self._state[r][c] = False
                    self._debounce[r][c] = now
            self._row_pins[r].value(1)
        return pressed
