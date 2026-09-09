# Kohlrausch

3x3 macropad firmware for RP2040, written in MicroPython.

## Hardware

| Component | Details |
|-----------|---------|
| MCU | RP2040 |
| Matrix | 3x3 with 1N4148 diodes (COL > SW > \| > ROW) |
| GPIO | GP0-2 = COL1-3, GP3-5 = ROW1-3 |
| Layer Switch | GP10 (other side to GND) |
| OLED | 0.91" SSD1306 I2C (SDA=GP26, SCL=GP27) |

## Setup

### 1. Flash MicroPython

Flash MicroPython v1.24+ to your RP2040 board.

### 2. Install HID package

```bash
mpremote mip install usb-device-keyboard
```

### 3. Upload firmware

```bash
mpremote fs cp config.py :config.py
mpremote fs cp scanner.py :scanner.py
mpremote fs cp display.py :display.py
mpremote fs cp layers.py :layers.py
mpremote fs cp hid.py :hid.py
mpremote fs cp macros.py :macros.py
mpremote fs cp storage.py :storage.py
mpremote fs cp main.py :main.py
```

### 4. Run

```bash
mpremote run main.py
```

Or set auto-start by uploading `main.py` (it will run on boot).

## Files

| File | Description |
|------|-------------|
| `config.py` | Pin definitions, constants |
| `scanner.py` | 3x3 matrix scanner with debounce |
| `display.py` | SSD1306 OLED display driver |
| `layers.py` | Layer state machine (4 layers) |
| `hid.py` | USB HID keyboard (usb-device-keyboard) |
| `macros.py` | Macro engine, key-to-macro mapping |
| `storage.py` | Serial protocol for CLI communication |
| `main.py` | Main loop |

## Default Key Mappings

| Key | Macro |
|-----|-------|
| (0,0) | A |
| (0,1) | B |
| (0,2) | C |
| (1,0) | D |
| (1,1) | E |
| (1,2) | F |
| (2,0) | G |
| (2,1) | H |
| (2,2) | I |

## Serial Protocol (for emtypyie-cli)

JSON over USB serial (115200 baud):

| Command | Response |
|---------|----------|
| `{"cmd":"PING"}` | `{"status":"ok","name":"Kohlrausch","layers":4}` |
| `{"cmd":"GET_LAYERS"}` | `{"layers":[{"id":1,"name":"Default"},...]}` |
| `{"cmd":"GET_KEY","layer":1,"row":0,"col":0}` | `{"layer":1,"row":0,"col":0,"macro":[65]}` |
| `{"cmd":"SET_KEY","layer":1,"row":0,"col":0,"macro":[65]}` | `{"status":"ok"}` |
| `{"cmd":"REBOOT"}` | Device reboots |

## License

MIT
