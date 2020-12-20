from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os
moduledir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, moduledir) 
from fizzbuzzMod.fizzbuzz import FizzBuzz
from PyQt5.QtCore import *
import sys


class MainWindow(QMainWindow):
    
    def __init__(self, parent=None):

        super(MainWindow, self).__init__(parent)

        self.setFixedSize(480, 480)
        self.po01 = QSpinBox()
        self.po01.setMinimum(1)
        self.po03 = QSpinBox()
        self.po03.setMinimum(1)
        self.pt01 = QPushButton('Show')
        
        self.log01 = QTextEdit()
        self.log01.setReadOnly(True)
        
        self.mainLayout = QVBoxLayout()
        self.layout01 = QHBoxLayout()
        self.layout01.addWidget(self.po01, 1)
        self.layout01.addWidget(self.po03, 1)
        self.mainLayout.addLayout(self.layout01, 0)
        self.mainLayout.addWidget(self.pt01, 1)
        self.mainLayout.addWidget(self.log01, 1)
        self.mainLabel = QLabel()
        self.mainLabel.setLayout(self.mainLayout)
        self.mainLabel.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.mainLabel)

        self.pt01.clicked.connect(self.showfizzbuzz)
 
    def closeEvent(self, event):
        if not self.okToContinue():
            event.ignore()

    def okToContinue(self):
        reply = QMessageBox.question(self, "fizzbuzz",
                                     """<p>You are about to close fizzbuzz.
                                     <p>Quit?""",
                                     QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            return True
        return False
 
    def showfizzbuzz(self):
        self.log01.setText('\n'.join(FizzBuzz(self.po01.value(), self.po03.value()).fizzbuzz))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("fizzbuzz")
    form = MainWindow()
    form.show()
    app.exec_()
