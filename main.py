"""GUI that keeps track of debts."""

from tkinter import *
from tkinter import messagebox

# Sets up the lists and constants
debtors = []
labels = []
buttons = []
BUTTON_BG_COLOUR = "yellow"

# This class is the support class to the GUI. It has several instance variables including name, amount, date, and reason.
# These all store information about different debts.


class Debt:
    """
    Stores information for debts.

    ...
    Instance Variables:
    ------------------
    name : str
        name of the debtor
    amount : float
        the value of the loan
    date : str
        the date the loan was given out
    reason : str
        the reason for the loan

    Methods
    -------
    show_info():
        Returns all the data in a formatted string.
    """

    def __init__(self, name, amount, date, reason):
        """Create the instance variables for the Debt class."""
        self.name = name
        self.amount = amount
        self.date = date
        self.reason = reason

    def show_info(self):
        """Return all the data in a formatted string."""
        # This method is used to return a formatted version of the object's data.
        return f"Name: {self.name} Amount: ${self.amount} Date: {self.date} Reason: {self.reason}"


class GUI:
    """
    Main GUI class.

    Methods:
    --------
    toggle_frame():
        Switch between frames

    confirm_new_data():
        Confirm newly inputted data and save it to the list of debtors.

    show_all_data():
        Packs multiple labels and buttons containing debt information through iteration.

    resolve_debt():
        Deletes a debt from the system.
    """

    def __init__(self, parent):
        """Create most GUI widgets."""
        # This initial method builds most if not all the widgets in the GUI.

        # Defines instance variables, and sets the StringVars for the entry widgets:
        self.parent = parent
        name = StringVar()
        amount = StringVar()
        date = StringVar()
        reason = StringVar()

        # Toggle button
        toggle_button = Button(text="Add/View Information", command=self.toggle_frame, background=BUTTON_BG_COLOUR)
        toggle_button.pack()

        # Sets the frames up along with the corresponding titles.
        self.viewing_frame = Frame(parent)
        t1 = Label(self.viewing_frame, text="Debtors:", font="Arial")
        t1.grid(row=1, column=0)
        self.viewing_frame.pack()

        self.adding_frame = Frame(parent)
        t1 = Label(self.adding_frame, text="Add a debtor:", font="Arial 15")
        t1.grid(row=0, column=0, sticky=W)

        # These labels and entries are where the user inputs information.
        name_label = Label(self.adding_frame, text="Enter the name of the debtor:")
        name_entry = Entry(self.adding_frame, textvariable=name)
        name_label.grid(row=2, column=0)
        name_entry.grid(row=2, column=1)

        amount_label = Label(self.adding_frame, text="Enter the value of the loan:")
        amount_entry = Entry(self.adding_frame, textvariable=amount)
        amount_label.grid(row=3, column=0)
        amount_entry.grid(row=3, column=1)

        date_label = Label(self.adding_frame, text="Enter the date:")
        date_entry = Entry(self.adding_frame, textvariable=date)
        date_label.grid(row=4, column=0)
        date_entry.grid(row=4, column=1)

        reason_label = Label(self.adding_frame, text="Enter the reason for the loan:")
        reason_entry = Entry(self.adding_frame, textvariable=reason)
        reason_label.grid(row=5, column=0)
        reason_entry.grid(row=5, column=1)

        # The confirm button calls the method confirm_new_data and passes in the user input from the entry widgets using lambda.
        confirm_button = Button(self.adding_frame, text="Confirm", width=30, background=BUTTON_BG_COLOUR, command=lambda: self.confirm_new_data(name.get(), amount.get(), date.get(), reason.get()))
        confirm_button.grid(row=6, column=0, columnspan=2)

        self.current_frame = self.viewing_frame
        self.current_frame.pack()

    def toggle_frame(self):
        """Switch between frames."""
        # This method works by checking which frame is currently selected,
        # and toggles between them by changing to the opposite frame to the current frame.
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
        """Confirm newly inputted data and save it to the list of debtors."""
        # This method checks if the input from the user is valid, and gives an error if necassary. if it is valid, an object of the Debt class is created.
        try:
            amount = float(amount)
            if name == "" or amount <= 0 or date == "" or reason == "":
                messagebox.showerror("Error", "Please fill out all fields")
            else:
                debtor = Debt(name, amount, date, reason)
                debtors.append(debtor)
                messagebox.showinfo("Debtor Added", f"Debtor {name} Added Successfuly")
                # Here, the entry fieldsare cleared to allow new info to be entered.
                for widget in self.current_frame.winfo_children():
                    if isinstance(widget, Entry):
                        widget.delete(0, END)
        except ValueError:
            messagebox.showerror("Error", "Enter a valid loan amount")

    def show_all_data(self):
        """Packs multiple labels and buttons containing debt information through iteration."""
        # The currently displayed info is all removed in order to make way for the up to date list of debtors.
        for widget in self.viewing_frame.winfo_children():
            widget.grid_forget()
        t1 = Label(self.viewing_frame, text="Debtors:", font="Arial")
        t1.grid(row=1, column=0)

        # The debtor information is created through iteration of the debtors list.
        for i, debtor in enumerate(debtors):
            label = Label(self.viewing_frame, text=debtor.show_info(), font="Arial 10")
            label.grid(row=i+2, column=0)
            labels.append(label)

            # A resolve button is also created for each row.
            resolve_button = Button(self.viewing_frame, text="Resolve", bg=BUTTON_BG_COLOUR, command=lambda idx=i: self.resolve_debt(idx))
            resolve_button.grid(row=i+2, column=2)
            buttons.append(resolve_button)

    def resolve_debt(self, index):
        """Delete a debt from the system."""
        debtors.pop(index)
        labels.pop(index)
        buttons.pop(index)
        self.show_all_data()


if __name__ == "__main__":
    root = Tk()
    app = GUI(root)
    root.geometry("500x200")
    root.mainloop()
