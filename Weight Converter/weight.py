import os
from dotenv import load_dotenv
import tkinter as tk
from tkinter import Label, StringVar, Entry, Text, Button, END


class WeightConverter:
    def to_grams(self, kilograms):
        return kilograms * 1000

    def to_pounds(self, kilograms):
        return kilograms * 2.20462

    def to_ounces(self, kilograms):
        return kilograms * 35.274
class ConversionStrategy:
    def convert(self, kilograms):
        raise NotImplementedError("You should implement this method!")

class GramsConversion(ConversionStrategy):
    def convert(self, kilograms):
        return kilograms * 1000

class PoundsConversion(ConversionStrategy):
    def convert(self, kilograms):
        return kilograms * 2.20462

class OuncesConversion(ConversionStrategy):
    def convert(self, kilograms):
        return kilograms * 35.274

class WeightConverterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Weight Converter")
        self.master.resizable(0, 0)
        self.master.configure(bg='#0492C2')

        self.converter = WeightConverter()

        self.create_widgets()

    def create_widgets(self):
        self.label = Label(self.master, text="Enter Weight In Kilograms")
        self.label.grid(row=0, column=0)

        self.weight_value = StringVar()
        self.entry = Entry(self.master, textvariable=self.weight_value)
        self.entry.grid(row=0, column=1)

        self.output_grams = Text(self.master, height=1, width=20)
        self.output_pounds = Text(self.master, height=1, width=20)
        self.output_ounces = Text(self.master, height=1, width=20)

        self.output_grams.grid(row=1, column=0)
        self.output_pounds.grid(row=1, column=1)
        self.output_ounces.grid(row=1, column=2)

        self.btn_convert = Button(self.master, text='Convert', command=self.convert_weight)
        self.btn_convert.grid(row=0, column=2)

        Label(self.master, text="Gram").grid(row=2, column=0)
        Label(self.master, text="Pound").grid(row=2, column=1)
        Label(self.master, text="Ounce").grid(row=2, column=2)

    def convert_weight(self):
        kilograms = float(self.weight_value.get())

        self.output_grams.delete("1.0", END)
        self.output_pounds.delete("1.0", END)
        self.output_ounces.delete("1.0", END)

        # Apply the conversion strategies
        grams_conv = GramsConversion().convert(kilograms)
        pounds_conv = PoundsConversion().convert(kilograms)
        ounces_conv = OuncesConversion().convert(kilograms)

        self.output_grams.insert(END, grams_conv)
        self.output_pounds.insert(END, pounds_conv)
        self.output_ounces.insert(END, ounces_conv)


if __name__ == "__main__":
    load_dotenv()  # Load environment variables from a .env file

    root = tk.Tk()
    app = WeightConverterApp(root)
    root.mainloop()
