from PyQt5 import QtCore, QtGui, QtWidgets

import os

class TableWindow(QtWidgets.QMainWindow):
    def __init__(self, window_size: tuple[int, int], window_title: str = "GUI Application", window_icon_path: str = None, parent: QtWidgets.QWidget = None) -> None:
        self.gates = {
            "or": [
                ["A", "B", "Y"],
                ["0", "0", "0"],
                ["0", "1", "1"],
                ["1", "0", "1"],
                ["0", "0", "1"],
            ],
            "and": [
                ["A", "B", "Y"],
                ["0", "0", "0"],
                ["0", "1", "0"],
                ["1", "0", "0"],
                ["0", "0", "1"],
            ],
            "nor": [
                ["A", "B", "Y"],
                ["0", "0", "1"],
                ["0", "1", "0"],
                ["1", "0", "0"],
                ["0", "0", "0"],
            ],
            "nand": [
                ["A", "B", "Y"],
                ["0", "0", "1"],
                ["0", "1", "1"],
                ["1", "0", "1"],
                ["1", "1", "0"],
            ],
            "xor": [
                ["A", "B", "Y"],
                ["0", "0", "0"],
                ["0", "1", "1"],
                ["1", "0", "1"],
                ["1", "1", "0"],
            ],
            "xnor": [
                ["A", "B", "Y"],
                ["0", "0", "1"],
                ["0", "1", "0"],
                ["1", "0", "0"],
                ["1", "1", "1"]
            ]
        }
        super(TableWindow, self).__init__(parent)

        self.gate = "or"

        self.setFixedSize(*window_size)
        self.setWindowTitle(window_title)

        if window_icon_path:
            self.setWindowIcon(QtGui.QIcon(window_icon_path))

        self.setup_ui()

    def setup_ui(self):
        self.table = QtWidgets.QTableWidget(5, 3, self)
        self.table.setGeometry(10, 10, self.width() - 20, self.height() - 20)
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setVisible(False)
        self.table.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.table.setAlternatingRowColors(True)

    def load_table(self):
        self.setWindowTitle(f"{self.gate.upper()} Truth Table")

        for x in range(3):
            for y in range(5):
                item = QtWidgets.QTableWidgetItem(self.gates[self.gate][y][x])
                item.setFlags(item.flags() ^ QtCore.Qt.ItemFlag.ItemIsEditable)
                self.table.setItem(y,x,item)


class CodeWindow(QtWidgets.QMainWindow):
    def __init__(self, window_size: tuple[int, int], window_title: str = "GUI Application", window_icon_path: str = None, parent: QtWidgets.QWidget = None) -> None:
        super(CodeWindow, self).__init__(parent)

        self.gate = "or"

        self.setFixedSize(*window_size)
        self.setWindowTitle(window_title)

        if window_icon_path:
            self.setWindowIcon(QtGui.QIcon(window_icon_path))

        self.setup_ui()

    def setup_ui(self):
        languages = ["C++", "Go", "Haskell", "Java", "JavaScript", "Python"]
        languages.sort()

        self.language_input = QtWidgets.QComboBox(self)
        self.language_input.addItems(languages)
        self.language_input.setGeometry(10, 0, 75, 25)

        self.open_image_button = QtWidgets.QPushButton("Show Code", self)
        self.open_image_button.setGeometry(10, 35, 150, 50)
        self.open_image_button.setFont(QtGui.QFont("helvetica", 15))
        self.open_image_button.clicked.connect(lambda: self.open_image("start"))

        self.open_code_button = QtWidgets.QPushButton("Edit Code", self)
        self.open_code_button.setGeometry(10, 90, 150, 50)
        self.open_code_button.setFont(QtGui.QFont("helvetica", 15))
        self.open_code_button.clicked.connect(lambda: self.open_image("code"))

    def open_image(self, cmd):
        lang = self.language_input.currentText()
        os.system(f"{cmd} Assets\\Code\\{lang}\\{self.gate}.png")
