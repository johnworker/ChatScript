import tkinter as tk
from dialog_generator import generate_dialog
import pyperclip

def generate():
    category = category_var.get()
    dialog = generate_dialog(category)
    result_text.set("\n".join(dialog))

def copy_to_clipboard():
    pyperclip.copy(result_text.get())

# 創建主視窗
root = tk.Tk()
root.title("ChatScript - AI 對話生成器")
root.geometry("400x300")

# 選擇對話類型
category_var = tk.StringVar(value="幽默")
category_label = tk.Label(root, text="選擇對話風格：")
category_label.pack()
category_menu = tk.OptionMenu(root, category_var, "幽默", "正式", "人生勵志")
category_menu.pack()

# 顯示結果
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, wraplength=350, justify="left")
result_label.pack()

# 按鈕
generate_button = tk.Button(root, text="生成對話", command=generate)
generate_button.pack()

copy_button = tk.Button(root, text="複製對話", command=copy_to_clipboard)
copy_button.pack()

root.mainloop()
