from PySide2 import QtWidgets

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Convertisseur de devises")
        self.setup_ui()

    def setup_ui(self):
        self.layout = QtWidgets.QHBoxLayout(self)
        self.combo_devisesFrom = QtWidgets.QComboBox()
        self.spin_montant = QtWidgets.QSpinBox()
        self.combo_devisesTo = QtWidgets.QComboBox()
        self.spin_montantConv = QtWidgets.QSpinBox()
        self.button_invert = QtWidgets.QPushButton("Convertir")
        self.layout.addWidget(self.combo_devisesFrom)
        self.layout.addWidget(self.spin_montant)
        self.layout.addWidget(self.combo_devisesTo)
        self.layout.addWidget(self.spin_montantConv)
        self.layout.addWidget(self.button_invert)

app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()