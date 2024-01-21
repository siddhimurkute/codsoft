import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox


class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Simple Calculator')
        self.setGeometry(100, 100, 300, 200)

        self.num1_label = QLabel('Enter number 1:')
        self.num1_input = QLineEdit()

        self.num2_label = QLabel('Enter number 2:')
        self.num2_input = QLineEdit()

        self.operation_label = QLabel('Choose operation (+, -, *, /) :')
        self.operation_input = QLineEdit()

        self.result_label = QLabel('Result:')
        self.result_output = QLineEdit()
        self.result_output.setReadOnly(True)

        calculate_button = QPushButton('Calculate', self)
        calculate_button.clicked.connect(self.calculate)

        layout = QVBoxLayout()
        layout.addWidget(self.num1_label)
        layout.addWidget(self.num1_input)
        layout.addWidget(self.num2_label)
        layout.addWidget(self.num2_input)
        layout.addWidget(self.operation_label)
        layout.addWidget(self.operation_input)
        layout.addWidget(calculate_button)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_output)

        self.setLayout(layout)

    def calculate(self):
        try:
            num1 = float(self.num1_input.text())
            num2 = float(self.num2_input.text())
            operation = self.operation_input.text()

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                result = num1 / num2
            else:
                raise ValueError("Invalid operation")

            self.result_output.setText(str(result))
        except ValueError as e:
            self.show_message("Error", str(e))
        except ZeroDivisionError:
            self.show_message("Error", "Cannot divide by zero")

    def show_message(self, title, text):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(text)
        msg_box.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator_app = CalculatorApp()
    calculator_app.show()
    sys.exit(app.exec_())
