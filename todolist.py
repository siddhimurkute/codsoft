import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QListWidgetItem, QCheckBox, QMessageBox
from PyQt5.QtCore import Qt


class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('To-Do List App')
        self.setGeometry(100, 100, 400, 300)

        self.tasks_list = QListWidget()
        self.task_input = QLineEdit()

        add_button = QPushButton('Add Task', self)
        add_button.clicked.connect(self.add_task)

        remove_button = QPushButton('Remove Task', self)
        remove_button.clicked.connect(self.remove_task)

        layout = QVBoxLayout()
        layout.addWidget(QLabel('To-Do List'))
        layout.addWidget(self.tasks_list)
        layout.addWidget(self.task_input)

        button_layout = QHBoxLayout()
        button_layout.addWidget(add_button)
        button_layout.addWidget(remove_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def add_task(self):
        task_text = self.task_input.text().strip()
        if task_text:
            task_item = QListWidgetItem(task_text, self.tasks_list)
            task_item.setFlags(task_item.flags() | Qt.ItemIsUserCheckable)
            task_item.setCheckState(Qt.Unchecked)
            self.task_input.clear()
        else:
            self.show_message("Empty Task", "Please enter a task.")

    def remove_task(self):
        selected_item = self.tasks_list.currentItem()
        if selected_item:
            self.tasks_list.takeItem(self.tasks_list.row(selected_item))
        else:
            self.show_message("No Task Selected", "Please select a task to remove.")

    def show_message(self, title, text):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(text)
        msg_box.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    todo_app = ToDoApp()
    todo_app.show()
    sys.exit(app.exec_())
