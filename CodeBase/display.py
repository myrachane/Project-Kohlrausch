from machine import Pin, I2C
from config import I2C_SDA, I2C_SCL, I2C_FREQ, OLED_ADDR


class Display:
    def __init__(self):
        self._i2c = I2C(0, sda=Pin(I2C_SDA), scl=Pin(I2C_SCL), freq=I2C_FREQ)
        import ssd1306
        self._oled = ssd1306.SSD1306_I2C(128, 32, self._i2c, addr=OLED_ADDR)
        self._oled.fill(0)
        self._oled.show()

    def show_layer(self, layer_num, layer_name):
        self._oled.fill(0)
        self._oled.text("Kohlrausch", 0, 0)
        self._oled.text("---------------------", 0, 12)
        self._oled.text("Layer: " + str(layer_num + 1), 0, 24)
        self._oled.show()

    def show_text(self, line1="", line2="", line3=""):
        self._oled.fill(0)
        self._oled.text(line1, 0, 0)
        self._oled.text(line2, 0, 12)
        self._oled.text(line3, 0, 24)
        self._oled.show()

    def clear(self):
        self._oled.fill(0)
        self._oled.show()
