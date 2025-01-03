import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Simple Hiragana")

# Set a font that supports Hiragana characters
hiragana_font = ("Noto Sans CJK", 20)

# Example Hiragana string
hiragana_text = "あいうえお 4564"

# Create a label to display the Hiragana text
label = tk.Label(root, text=hiragana_text, font=hiragana_font)
label.pack()

root.mainloop()
