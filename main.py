from tkinter import *
debtors = []
page = 1

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
        toggle_button = Button(text = "Add/View Information", command = self.toggle_frame)
        toggle_button.pack()

        self.viewing_frame = Frame(parent)
        t1 = Label(self.viewing_frame, text="Debtors:", font="Arial")
        t1.grid(row=1, column=0)
        self.viewing_frame.pack()

        self.adding_frame = Frame(parent)
        t1 = Label(self.adding_frame, text = "Add a debtor:", font="Arial 15")
        t1.grid(row=0, column=0, sticky=W)

        name_label = Label(self.adding_frame, text="Enter the name of the debtor:")
        name_entry = Entry(self.adding_frame)
        name_label.grid(row=2,column=0)
        name_entry.grid(row=2, column = 1)
        
        amount_label = Label(self.adding_frame, text = "Enter the value of the loan:")
        amount_entry = Entry(self.adding_frame)
        amount_label.grid(row=3, column=0)
        amount_entry.grid(row=3, column=1)

        date_label = Label(self.adding_frame, text = "Enter the date:")
        date_entry = Entry(self.adding_frame)
        date_label.grid(row=4, column=0)
        date_entry.grid(row=4, column = 1)


        self.current_frame = self.viewing_frame
        self.current_frame.pack()

    def toggle_frame(self):
        if self.current_frame == self.viewing_frame:
            self.current_frame.pack_forget()
            self.current_frame = self.adding_frame
            self.current_frame.pack()
        else:
            self.current_frame.pack_forget()
            self.current_frame = self.viewing_frame
            self.current_frame.pack()


if __name__ == "__main__":
    root = Tk()
    app = GUI(root)
    root.mainloop()