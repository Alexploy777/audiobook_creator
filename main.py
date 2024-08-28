import sys
from PyQt5.QtWidgets import *
from gui import Ui_MainWindow  # Импортируем Ui_MainWindow из пакета gui


class AudiobookCreator(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(AudiobookCreator, self).__init__()
        self.ui = Ui_MainWindow()
        self.setupUi(self)
        self.setWindowTitle('Audiobook Creator')

        # Подключаем сигналы к слотам
        self.pushButton.clicked.connect(self.add_files)
        self.pushButton_2.clicked.connect(self.remove_selected_files)
        self.pushButton_upload_cover.clicked.connect(self.upload_cover)
        self.pushButton_convert.clicked.connect(self.convert_files)
        self.pushButton_stop_and_clean.clicked.connect(self.stop_and_clean)

    def add_files(self):
        # Реализация добавления файлов в listWidget
        pass

    def remove_selected_files(self):
        # Реализация удаления выбранных файлов из listWidget
        pass

    def upload_cover(self):
        # Реализация загрузки обложки
        pass

    def convert_files(self):
        # Реализация конвертации файлов
        pass

    def stop_and_clean(self):
        # Реализация остановки процесса и очистки данных
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = AudiobookCreator()
    w.show()
    sys.exit(app.exec_())