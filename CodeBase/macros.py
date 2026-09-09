import json
from config import NUM_LAYERS, NUM_ROWS, NUM_COLS, LAYER_KEYMAP, MACRO_FILE


class MacroEngine:
    def __init__(self):
        self._layers = []
        for _ in range(NUM_LAYERS):
            layer = {}
            for r in range(NUM_ROWS):
                for c in range(NUM_COLS):
                    key = str(r) + "," + str(c)
                    layer[key] = LAYER_KEYMAP.get((r, c), [])
            self._layers.append(layer)

    def get_macro(self, layer, row, col):
        if 0 <= layer < len(self._layers):
            key = str(row) + "," + str(col)
            return self._layers[layer].get(key, [])
        return []

    def set_macro(self, layer, row, col, keycodes):
        if 0 <= layer < len(self._layers):
            key = str(row) + "," + str(col)
            self._layers[layer][key] = list(keycodes)

    def to_dict(self):
        return {"layers": self._layers}

    def from_dict(self, data):
        if "layers" in data:
            self._layers = data["layers"]

    def save(self):
        try:
            with open(MACRO_FILE, "w") as f:
                json.dump(self.to_dict(), f)
            return True
        except Exception:
            return False

    def load(self):
        try:
            with open(MACRO_FILE, "r") as f:
                self.from_dict(json.load(f))
            return True
        except Exception:
            return False
