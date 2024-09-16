from flask import Flask, render_template, request, redirect, url_for
from contacts import ContactManager

app = Flask(__name__)
manager = ContactManager()

# Home Page: View All Contacts
@app.route('/')
def index():
    contacts = manager.view_contacts()
    return render_template('index.html', contacts=contacts)

# Add Contact Page
@app.route('/add', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        address = request.form['address']
        manager.add_contact(name, phone, email, address)
        return redirect(url_for('index'))
    return render_template('add_contact.html')

# Edit Contact Page
@app.route('/edit/<name>', methods=['GET', 'POST'])
def edit_contact(name):
    if request.method == 'POST':
        phone = request.form['phone']
        email = request.form['email']
        address = request.form['address']
        manager.update_contact(name, phone, email, address)
        return redirect(url_for('index'))
    
    contact = manager.contacts.get(name)
    return render_template('edit_contact.html', name=name, contact=contact)

# Delete Contact
@app.route('/delete/<name>')
def delete_contact(name):
    manager.delete_contact(name)
    return redirect(url_for('index'))
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
