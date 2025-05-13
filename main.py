from tkinter import *
from tkinter import messagebox

debtors = []
page = 1
BUTTON_BG_COLOUR = "yellow"

class Debt:
    def __init__(self, name, amount, date, reason):
        self.name = name
        self.amount = amount
        self.date = date
        self.reason = reason

    def show_info(self):
        return f"Name: {self.name} Amount: ${self.amount} Date: {self.date} Reason: {self.reason}"
    
class GUI:
    def __init__(self, parent):
        self.parent = parent
        name = StringVar()
        amount = StringVar()
        date = StringVar()
        reason = StringVar()

        toggle_button = Button(text = "Add/View Information", command = self.toggle_frame, background=BUTTON_BG_COLOUR)
        toggle_button.pack()

        self.viewing_frame = Frame(parent)
        t1 = Label(self.viewing_frame, text="Debtors:", font="Arial")
        t1.grid(row=1, column=0)
        self.viewing_frame.pack()

        self.adding_frame = Frame(parent)
        t1 = Label(self.adding_frame, text = "Add a debtor:", font="Arial 15")
        t1.grid(row=0, column=0, sticky=W)

        name_label = Label(self.adding_frame, text="Enter the name of the debtor:")
        name_entry = Entry(self.adding_frame, textvariable=name)
        name_label.grid(row=2,column=0)
        name_entry.grid(row=2, column = 1)
        
        amount_label = Label(self.adding_frame, text = "Enter the value of the loan:")
        amount_entry = Entry(self.adding_frame, textvariable=amount)
        amount_label.grid(row=3, column=0)
        amount_entry.grid(row=3, column=1)

        date_label = Label(self.adding_frame, text = "Enter the date:")
        date_entry = Entry(self.adding_frame, textvariable=date)
        date_label.grid(row=4, column=0)
        date_entry.grid(row=4, column = 1)

        reason_label = Label(self.adding_frame, text = "Enter the reason for the loan:")
        reason_entry = Entry(self.adding_frame, textvariable=reason)
        reason_label.grid(row=5, column=0)
        reason_entry.grid(row=5, column = 1)


        confirm_button = Button(self.adding_frame, text = "Confirm", width=30, background=BUTTON_BG_COLOUR, command=lambda:self.confirm_new_data(name.get(), amount.get(), date.get(), reason.get()))
        confirm_button.grid(row=6, column = 0, columnspan=2)

        self.current_frame = self.viewing_frame
        self.current_frame.pack()


    def toggle_frame(self):
        self.show_all_data()
        if self.current_frame == self.viewing_frame:
            self.current_frame.pack_forget()
            self.current_frame = self.adding_frame
            self.current_frame.pack()
        else:
            self.current_frame.pack_forget()
            self.current_frame = self.viewing_frame
            self.current_frame.pack()

    def confirm_new_data(self, name, amount, date, reason):
        try:
            amount = int(amount)
            if name == "" or amount <= 0 or date == "" or reason == "":
                messagebox.showerror("Error", "Please fill out all fields")
            else:
                debtor = Debt(name, amount, date, reason)
                debtors.append(debtor)
        except ValueError:
            messagebox.showerror("Error", "Enter a valid loan amount")


    def show_all_data(self):
        for i, debtor in enumerate(debtors):
            label = Label(self.viewing_frame, text=debtor.show_info(), font="Arial 10")
            label.grid(row=i+1, column=0)

            resolve_button = Button(self.viewing_frame, text="Resolve", bg=BUTTON_BG_COLOUR)
            resolve_button.grid(row=i+1, column=2)

if __name__ == "__main__":
    root = Tk()
    app = GUI(root)
    root.geometry("400x200")
    root.mainloop()