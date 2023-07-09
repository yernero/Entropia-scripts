import tkinter as tk
from tkinter import messagebox
import pickle
from datetime import datetime

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()
        self.load_data()

    def create_widgets(self):
        self.material_label = tk.Label(self, text="Material Name:")
        self.material_label.grid(row=0, column=0)
        self.material_entry = tk.Entry(self)
        self.material_entry.grid(row=0, column=1)

        self.markup_label = tk.Label(self, text="Lowest Markup:")
        self.markup_label.grid(row=1, column=0)
        self.markup_entry = tk.Entry(self)
        self.markup_entry.grid(row=1, column=1)

        self.amount_label = tk.Label(self, text="Amount in Inventory:")
        self.amount_label.grid(row=2, column=0)
        self.amount_entry = tk.Entry(self)
        self.amount_entry.grid(row=2, column=1)

        self.total_value_label = tk.Label(self, text="Total PED Value:")
        self.total_value_label.grid(row=3, column=0)
        self.total_value_entry = tk.Entry(self)
        self.total_value_entry.grid(row=3, column=1)

        self.calculate_button = tk.Button(self, text="Calculate", command=self.calculate_quantity)
        self.calculate_button.grid(row=4, column=0, columnspan=2)

    def load_data(self):
        try:
            with open('data.pkl', 'rb') as f:
                self.data = pickle.load(f)
        except FileNotFoundError:
            self.data = []

    def calculate_quantity(self):
        material = self.material_entry.get()
        markup = float(self.markup_entry.get())
        amount = float(self.amount_entry.get())
        total_value = float(self.total_value_entry.get())
        
        avg_material_price = total_value / amount
        target_price = avg_material_price * (1 + markup/100)
        best_quantity_to_sell = total_value // target_price
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.data.append((timestamp, material, markup, amount, total_value, best_quantity_to_sell))

        with open('data.pkl', 'wb') as f:
            pickle.dump(self.data, f)
        
        messagebox.showinfo("Result", f"The best quantity of {material} to sell, to stay under the lowest markup price, is: {best_quantity_to_sell}")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
