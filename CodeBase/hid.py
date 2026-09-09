import time
import usb.device
from usb.device.keyboard import KeyboardInterface, KeyCode
from config import HID_INIT_DELAY_S, HID_MAX_KEYS_PER_REPORT


class HIDKeyboard:
    def __init__(self):
        self._kb = KeyboardInterface()
        usb.device.get().init(self._kb, builtin_driver=True)
        time.sleep(HID_INIT_DELAY_S)

    def send(self, keycodes):
        if not keycodes:
            return
        for i in range(0, len(keycodes), HID_MAX_KEYS_PER_REPORT):
            chunk = keycodes[i:i + HID_MAX_KEYS_PER_REPORT]
            self._kb.send_keys(chunk)
            time.sleep_ms(10)
        self._kb.send_keys([])

    def release(self):
        self._kb.send_keys([])
