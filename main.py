from tkinter import *
debtors = []

class Debt:
    def __init__(self, name, amount, date, reason):
        self.name = name
        self.amount = amount
        self.date = date
        self.reason = reason

    def get_details(self):
        return f"{self.name}: ${self.amount}, {self.date}, {self.reason}"
    
    
class GUI:
    def __init__(self, parent):
        self.parent = parent
        main_page = Frame(root)
        t1 = Label(text="Debtor:")
        for i in range(len(debtors)):
            debtor = Label(main_page, text = "f{}")
            debt = Label()

        

if __name__ == "__main__":
    root = Tk()
    app = GUI(root)
    root.mainloop()