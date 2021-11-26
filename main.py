from PyQt5 import QtCore, QtGui, QtWidgets
from typing import Callable
import sys

from window import CodeWindow, TableWindow


class Buttons:
    OR = "or"
    AND = "and"
    NOR = "nor"
    NAND = "nand"
    XOR = "xor"
    XNOR = "xnor"

    gates = ["or", "and", "nor", "nand", "xor", "xnor"]


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, window_size: tuple[int, int], window_title: str = "GUI Application", window_icon_path: str = None, parent: QtWidgets.QWidget = None) -> None:
        super(MainWindow, self).__init__(parent)

        self.active_button = Buttons.OR
        self.table_window = TableWindow((240, 172), "Truth Table", "Assets/table.png")
        self.code_window = CodeWindow((170, 150), " ", "Assets/angle-brackets.png")

        self.setFixedSize(*window_size)
        self.setWindowTitle(window_title)

        if window_icon_path:
            self.setWindowIcon(QtGui.QIcon(window_icon_path))

        self.setup_ui()

    def setup_ui(self) -> None:
        images = [QtGui.QPixmap(f"Assets/Gates/{gate}.png") for gate in Buttons.gates]

        self.gates: dict[str, Callable[[int, int], int]] = {
            Buttons.OR : lambda a, b: a | b,
            Buttons.AND : lambda a, b: a & b,
            Buttons.NOR : lambda a, b: 1 - (a | b),
            Buttons.NAND : lambda a, b: 1 - (a & b),
            Buttons.XOR : lambda a, b: a ^ b,
            Buttons.XNOR : lambda a, b: 1 - (a ^ b),
        }

        self.buttons = {
            Buttons.OR : QtWidgets.QPushButton("OR", self),
            Buttons.AND : QtWidgets.QPushButton("AND", self),
            Buttons.NOR : QtWidgets.QPushButton("NOR", self),
            Buttons.NAND : QtWidgets.QPushButton("NAND", self),
            Buttons.XOR : QtWidgets.QPushButton("XOR", self),
            Buttons.XNOR : QtWidgets.QPushButton("XNOR", self),
        }

        self.icons = {
            Buttons.OR : QtWidgets.QLabel(self),
            Buttons.AND : QtWidgets.QLabel(self),
            Buttons.NOR : QtWidgets.QLabel(self),
            Buttons.NAND : QtWidgets.QLabel(self),
            Buttons.XOR : QtWidgets.QLabel(self),
            Buttons.XNOR : QtWidgets.QLabel(self),
        }

        _font = QtGui.QFont("helvetica", 20)

        for i, (button, icon) in enumerate(zip(self.buttons, self.icons)):
            self.buttons[button].setGeometry(10, (i * 75) + 15, 100, 75)
            self.buttons[button].setFont(_font)
            self.buttons[button].setCheckable(True)
            self.buttons[button].clicked.connect(self.on_toggle_gate)
            self.buttons[button].setStyleSheet("background-color: lightgrey")

            self.icons[icon].setGeometry(130, (i * 75) + 15, 75, 75)
            self.icons[icon].setPixmap(images[i].scaled(75, 75))

        self.buttons[Buttons.OR].setChecked(True)

        self.input_buttons = {
            0 : QtWidgets.QPushButton("0", self),
            1 : QtWidgets.QPushButton("0", self),
        }

        for i in self.input_buttons:
            self.input_buttons[i].setGeometry(self.width() - ((i + 1) * 165), 10, 150, 150)
            self.input_buttons[i].setFont(QtGui.QFont("helvetica", 75))

        self.input_buttons[0].clicked.connect(lambda: self.on_toggle_input(int(0)))
        self.input_buttons[1].clicked.connect(lambda: self.on_toggle_input(int(1)))

        self.output = QtWidgets.QPushButton("0", self)
        self.output.setGeometry(self.width() - 165, 185, 150, 150)
        self.output.setFont(QtGui.QFont("helvetica", 75))
        self.output.setCheckable(False)

        self.view_table_button = QtWidgets.QPushButton("Table", self)
        self.view_table_button.setGeometry(550, 440, 75, 25)
        self.view_table_button.clicked.connect(self.show_table)

        self.view_code_button = QtWidgets.QPushButton("Code", self)
        self.view_code_button.setGeometry(470, 440, 75, 25)
        self.view_code_button.clicked.connect(self.show_code)

    def on_toggle_gate(self) -> None:

        if self.active_button:
            self.buttons[self.active_button].setChecked(False)
            self.buttons[self.active_button].setStyleSheet("background-color: lightgrey")

        if self.table_window.isVisible(): self.table_window.hide()
        if self.code_window.isVisible(): self.code_window.hide()

        for button in self.buttons:
            if self.buttons[button].isChecked():
                self.buttons[button].setStyleSheet("background-color: lightblue")
                self.active_button = button
                self.table_window.gate = button
                self.code_window.gate = button
                break

        self.update_output()

    def update_output(self) -> None:
        self.output.setText(str(self.gates[self.active_button](int(self.input_buttons[0].text()), int(self.input_buttons[1].text()))))

    def on_toggle_input(self, n: int) -> None:
        self.input_buttons[n].setText(str(int(not int(self.input_buttons[n].text()))))
        self.update_output()

    def show_table(self):
        if self.code_window.isVisible():
            self.code_window.hide()

        if not self.table_window.isVisible():
            self.table_window.load_table()
            self.table_window.show()

    def show_code(self):
        if self.table_window.isVisible():
            self.table_window.hide()

        if not self.code_window.isVisible():
            self.code_window.show()


def main():
    app = QtWidgets.QApplication(sys.argv)

    WIDTH, HEIGHT = 640, 480
    TITLE = "Logic Gates"
    ICON = "Assets/operators.png"

    window = MainWindow((WIDTH, HEIGHT), TITLE, ICON)
    window.show()

    app.exec()


if __name__ == "__main__":
    main()
