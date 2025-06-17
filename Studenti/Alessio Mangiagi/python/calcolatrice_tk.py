import tkinter as tk
import math
print("><(((º> sabusabu <º)))><")


import tkinter as tk
import math

class Calcolatrice:
    def __init__(self, master):
        self.master = master
        master.title("Calcolatrice")
        master.configure(bg="#3653D1", highlightbackground="#3653D1", highlightcolor="#3653D1")
        #master.iconbitmap("Studenti\Alessio Mangiagi\icone\favicon.ico")
        master.geometry("400x500")

        self.expression = ""
        self.equation = tk.StringVar()

        for i in range(2):
            master.rowconfigure(i, weight=1)
        for j in range(2):
            master.columnconfigure(j, weight=1)

        entry = tk.Entry(master, textvariable=self.equation, font=("Arial", 20), justify="right")
        entry.grid(columnspan=4, ipadx=8, ipady=8, sticky="nsew")

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('√', 5, 0), ('x²', 5, 1), ('%', 5, 2)
        ]

        for (text, row, col) in buttons:
            if text == '=':
                action = self.equalpress
            else:
                action = lambda x=text: self.press(x)
            tk.Button(master, text=text, font=("Arial", 18), bg="#e40e1a", fg="white",
                      command=action, width=5, height=2).grid(row=row, column=col, sticky="nsew")

        tk.Button(master, text="C", font=("Arial", 18), bg="#0e19e4", fg="white",
                  command=self.clear, width=5, height=2).grid(row=5, column=3, sticky="nsew")

    def press(self, num):
        if num == "√":
            try:
                result = str(math.sqrt(float(self.expression)))
                self.equation.set(result)
                self.expression = result
            except:
                self.equation.set("Errore")
                self.expression = ""
        elif num == "x²":
            try:
                result = str(float(self.expression) ** 2)
                self.equation.set(result)
                self.expression = result
            except:
                self.equation.set("Errore")
                self.expression = ""
        elif num == "%":
            try:
                result = str(float(self.expression) / 100)
                self.equation.set(result)
                self.expression = result
            except:
                self.equation.set("Errore")
                self.expression = ""
        else:
            self.expression += str(num)
            self.equation.set(self.expression)

    def equalpress(self):
        try:
            total = str(eval(self.expression))
            self.equation.set(total)
            self.expression = ""
        except:
            self.equation.set("Errore")
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.equation.set("")

if __name__ == "__main__":
    print("><(((º> sabusabu <º)))><")
    root = tk.Tk()
    app = Calcolatrice(root)
    root.mainloop()