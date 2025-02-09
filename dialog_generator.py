import json
import random

def load_dialogs():
    with open("dialogs.json", "r", encoding="utf-8") as file:
        return json.load(file)

def generate_dialog(category="幽默"):
    dialogs = load_dialogs()
    if category in dialogs:
        return random.choice(dialogs[category])
    return ["對不起，沒有這類型的對話。"]
dialog = generate_dialog(category="人生勵志")
