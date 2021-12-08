from tkinter import*


class calculator:
    def __init__(self, root):

        self.f = Frame(root, height=500, width=500, bg="#00ff99")
        self.f.propagate(0)
        self.f.pack()

        self.h = Label(self.f, text="PROFIT CALCULATIOR",
                       font=("Ariel", 20), bg="#3399ff")
        self.h.pack(fill=X)
        self.label1 = Label(self.f, text="Enter your C.P-->>",
                            font=("Ariel", 10), bg="#00ff00")
        self.label2 = Label(self.f, text="Enter your S.P-->>",
                            font=("Ariel", 10), bg="#00ff00")
        self.values = StringVar()
        self.values1 = StringVar()
        self.e = Entry(self.f, textvariable=self.values, bg="#00ffff")
        self.e1 = Entry(self.f, textvariable=self.values1, bg="#00ffff")
        self.label1.place(x=100, y=100)
        self.label2.place(x=100, y=200)
        self.e.place(x=300, y=100)
        self.e1.place(x=300, y=200)
        # self.label1.place(x=100,y=100)
        self.b = Button(self.f, text="show", width=15,
                        height=2, command=lambda: self.calculates(), bg="#ff00aa")
        self.b.place(x=350, y=300)

    def calculates(self):
        self.cost_price = int(self.values.get())
        self.selling_price = int(self.values1.get())
        self.profit = (self.selling_price-self.cost_price)
        self.string_profit = str(self.profit)
        self.profitper = ((self.profit/self.cost_price)*100)
        self.profitp1 = str(self.profitper)
        self.text = "your profit is-->>"+self.string_profit
        self.text2 = "your profit percentage is-->"+self.profitp1+"%"
        self.label3 = Label(self.f, text=self.text, bg="#ffff00")
        self.label4 = Label(self.f, text=self.text2, bg="#ffff00")
        self.label3.place(x=100, y=400)
        self.label4.place(x=100, y=430)


root = Tk()
root.title("profit calculator")
b = calculator(root)
root.mainloop()
