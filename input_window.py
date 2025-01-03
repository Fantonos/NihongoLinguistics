import tkinter as tk
from genorate_prompt import *
import constants 

def on_submit():
    constants.user_answer = entry.get()
    entry.delete(0, tk.END)
    if str(constants.user_answer).lower() == str(constants.final_prompt[1]):
        constants.game_score += 1
        if constants.game_score > constants.game_high_score:
            constants.game_high_score = constants.game_score
        change_prompt()
    else:
        constants.game_score = 0
        constants.game_label = f'High Score: {constants.game_high_score}                                      "{constants.final_prompt[1]}"                                      Score: {constants.game_score}'
        game_label.config(text=constants.game_label, bg="#dd2000")
    return 

def change_prompt():
        constants.final_prompt = generate_question()
        constants.game_label = f'High Score: {constants.game_high_score}                                                                             Score: {constants.game_score}'
        label.config(text=constants.final_prompt[0])
        game_label.config(text=constants.game_label, bg="lightblue")
        
    
def on_enter_key(event):
    on_submit()

# Create the main window
root = tk.Tk()
root.title("Nihongo Linguistics")

# Create a label
game_label = tk.Label(root, text=constants.game_label, font=("Arial", 13))
label = tk.Label(root, text=constants.final_prompt[0], font=("Arial", 23))
game_label.config(width=70, bg="lightblue")
game_label.pack(pady=0)
label.config(width=50, height=3, bg="lightblue")  # in pixels
label.pack(pady=0)

# Create an entry widget (text input box)
entry = tk.Entry(root, width=40, font=("Arial", 16))
entry.pack(pady=5)

# Bind the Enter key to the on_submit function
entry.bind("<Return>", on_enter_key)
entry.bind("<KP_Enter>", on_enter_key)

# Create a button to submit the input
sub_button = tk.Button(root, text="Submit", command=on_submit, width=40, height=2)
cng_button = tk.Button(root, text="Change", command=change_prompt, width=45, height=2)
sub_button.pack(side="left", pady=0)
cng_button.pack(pady=0,)

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the size of the window and calculate the position
window_width = 600
window_height = 210
x_pos = (screen_width - window_width) // 2 + 2000
y_pos = (screen_height - window_height) // 2

# Set the position of the window
root.resizable(False, False)
root.geometry(f'{window_width}x{window_height}+{x_pos}+{y_pos}')
