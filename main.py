import sys
from PyQt5.QtWidgets import *
from gui import Ui_MainWindow  # Импортируем Ui_MainWindow из пакета gui


class AudiobookCreator(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(AudiobookCreator, self).__init__()
        self.ui = Ui_MainWindow()
        self.setupUi(self)
        self.setWindowTitle('Audiobook Creator')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = AudiobookCreator()
    w.show()
    sys.exit(app.exec_())