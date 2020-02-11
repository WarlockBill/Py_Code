from PyQt5.QtWidgets import *


class MainWindow(QDialog):

    def __init__(self):
        super().__init__()

        convert_from_label = QLabel('Convert From:')
        self.convert_from_line_edit = QLineEdit()

        convert_to_label = QLabel('Convert To:')
        self.converted_to_label = QLabel()

        self.convert_button = QPushButton('Convert')
        self.convert_button.clicked.connect(self.unit_convert)

        self.uom_from = QComboBox()
        self.uom_from.addItems(['tb', 'gb', 'mb', 'kb', 'b'])

        self.uom_to = QComboBox()
        self.uom_to.addItems(['tb', 'gb', 'mb', 'kb', 'b'])

        uom_grid_layout = QGridLayout()
        uom_grid_layout.addWidget(convert_from_label, 0, 0)
        uom_grid_layout.addWidget(self.convert_from_line_edit, 0, 1)
        uom_grid_layout.addWidget(self.uom_from, 0, 2)
        uom_grid_layout.addWidget(convert_to_label, 1, 0)
        uom_grid_layout.addWidget(self.converted_to_label, 1, 1)
        uom_grid_layout.addWidget(self.uom_to, 1, 2)
        uom_grid_layout.addWidget(self.convert_button, 2, 1)

        v_layout = QVBoxLayout()
        v_layout.addLayout(uom_grid_layout)
        self.setLayout(v_layout)

    def unit_convert(self):
        if self.convert_from_line_edit.text():
            if self.uom_from.currentText() == self.uom_to.currentText():
                self.converted_to_label.setText(self.convert_from_line_edit.text())
            else:
                self._kb_convert()
        else:
            self._no_data()

    def _kb_convert(self):
        self.converted_to_label.setText(str(int(self.convert_from_line_edit.text()) * (
                1024 ** (self.uom_to.currentIndex() - self.uom_from.currentIndex()))))

    def _no_data(self):
        no_entry = QMessageBox()
        no_entry.setText('You must enter a value to convert.')
        no_entry.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
