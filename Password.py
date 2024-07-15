import tkinter as tk
from random import choice
import string
import time

class PasswordGenerator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Password Generator")
        self.window.geometry("400x400")  
        self.window.resizable(False, False)  

        self.trial_period = 30  
        self.start_time = time.time()

        self.create_widgets()

    def create_widgets(self):
        
        self.title_label = tk.Label(self.window, text="Password Generator", font=("Arial", 24), fg="#007bff")
        self.title_label.pack(padx=20, pady=10)

        self.trial_label = tk.Label(self.window, text="Trial Period: {} days remaining".format(self.trial_period), font=("Arial", 16), fg="#ff0000")
        self.trial_label.pack(padx=20, pady=10)

    
        self.length_label = tk.Label(self.window, text="Enter password length:", font=("Arial", 16), fg="#333")
        self.length_label.pack(padx=20, pady=10)

        self.length_entry = tk.Entry(self.window, width=20, font=("Arial", 16))
        self.length_entry.pack(padx=20, pady=10)

        # Character selection section
        self.character_label = tk.Label(self.window, text="Select characters to include:", font=("Arial", 16), fg="#333")
        self.character_label.pack(padx=20, pady=10)

        self.lowercase_var = tk.IntVar()
        self.lowercase_checkbox = tk.Checkbutton(self.window, text="Lowercase letters", variable=self.lowercase_var, fg="#008000") 
        self.lowercase_checkbox.pack(padx=20, pady=5)

        self.uppercase_var = tk.IntVar()
        self.uppercase_checkbox = tk.Checkbutton(self.window, text="Uppercase letters", variable=self.uppercase_var, fg="#0000ff")  
        self.uppercase_checkbox.pack(padx=20, pady=5)

        self.digits_var = tk.IntVar()
        self.digits_checkbox = tk.Checkbutton(self.window, text="Digits", variable=self.digits_var, fg="#ff0000")  
        self.digits_checkbox.pack(padx=20, pady=5)

        self.punctuation_var = tk.IntVar()
        self.punctuation_checkbox = tk.Checkbutton(self.window, text="Punctuation", variable=self.punctuation_var, fg="#ffff00") 
        self.punctuation_checkbox.pack(padx=20, pady=5)

        self.generate_button = tk.Button(self.window, text="Generate Password", command=self.generate_password, width=20, height=2, font=("Arial", 14), bg="#007bff", fg="white")
        self.generate_button.pack(padx=20, pady=10)

        # Password section
        self.password_label = tk.Label(self.window, text="Generated Password:", font=("Arial", 16), fg="#333")
        self.password_label.pack(padx=20, pady=10)

        self.password_text = tk.Text(self.window, width=40, height=5, font=("Arial", 14), bg="#ccccff")  
        self.password_text.pack(padx=20, pady=10)

    def generate_password(self):
        if time.time() - self.start_time > self.trial_period * 86400: 
            self.trial_label.config(text="Trial Period Expired!")
            self.generate_button.config(state="disabled")
            return

        length = int(self.length_entry.get())
        characters = ""

        if self.lowercase_var.get():
            characters += string.ascii_lowercase
        if self.uppercase_var.get():
            characters += string.ascii_uppercase
        if self.digits_var.get():
            characters += string.digits
        if self.punctuation_var.get():
            characters += string.punctuation

        password = ''.join(choice(characters) for _ in range(length))
        self.password_text.delete(1.0, tk.END)  
        self.password_text.insert(tk.END, password)  

    def update_trial_period(self):
        remaining_days = int((self.trial_period * 86400 - (time.time() - self.start_time)) / 86400)
        self.trial_label.config(text="Trial Period: {} days remaining".format(remaining_days))
        self.window.after(1000, self.update_trial_period)  

    def run(self):
        self.window.after(1000, self.update_trial_period) 
        self.window.mainloop()

if __name__ == "__main__":
    generator = PasswordGenerator()
    generator.run()