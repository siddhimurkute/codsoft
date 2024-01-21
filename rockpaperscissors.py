import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QMessageBox


class RockPaperScissorsApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Rock Paper Scissors Game')
        self.setGeometry(100, 100, 400, 200)

        self.user_choice_label = QLabel('Choose rock, paper, or scissors:')
        self.result_label = QLabel('Result:')
        self.play_again_button = QPushButton('Play Again', self)
        self.play_again_button.setEnabled(False)
        self.play_again_button.clicked.connect(self.play_again)

        layout = QVBoxLayout()
        layout.addWidget(self.user_choice_label)

        choices_layout = QHBoxLayout()
        for choice in ['Rock', 'Paper', 'Scissors']:
            button = QPushButton(choice, self)
            button.clicked.connect(lambda _, choice=choice: self.check_winner(choice))
            choices_layout.addWidget(button)

        layout.addLayout(choices_layout)
        layout.addWidget(self.result_label)
        layout.addWidget(self.play_again_button)

        self.setLayout(layout)

    def check_winner(self, user_choice):
        choices = ['Rock', 'Paper', 'Scissors']
        computer_choice = random.choice(choices)

        result = self.determine_winner(user_choice, computer_choice)

        self.result_label.setText(f'Your choice: {user_choice}\nComputer\'s choice: {computer_choice}\nResult: {result}')

        self.play_again_button.setEnabled(True)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return 'It\'s a tie!'
        elif (
            (user_choice == 'Rock' and computer_choice == 'Scissors') or
            (user_choice == 'Paper' and computer_choice == 'Rock') or
            (user_choice == 'Scissors' and computer_choice == 'Paper')
        ):
            return 'You win!'
        else:
            return 'Computer wins!'

    def play_again(self):
        self.result_label.clear()
        self.play_again_button.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    rps_app = RockPaperScissorsApp()
    rps_app.show()
    sys.exit(app.exec_())
