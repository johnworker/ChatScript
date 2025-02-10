import json
import random
import time
import sys

def load_dialogs():
    """讀取對話 JSON 檔案"""
    with open("dialogs.json", "r", encoding="utf-8") as file:
        return json.load(file)

def generate_dialog(category="幽默"):
    """隨機選擇對話類別，並返回一組對話"""
    dialogs = load_dialogs()
    if category in dialogs:
        return random.choice(dialogs[category])
    return ["對不起，沒有這類型的對話。"]

def display_dialog(dialog):
    """依序顯示對話（字幕效果）"""
    for line in dialog:
        print(line)
        sys.stdout.flush()  # 立刻輸出，確保不會卡住
        time.sleep(1)  # 延遲 1 秒，模擬字幕顯示效果

if __name__ == "__main__":
    print("=== AI 自動對話生成器 ===")
    print("請選擇對話類型：幽默 / 正式 / 人生勵志")
    category = input("輸入對話類型: ").strip()

    print("\n正在生成對話...\n")
    dialog = generate_dialog(category)
    display_dialog(dialog)

    print("\n=== 對話結束 ===")
