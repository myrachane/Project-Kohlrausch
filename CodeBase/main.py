import time
import gc
from config import SCAN_INTERVAL_MS, HID_INIT_DELAY_S

gc.collect()

print("STATUS:booting")

from scanner import Scanner
from display import Display
from layers import LayerManager
from macros import MacroEngine
from storage import SerialProtocol

gc.collect()

scanner = Scanner()
display = Display()
layers = LayerManager()
macros = MacroEngine()
protocol = SerialProtocol(macros)

gc.collect()

print("STATUS:loading_macros")

if macros.load():
    display.show_text("Kohlrausch", "", "Macros loaded")
else:
    display.show_text("Kohlrausch", "", "Default macros")

time.sleep(1)

print("STATUS:init_hid")

display.show_text("Kohlrausch", "", "Init USB HID...")

from hid import HIDKeyboard

hid = HIDKeyboard()

display.show_layer(layers.current, layers.name)
print("STATUS:ready")

while True:
    layer_changed = layers.update()
    if layer_changed:
        display.show_layer(layers.current, layers.name)
        print("STATUS:layer_" + str(layers.current + 1))

    keys = scanner.scan()
    for row, col in keys:
        macro = macros.get_macro(layers.current, row, col)
        if macro:
            hid.send(macro)

    cmd = protocol.poll()
    if cmd:
        print("RESULT:" + cmd)

    gc.collect()
    time.sleep_ms(SCAN_INTERVAL_MS)
