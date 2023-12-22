import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
import random

class DiceSimulator(QWidget):
    def __init__(self):
        super().__init__()

        self.results = {}

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Кости')
        self.setGeometry(200, 100, 300, 200)

        self.result_label = QLabel('Результат: ')
        self.frequency_label = QLabel('Количество повторов: ')

        roll_button = QPushButton('Кинуть кости', self)
        roll_button.clicked.connect(self.rollDice)

        layout = QVBoxLayout()
        layout.addWidget(self.result_label)
        layout.addWidget(self.frequency_label)
        layout.addWidget(roll_button)

        self.setLayout(layout)

    def rollDice(self):
        result = random.randint(1, 6)
        self.updateResults(result)
        self.updateLabels()

    def updateResults(self, result):
        if result in self.results:
            self.results[result] += 1
        else:
            self.results[result] = 1

    def updateLabels(self):
        total_rolls = sum(self.results.values())
        result_text = f'Результат: {list(self.results.keys())}, Количество повторов: {list(self.results.values())}'
        frequency_text = ''

        for key, value in self.results.items():
            frequency = (value / total_rolls) * 100
            frequency_text += f'{key}: {frequency:.2f}%\n'

        self.result_label.setText(result_text)
        self.frequency_label.setText(frequency_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DiceSimulator()
    window.show()
    sys.exit(app.exec())