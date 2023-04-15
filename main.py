import tkinter as tk
from q_codes import qc

user_input = "Q"
instruction = "Q-Lookup\nA utility to help with those crazy Q Codes.\nby KI5WWP\n\n"
instruction += "Start typing the Q-code (the Q is already there)\n\n"
instruction += "KEYS:\n<BACKSPACE> --- backspaces\n<ESC> --- Clears all input - start again"
instruction += "\n<ALT>+<F4> --- Exit the program"
out_text = instruction

def update_output():
    global out_text
    out_text = user_input
    out_label.config(text= out_text)
    out_label.pack()

def keyup(e):
    # https://stackoverflow.com/questions/27215326/tkinter-keypress-and-keyrelease-events
    # used key release event, press event doesn't matter... don't want to catch key repeat
    global user_input
    global out_text
    if e.keysym == "BackSpace" and len(user_input)>1:
        user_input = user_input[:-1]
        update_output()
    elif e.keysym == "Escape":
        user_input = "Q"
        out_label.config(text = instruction)
        out_label.pack()
    
    else:
        if len(user_input) <3:
            user_input += e.char.upper()
            update_output()
    in_label.config(text=user_input, font=('Arial', 50))


root = tk.Tk()
root.title("Q-Lookup by KI5WWP")
in_frame = tk.Frame(root, width = 300, height = 45)
#out_frame = tk.Frame(root, width=300, height=300)
in_label = tk.Label(in_frame, text = user_input, font=('Arial', 50), highlightbackground="blue", highlightthickness=3)
out_label = tk.Label(in_frame, text = out_text)
in_label.pack()
out_label.pack()

#frame.bind("<KeyPress>", keydown)
in_frame.bind("<KeyRelease>", keyup)

in_frame.pack()
#out_frame.pack()

in_frame.focus_set()
root.mainloop()