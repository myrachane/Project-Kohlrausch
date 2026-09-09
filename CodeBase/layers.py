import time
from machine import Pin
from config import LAYER_SWITCH_PIN, NUM_LAYERS, DEFAULT_LAYER, LAYER_SWITCH_DEBOUNCE_MS, LAYER_NAMES


class LayerManager:
    def __init__(self):
        self._pin = Pin(LAYER_SWITCH_PIN, Pin.IN, Pin.PULL_UP)
        self._layer = DEFAULT_LAYER
        self._last_state = self._pin.value()
        self._last_time = time.ticks_ms()

    def update(self):
        current = self._pin.value()
        now = time.ticks_ms()
        if current != self._last_state:
            if time.ticks_diff(now, self._last_time) >= LAYER_SWITCH_DEBOUNCE_MS:
                self._last_time = now
                self._last_state = current
                if current == 0:
                    self._layer = (self._layer + 1) % NUM_LAYERS
                    return True
        return False

    @property
    def current(self):
        return self._layer

    @property
    def name(self):
        return LAYER_NAMES[self._layer]

    def set_layer(self, layer):
        if 0 <= layer < NUM_LAYERS:
            self._layer = layer
