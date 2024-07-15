import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.configure(background="#f0f0f0")  

        self.num1_label = tk.Label(root, text="Number 1:", font=("Arial", 12), fg="#00698f")  
        self.num1_label.pack(padx=10, pady=10)

        self.num1_entry = tk.Entry(root, width=20, font=("Arial", 12))  
        self.num1_entry.pack(padx=10, pady=10)

        self.num2_label = tk.Label(root, text="Number 2:", font=("Arial", 12), fg="#00698f")  
        self.num2_label.pack(padx=10, pady=10)

        self.num2_entry = tk.Entry(root, width=20, font=("Arial", 12))  
        self.num2_entry.pack(padx=10, pady=10)

        self.operation_label = tk.Label(root, text="Operation:", font=("Arial", 12), fg="#00698f") 
        self.operation_label.pack(padx=10, pady=10)

        self.operation_var = tk.StringVar()
        self.operation_var.set("+")

        self.add_radio = tk.Radiobutton(root, text="+", variable=self.operation_var, value="+", fg="#008000", bg="#f0f0f0")  
        self.add_radio.pack(padx=10, pady=10)

        self.sub_radio = tk.Radiobutton(root, text="-", variable=self.operation_var, value="-", fg="#ff0000", bg="#f0f0f0") 
        self.sub_radio.pack(padx=10, pady=10)

        self.mul_radio = tk.Radiobutton(root, text="*", variable=self.operation_var, value="*", fg="#0000ff", bg="#f0f0f0")  
        self.mul_radio.pack(padx=10, pady=10)

        self.div_radio = tk.Radiobutton(root, text="/", variable=self.operation_var, value="/", fg="#ffff00", bg="#f0f0f0")
        self.div_radio.pack(padx=10, pady=10)

        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate, font=("Arial", 12), bg="#007bff", fg="white")  
        self.calculate_button.pack(padx=10, pady=10)

        self.result_label = tk.Label(root, text="Result:", font=("Arial", 12), fg="#00698f")  
        self.result_label.pack(padx=10, pady=10)

        self.result_entry = tk.Entry(root, width=20, font=("Arial", 12))  
        self.result_entry.pack(padx=10, pady=10)

    def calculate(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            operation = self.operation_var.get()

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 != 0:
                    result = num1 / num2
                else:
                    messagebox.showerror("Error", "Division by zero is not allowed.")
                    return

            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(0, str(result))
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter numbers.")

root = tk.Tk()
app = CalculatorApp(root)
root.mainloop()