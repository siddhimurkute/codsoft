import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QMessageBox, QDialog, QFormLayout, QDialogButtonBox


class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name} - {self.phone}"


class ContactManagerApp(QWidget):
    def __init__(self):
        super().__init__()

        self.contacts = []
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Contact Manager')
        self.setGeometry(100, 100, 500, 400)

        self.contact_list = QListWidget()
        self.update_contact_list()

        add_button = QPushButton('Add Contact', self)
        add_button.clicked.connect(self.add_contact)

        update_button = QPushButton('Update Contact', self)
        update_button.clicked.connect(self.update_contact)

        delete_button = QPushButton('Delete Contact', self)
        delete_button.clicked.connect(self.delete_contact)

        view_button = QPushButton('View Contact', self)
        view_button.clicked.connect(self.view_contact)

        search_label = QLabel('Search:')
        self.search_input = QLineEdit()
        search_button = QPushButton('Search', self)
        search_button.clicked.connect(self.search_contact)

        layout = QVBoxLayout()
        layout.addWidget(self.contact_list)

        button_layout = QHBoxLayout()
        button_layout.addWidget(add_button)
        button_layout.addWidget(update_button)
        button_layout.addWidget(delete_button)
        button_layout.addWidget(view_button)

        search_layout = QHBoxLayout()
        search_layout.addWidget(search_label)
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(search_button)

        layout.addLayout(button_layout)
        layout.addLayout(search_layout)

        self.setLayout(layout)

    def add_contact(self):
        dialog = ContactDialog()
        if dialog.exec_() == QDialog.Accepted:
            contact = dialog.get_contact()
            self.contacts.append(contact)
            self.update_contact_list()

    def update_contact(self):
        selected_item = self.contact_list.currentItem()
        if selected_item:
            contact_index = self.contact_list.row(selected_item)
            old_contact = self.contacts[contact_index]

            dialog = ContactDialog(old_contact)
            if dialog.exec_() == QDialog.Accepted:
                new_contact = dialog.get_contact()
                self.contacts[contact_index] = new_contact
                self.update_contact_list()

    def delete_contact(self):
        selected_item = self.contact_list.currentItem()
        if selected_item:
            contact_index = self.contact_list.row(selected_item)
            del self.contacts[contact_index]
            self.update_contact_list()

    def view_contact(self):
        selected_item = self.contact_list.currentItem()
        if selected_item:
            contact_index = self.contact_list.row(selected_item)
            contact = self.contacts[contact_index]
            QMessageBox.information(self, 'Contact Details', f"Name: {contact.name}\nPhone: {contact.phone}\nEmail: {contact.email}\nAddress: {contact.address}")

    def search_contact(self):
        search_term = self.search_input.text().lower()
        results = [contact for contact in self.contacts if search_term in contact.name.lower() or search_term in contact.phone]
        self.update_contact_list(results)

    def update_contact_list(self, contacts=None):
        self.contact_list.clear()
        contacts = contacts or self.contacts
        for contact in contacts:
            self.contact_list.addItem(str(contact))


class ContactDialog(QDialog):
    def __init__(self, contact=None):
        super().__init__()

        self.contact = contact
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Add/Update Contact')
        self.setGeometry(200, 200, 300, 200)

        form_layout = QFormLayout()

        self.name_input = QLineEdit()
        self.phone_input = QLineEdit()
        self.email_input = QLineEdit()
        self.address_input = QLineEdit()

        form_layout.addRow('Name:', self.name_input)
        form_layout.addRow('Phone:', self.phone_input)
        form_layout.addRow('Email:', self.email_input)
        form_layout.addRow('Address:', self.address_input)

        if self.contact:
            self.name_input.setText(self.contact.name)
            self.phone_input.setText(self.contact.phone)
            self.email_input.setText(self.contact.email)
            self.address_input.setText(self.contact.address)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        layout = QVBoxLayout()
        layout.addLayout(form_layout)
        layout.addWidget(button_box)

        self.setLayout(layout)

    def get_contact(self):
        name = self.name_input.text()
        phone = self.phone_input.text()
        email = self.email_input.text()
        address = self.address_input.text()
        return Contact(name, phone, email, address)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    contact_manager_app = ContactManagerApp()
    contact_manager_app.show()
    sys.exit(app.exec_())
