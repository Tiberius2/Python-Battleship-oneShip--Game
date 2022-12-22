import tkinter as tk

window = tk.Tk()

# 10x10 grid of buttons
for i in range(10):
    for j in range(10):
        btn = tk.Button(window, width=2, height=1)
        btn.grid(row=i, column=j)

# Turn red on click
def btn_click(event):
    event.widget["bg"] = "red"

# Bind the button_click function to the left mouse button
window.bind("<Button-1>", btn_click)
window.mainloop()