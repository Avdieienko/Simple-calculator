import tkinter as tk

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculator")

        self.root.geometry("300x500")

        self.heading = tk.Label(self.root, text = "Calculator", font = ("Arial",18))
        self.heading.pack(padx=10,pady=10)

        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(anchor = "w", padx = 10)

        self.result = ""

        self.label = tk.Label(self.input_frame, text = "0",font = ("Arial",13))
        self.label.pack(side="left")

        self.numbers_frame = tk.Frame(self.root)
        self.numbers_frame.columnconfigure(0, weight=1)
        self.numbers_frame.columnconfigure(1, weight=1)
        self.numbers_frame.columnconfigure(2, weight=1)
        self.numbers_frame.columnconfigure(3, weight=1)
        self.numbers_frame.pack(fill="x", pady=30)

        self.btn_del = tk.Button(self.numbers_frame, text="AC", font=("Arial", 15),
                              command=self.clean)
        self.btn_del.grid(row=0, column=2, sticky=tk.W + tk.E)

        self.btn_div = tk.Button(self.numbers_frame, text="/", font=("Arial", 15),
                              command=lambda: self.add_to_calculations("/"))
        self.btn_div.grid(row=0, column=3, sticky=tk.W + tk.E)

        self.btn7 = tk.Button(self.numbers_frame, text="7", font=("Arial", 15),
                              command=lambda:self.add_to_calculations("7"))
        self.btn7.grid(row=1,column=0, sticky = tk.W+tk.E)

        self.btn8 = tk.Button(self.numbers_frame, text="8", font=("Arial", 15),
                              command=lambda:self.add_to_calculations("8"))
        self.btn8.grid(row=1, column=1, sticky=tk.W+tk.E)

        self.btn9 = tk.Button(self.numbers_frame, text="9", font=("Arial", 15),
                              command=lambda:self.add_to_calculations("9"))
        self.btn9.grid(row=1, column=2, sticky=tk.W+tk.E)

        self.btn_mult = tk.Button(self.numbers_frame, text="X", font=("Arial", 15),
                                  command=lambda:self.add_to_calculations("*"))
        self.btn_mult.grid(row=1, column=3, sticky=tk.W+tk.E)

        self.btn4 = tk.Button(self.numbers_frame, text="4", font=("Arial", 15),
                              command=lambda:self.add_to_calculations("4"))
        self.btn4.grid(row=2, column=0, sticky=tk.W+tk.E)

        self.btn5 = tk.Button(self.numbers_frame, text="5", font=("Arial", 15),
                              command=lambda:self.add_to_calculations("5"))
        self.btn5.grid(row=2, column=1, sticky=tk.W+tk.E)

        self.btn6 = tk.Button(self.numbers_frame, text="6", font=("Arial", 15),
                              command=lambda:self.add_to_calculations("6"))
        self.btn6.grid(row=2, column=2, sticky=tk.W+tk.E)

        self.btn_sub = tk.Button(self.numbers_frame, text="-", font=("Arial", 15),
                                 command=lambda:self.add_to_calculations("-"))
        self.btn_sub.grid(row=2, column=3, sticky=tk.W+tk.E)

        self.btn1 = tk.Button(self.numbers_frame, text="1", font=("Arial", 15),
                              command=lambda:self.add_to_calculations("1"))
        self.btn1.grid(row=3, column=0, sticky=tk.W+tk.E)

        self.btn2 = tk.Button(self.numbers_frame, text="2", font=("Arial", 15),
                              command=lambda:self.add_to_calculations("2"))
        self.btn2.grid(row=3, column=1, sticky=tk.W+tk.E)

        self.btn3 = tk.Button(self.numbers_frame, text="3", font=("Arial", 15),
                              command=lambda:self.add_to_calculations("3"))
        self.btn3.grid(row=3, column=2, sticky=tk.W+tk.E)

        self.btn_add = tk.Button(self.numbers_frame, text="+", font=("Arial", 15),
                                 command=lambda:self.add_to_calculations("+"))
        self.btn_add.grid(row=3, column=3, sticky=tk.W+tk.E)

        self.btn_clear = tk.Button(self.numbers_frame, text="DEL", font=("Arial", 15), command = self.del_prev)
        self.btn_clear.grid(row=4, column=0, sticky=tk.W+tk.E)

        self.btn0 = tk.Button(self.numbers_frame, text="0", font=("Arial", 15),
                              command=lambda: self.add_to_calculations("0"))
        self.btn0.grid(row=4, column=1, sticky=tk.W+tk.E)

        self.btn_dot = tk.Button(self.numbers_frame, text=".", font=("Arial", 15),
                                 command=lambda:self.add_to_calculations("."))
        self.btn_dot.grid(row=4, column=2, sticky=tk.W+tk.E)

        self.btn_equal = tk.Button(self.numbers_frame, text="=", font=("Arial", 15), command=self.calculations)
        self.btn_equal.grid(row=4, column=3, sticky=tk.W+tk.E)
        self.root.mainloop()

    def add_to_calculations(self, symbol):
        if len(self.result) == 0 and symbol == ".":
            symbol = "0"+symbol
        self.result += symbol
        self.label.config(text=self.result)
    def calculations(self):
        try:
            self.result = str(eval(self.result))
            self.label.config(text=self.result)
        except:
            self.label.config(text="Error")
            self.result = ""

    def clean(self):
        self.label.config(text="0")
        self.result = ""
    def del_prev(self):
        self.result = self.result[:-1]
        if len(self.result) == 0:
            self.label.config(text="0")
        else:
            self.label.config(text=self.result)

GUI()