import tkinter as tk
from tkinter import messagebox

class ContactManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Management System")
        self.root.configure(background="#f0f0f0")  

        self.contacts = {}

        self.name_label = tk.Label(root, text="Name:", font=("Arial", 12), fg="#00698f")  
        self.name_label.pack(padx=10, pady=10)

        self.name_entry = tk.Entry(root, width=20, font=("Arial", 12))  
        self.name_entry.pack(padx=10, pady=10)

        self.phone_label = tk.Label(root, text="Phone Number:", font=("Arial", 12), fg="#00698f")  
        self.phone_label.pack(padx=10, pady=10)

        self.phone_entry = tk.Entry(root, width=20, font=("Arial", 12))  
        self.phone_entry.pack(padx=10, pady=10)

        self.email_label = tk.Label(root, text="Email:", font=("Arial", 12), fg="#00698f") 
        self.email_label.pack(padx=10, pady=10)

        self.email_entry = tk.Entry(root, width=20, font=("Arial", 12))  
        self.email_entry.pack(padx=10, pady=10)

        self.address_label = tk.Label(root, text="Address:", font=("Arial", 12), fg="#00698f") 
        self.address_label.pack(padx=10, pady=10)

        self.address_entry = tk.Entry(root, width=20, font=("Arial", 12)) 
        self.address_entry.pack(padx=10, pady=10)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact, font=("Arial", 12), bg="#007bff", fg="white") 
        self.add_button.pack(padx=10, pady=10)

        self.view_button = tk.Button(root, text="View Contact List", command=self.view_contacts, font=("Arial", 12), bg="#007bff", fg="white") 
        self.view_button.pack(padx=10, pady=10)

        self.search_label = tk.Label(root, text="Search:", font=("Arial", 12), fg="#00698f")  
        self.search_label.pack(padx=10, pady=10)

        self.search_entry = tk.Entry(root, width=20, font=("Arial", 12))  
        self.search_entry.pack(padx=10, pady=10)

        self.search_button = tk.Button(root, text="Search", command=self.search_contact, font=("Arial", 12), bg="#007bff", fg="white") 
        self.search_button.pack(padx=10, pady=10)

        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact, font=("Arial", 12), bg="#007bff", fg="white") 
        self.update_button.pack(padx=10, pady=10)

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact, font=("Arial", 12), bg="#007bff", fg="white")  
        self.delete_button.pack(padx=10, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            self.contacts[name] = {"phone": phone, "email": email, "address": address}
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showerror("Error", "Please enter name and phone number.")

    def view_contacts(self):
        contact_list = ""
        for name, details in self.contacts.items():
            contact_list += f"{name}: {details['phone']}\n"
        messagebox.showinfo("Contact List", contact_list)

    def search_contact(self):
        search_term = self.search_entry.get()
        found = False
        for name, details in self.contacts.items():
            if search_term in name or search_term in details["phone"]:
                messagebox.showinfo("Search Result", f"Name: {name}\nPhone: {details['phone']}\nEmail:{details['email']}\nAddress: {details['address']}")
                found = True
                break
        if not found:
            messagebox.showerror("Error", "Contact not found.")

    def update_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name in self.contacts:
            self.contacts[name] = {"phone": phone, "email": email, "address": address}
            messagebox.showinfo("Success", "Contact updated successfully!")
        else:
            messagebox.showerror("Error", "Contact not found.")

    def delete_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showerror("Error", "Contact not found.")

root = tk.Tk()
app = ContactManagementSystem(root)
root.mainloop()