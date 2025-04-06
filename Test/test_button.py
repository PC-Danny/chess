import tkinter as tk

def handle_button_click(clicked_btn):
    global active_btn

    # Deactivate previous
    if active_btn and active_btn != clicked_btn:
        active_btn.config(bg="SystemButtonFace")
        clicked_btn.config(bg="SystemButtonFace")
        active_btn = None
        return  # Don't highlight next in this case

    # Activate clicked button
    clicked_btn.config(bg="lightblue")
    active_btn = clicked_btn

    # Example logic: if Button 1 is clicked, highlight Button 3
    if clicked_btn == buttons[0]:
        highlight_button(2, color="white")  # Button 3 (index 2)
    elif clicked_btn == buttons[1]:
        highlight_button(3, color="white")  # Button 4
    # ...add more logic as needed

def highlight_button(index, color="white"):
    buttons[index].config(bg=color)

root = tk.Tk()

buttons = []
active_btn = None

for i in range(4):
    btn = tk.Button(root, text=f"Button {i+1}", width=20,
                    command=lambda b=i: handle_button_click(buttons[b]))
    btn.pack(pady=5)
    buttons.append(btn)

root.mainloop()
