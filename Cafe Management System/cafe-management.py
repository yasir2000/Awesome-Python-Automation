import os
from dotenv import load_dotenv
import tkinter as tk
from tkinter import messagebox, LabelFrame, Entry, Button, Label
from datetime import datetime

load_dotenv()

class PriceList:
    def __init__(self):
        self.prices = {
            "tea": float(os.getenv('TEA_PRICE', 10)),
            "coffee": float(os.getenv('COFFEE_PRICE', 20)),
            "sandwich": float(os.getenv('SANDWICH_PRICE', 50)),
            "cake": float(os.getenv('CAKE_PRICE', 100)),
            "burger": float(os.getenv('BURGER_PRICE', 50)),
            "pizza": float(os.getenv('PIZZA_PRICE', 150)),
            "fries": float(os.getenv('FRIES_PRICE', 80)),
            "pepsi": float(os.getenv('PEPSI_PRICE', 80)),
        }

class Order:
    def __init__(self, item_quantities):
        self.item_quantities = item_quantities

    def compute_total(self, price_list):
        total = sum(price_list.prices[item] * qty 
                    for item, qty in self.item_quantities.items() if qty)
        return total

class CafeManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry('500x300')
        self.root.title("Cafe Management System")
        self.initialize_ui()

    def initialize_ui(self):
        self.heading = tk.Label(self.root, text="Cafe Management System", font=('verdana', 20, 'bold'), fg="#248aa2")
        self.heading.pack()

        self.price_list = PriceList()
        self.item_entries = {}
        
        frame1 = LabelFrame(self.root, text="Cafe Items", bg="white")
        frame1.pack(pady=10)

        for index, item in enumerate(self.price_list.prices.keys()):
            label = Label(frame1, text=item.capitalize(), font=('verdana', 10, 'bold'), bg="white")
            label.grid(row=index, column=0, padx=10)

            entry = Entry(frame1, width=7, borderwidth=4, relief=tk.SUNKEN)
            entry.grid(row=index, column=1)
            self.item_entries[item] = entry

        Button(self.root, text="Calculate Total", command=self.calculate_total).pack(pady=10)
        Button(self.root, text="Clear", command=self.clear_entries).pack(pady=5)
        Button(self.root, text="Exit", command=self.quit_app).pack(pady=5)

    def calculate_total(self):
        quantities = {item: int(entry.get()) if entry.get() else 0 
                      for item, entry in self.item_entries.items()}
        order = Order(quantities)
        total = order.compute_total(self.price_list)

        messagebox.showinfo("Total Bill", f"The total bill is {total:.2f} INR")

    def clear_entries(self):
        for entry in self.item_entries.values():
            entry.delete(0, tk.END)

    def quit_app(self):
        if messagebox.askyesno('Exit', "Do you want to exit the application?"):
            self.root.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    app = CafeManagementApp(root)
    root.mainloop()
