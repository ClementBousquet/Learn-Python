from PySide2 import QtWidgets

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Convertisseur de devise")

app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()