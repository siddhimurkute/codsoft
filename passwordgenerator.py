import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton


class PasswordGeneratorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Password Generator')
        self.setGeometry(100, 100, 400, 200)

        self.length_label = QLabel('Enter password length:')
        self.length_input = QLineEdit()
        self.generated_password_label = QLabel('Generated Password:')
        self.generated_password_output = QLineEdit()
        self.generated_password_output.setReadOnly(True)

        generate_button = QPushButton('Generate Password', self)
        generate_button.clicked.connect(self.generate_password)

        layout = QVBoxLayout()
        layout.addWidget(self.length_label)
        layout.addWidget(self.length_input)
        layout.addWidget(generate_button)
        layout.addWidget(self.generated_password_label)
        layout.addWidget(self.generated_password_output)

        self.setLayout(layout)

    def generate_password(self):
        try:
            password_length = int(self.length_input.text())
            if password_length <= 0:
                raise ValueError("Password length should be a positive integer.")
            
            characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?~"
            generated_password = ''.join(random.choice(characters) for _ in range(password_length))
            
            self.generated_password_output.setText(generated_password)
        except ValueError as e:
            self.show_message("Error", str(e))

    def show_message(self, title, text):
        from PyQt5.QtWidgets import QMessageBox
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(text)
        msg_box.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    password_generator_app = PasswordGeneratorApp()
    password_generator_app.show()
    sys.exit(app.exec_())
