import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

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
        self.master.geometry("400x400")
        self.contacts = []

        # Create UI Elements
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        title_label = tk.Label(self.master, text="Contact Book", font=("Arial", 18))
        title_label.pack(pady=10)

        # Contact List Box
        self.contact_listbox = tk.Listbox(self.master, width=50, height=10)
        self.contact_listbox.pack(pady=10)

        # Scrollbar for Listbox
        scrollbar = tk.Scrollbar(self.master)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.contact_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.contact_listbox.yview)

        # Buttons Frame
        button_frame = tk.Frame(self.master)
        button_frame.pack(pady=10)

        add_button = tk.Button(button_frame, text="Add Contact", command=self.add_contact, width=12)
        add_button.grid(row=0, column=0, padx=5)

        update_button = tk.Button(button_frame, text="Update Contact", command=self.update_contact, width=12)
        update_button.grid(row=0, column=1, padx=5)

        delete_button = tk.Button(button_frame, text="Delete Contact", command=self.delete_contact, width=12)
        delete_button.grid(row=0, column=2, padx=5)

        search_button = tk.Button(button_frame, text="Search Contact", command=self.search_contact, width=12)
        search_button.grid(row=0, column=3, padx=5)

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
        self.update_contact_listbox()
        messagebox.showinfo("Success", "Contact updated successfully!")

    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Warning", "No contact selected!")
            return

        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this contact?")
        if confirm:
            del self.contacts[selected_index[0]]
            self.update_contact_listbox()
            messagebox.showinfo("Success", "Contact deleted successfully!")

    def search_contact(self):
        query = simpledialog.askstring("Input", "Search by Name or Phone:")
        if not query: return
        
        found_contacts = [contact for contact in self.contacts if query.lower() in contact.name.lower() or query in contact.phone]
        
        if found_contacts:
            self.contact_listbox.delete(0, tk.END)  # Clear the listbox
            for contact in found_contacts:
                self.contact_listbox.insert(tk.END, f"{contact.name} - {contact.phone}")
        else:
            messagebox.showinfo("Not Found", "No contacts found.")

    def update_contact_listbox(self):
        self.contact_listbox.delete(0, tk.END)  # Clear the listbox
        for contact in self.contacts:
            self.contact_listbox.insert(tk.END, f"{contact.name} - {contact.phone}")

# Create the main application window
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
