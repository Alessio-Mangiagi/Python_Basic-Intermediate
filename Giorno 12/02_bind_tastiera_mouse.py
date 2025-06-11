"""
Esempio 4: Il metodo bind() per associare eventi
Esempio 5: Eventi da tastiera: <KeyPress>, <Return>
Esempio 6: Eventi da mouse: <Button-1>, <Double-Button-1>
"""
import tkinter as tk

def on_key(event):
    print(f"Tasto premuto: {event.keysym}")

def on_click(event):
    print(f"Click con il mouse alle coordinate: {event.x}, {event.y}")

root = tk.Tk()
root.title("Esempio bind eventi")

entry = tk.Entry(root)
entry.pack(padx=10, pady=10)
entry.bind("<KeyPress>", on_key)
entry.bind("<Return>", lambda e: print("Invio premuto!"))

root.bind("<Button-1>", on_click)
root.bind("<Double-Button-1>", lambda e: print("Doppio click!"))

root.mainloop()
