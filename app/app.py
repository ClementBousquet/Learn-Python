from PySide2 import QtWidgets
import currency_converter

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.c = currency_converter.CurrencyConverter()
        self.setWindowTitle("Convertisseur de devises")
        self.setup_ui()
        self.set_default_values()

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


    def set_default_values(self):
        self.combo_devisesFrom.addItems(sorted(list(self.c.currencies)))
        self.combo_devisesTo.addItems(sorted(list(self.c.currencies)))
        self.combo_devisesFrom.setCurrentText("EUR")
        self.combo_devisesTo.setCurrentText("EUR")

        self.spin_montant.setRange(1, 1000000000)
        self.spin_montantConv.setRange(1, 1000000000)
        self.spin_montant.setValue(100)
        self.spin_montantConv.setValue(100)


app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()