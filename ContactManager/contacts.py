import json
import os

CONTACTS_FILE = 'data/contacts.json'

class ContactManager:
    def __init__(self):
        self.contacts = {}
        self.load_contacts()

    def load_contacts(self):
        """Load contacts from a JSON file."""
        if os.path.exists(CONTACTS_FILE):
            with open(CONTACTS_FILE, 'r') as file:
                self.contacts = json.load(file)
        else:
            self.contacts = {}

    def save_contacts(self):
        """Save contacts to a JSON file."""
        with open(CONTACTS_FILE, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, name, phone, email, address):
        """Add a new contact."""
        self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
        self.save_contacts()

    def view_contacts(self):
        """Return all contacts."""
        return self.contacts

    def search_contact(self, query):
        """Search for a contact by name or phone."""
        results = {name: details for name, details in self.contacts.items()
                   if query.lower() in name.lower() or query in details['phone']}
        return results

    def update_contact(self, name, phone=None, email=None, address=None):
        """Update an existing contact."""
        if name in self.contacts:
            if phone:
                self.contacts[name]['phone'] = phone
            if email:
                self.contacts[name]['email'] = email
            if address:
                self.contacts[name]['address'] = address
            self.save_contacts()

    def delete_contact(self, name):
        """Delete a contact."""
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
