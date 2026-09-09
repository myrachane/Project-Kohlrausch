import json
import sys
from config import NAME, NUM_LAYERS, NUM_ROWS, NUM_COLS, LAYER_NAMES


class SerialProtocol:
    def __init__(self, macros):
        self._macros = macros
        self._buf = ""

    def poll(self):
        try:
            data = sys.stdin.read(1)
            if data == "\n":
                line = self._buf.strip()
                self._buf = ""
                if line:
                    return self._handle(line)
        except TypeError:
            pass
        return None

    def _handle(self, line):
        try:
            cmd = json.loads(line)
        except ValueError:
            return json.dumps({"error": "invalid_json"})

        action = cmd.get("cmd", "")

        if action == "PING":
            return json.dumps({"status": "ok", "name": NAME, "layers": NUM_LAYERS})

        elif action == "GET_LAYERS":
            layers = []
            for i in range(NUM_LAYERS):
                layers.append({"id": i + 1, "name": LAYER_NAMES[i]})
            return json.dumps({"layers": layers})

        elif action == "GET_KEY":
            layer = cmd.get("layer", 1) - 1
            row = cmd.get("row", 0)
            col = cmd.get("col", 0)
            macro = self._macros.get_macro(layer, row, col)
            return json.dumps({
                "layer": layer + 1,
                "row": row,
                "col": col,
                "macro": macro,
            })

        elif action == "SET_KEY":
            layer = cmd.get("layer", 1) - 1
            row = cmd.get("row", 0)
            col = cmd.get("col", 0)
            macro = cmd.get("macro", [])
            self._macros.set_macro(layer, row, col, macro)
            self._macros.save()
            return json.dumps({"status": "ok"})

        elif action == "SET_LAYER_NAME":
            layer = cmd.get("layer", 1) - 1
            name = cmd.get("name", "")
            if 0 <= layer < NUM_LAYERS:
                LAYER_NAMES[layer] = name
                return json.dumps({"status": "ok"})
            return json.dumps({"error": "invalid_layer"})

        elif action == "REBOOT":
            import machine
            machine.reset()
            return json.dumps({"status": "rebooting"})

        return json.dumps({"error": "unknown_cmd"})
