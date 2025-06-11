"""
Esempio 10: Uso del focus per rilevare eventi
Esempio 11: Differenze tra command e bind()
"""
import tkinter as tk

def on_focus_in(event):
    entry.config(bg="yellow")

def on_focus_out(event):
    entry.config(bg="white")

def on_button():
    label.config(text="Pulsante premuto (command)")

def on_button_bind(event):
    label.config(text="Pulsante premuto (bind)")

root = tk.Tk()
root.title("Esempio focus e differenze eventi")

entry = tk.Entry(root)
entry.pack(padx=10, pady=10)
entry.bind("<FocusIn>", on_focus_in)
entry.bind("<FocusOut>", on_focus_out)

button = tk.Button(root, text="Premi me", command=on_button)
button.pack(padx=10, pady=10)
button.bind("<Button-1>", on_button_bind)

label = tk.Label(root, text="")
label.pack(padx=10, pady=10)

root.mainloop()
