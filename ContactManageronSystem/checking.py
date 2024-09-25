import tkinter as tk

root = tk.Tk()
root.title("Tkinter Test")
root.mainloop()
from tkinter import messagebox, simpledialog

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBookApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Book")
        self.contacts = []
        
        # Create UI Elements
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        title_label = tk.Label(self.master, text="Contact Book", font=("Arial", 16))
        title_label.pack(pady=10)

        # Contact List Box
        self.contact_listbox = tk.Listbox(self.master, width=50, height=10)
        self.contact_listbox.pack(pady=10)

        # Buttons
        add_button = tk.Button(self.master, text="Add Contact", command=self.add_contact)
        add_button.pack(pady=5)

        update_button = tk.Button(self.master, text="Update Contact", command=self.update_contact)
        update_button.pack(pady=5)

        delete_button = tk.Button(self.master, text="Delete Contact", command=self.delete_contact)
        delete_button.pack(pady=5)

        search_button = tk.Button(self.master, text="Search Contact", command=self.search_contact)
        search_button.pack(pady=5)

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter Name:")
        if not name: return
        phone = simpledialog.askstring("Input", "Enter Phone Number:")
        email = simpledialog.askstring("Input", "Enter Email:")
        address = simpledialog.askstring("Input", "Enter Address:")

        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        self.update_contact_listbox()
        messagebox.showinfo("Success", f"Contact '{name}' added successfully!")

    def update_contact(self):
        selected_index = self.contact_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Warning", "No contact selected!")
            return
        
        contact = self.contacts[selected_index[0]]
        name = simpledialog.askstring("Input", "Update Name:", initialvalue=contact.name)
        phone = simpledialog.askstring("Input", "Update Phone Number:", initialvalue=contact.phone)
        email = simpledialog.askstring("Input", "Update Email:", initialvalue=contact.email)
        address = simpledialog.askstring("Input", "Update Address:", initialvalue=contact.address)

        contact.name = name
        contact.phone = phone
        contact.email = email
        contact.address = address
       
