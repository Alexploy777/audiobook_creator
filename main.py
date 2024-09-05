import sys

from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
# from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from mutagen.id3 import ID3, APIC
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

from gui import Ui_MainWindow  # Импортируем Ui_MainWindow из пакета gui


class AudiobookCreator(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(AudiobookCreator, self).__init__()
        # self.ui = Ui_MainWindow()
        self.setupUi(self)
        self.setWindowTitle('Audiobook Creator')

        # Подключаем сигналы к слотам
        self.pushButton.clicked.connect(self.add_files)
        self.pushButton_2.clicked.connect(self.remove_selected_files)
        self.pushButton_upload_cover.clicked.connect(self.upload_cover)
        self.pushButton_convert.clicked.connect(self.convert_files)
        self.pushButton_stop_and_clean.clicked.connect(self.stop_and_clean)

        self.file_paths = []  # Список для хранения путей к файлам
        self.cover_image_path = None  # Путь к изображению обложки

    def add_files(self):
        # Реализация добавления файлов в listWidget
        options = QFileDialog.Options()
        file_paths, _ = QFileDialog.getOpenFileNames(self, "Выберите файлы", "", "MP3 Files (*.mp3);;All Files (*)", options=options)
        if file_paths:
            for path in file_paths:
                if path not in self.file_paths:
                    self.file_paths.append(path)
                    self.listWidget.addItem(path)
                else:
                    QMessageBox.warning(self, "Предупреждение", f"Файл {path} уже добавлен.")

        if file_paths:
            self.extract_and_show_cover(file_paths[0])
            self.extract_metadata(file_paths[0])


    def extract_and_show_cover(self, file_path):
        try:
            audio = ID3(file_path)
            for tag in audio.values():
                if isinstance(tag, APIC):
                    image_data = tag.data
                    image = QPixmap()
                    image.loadFromData(image_data)
                    if image.isNull():
                        QMessageBox.warning(self, "Ошибка", "Не удалось загрузить изображение обложки.")
                    else:
                        self.label_cover_of_book.setPixmap(
                            image.scaled(self.label_cover_of_book.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio))
                    break
            else:
                # Нет обложки в метаданных
                self.label_cover_of_book.clear()
                QMessageBox.information(self, "Информация", "Обложка не найдена в выбранном файле.")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка при извлечении обложки: {str(e)}")

    def extract_metadata(self, file_path):
        audio = MP3(file_path, ID3=EasyID3)

        # Извлечение метаданных
        book_title = audio.get('title', [''])[0]
        author_name = audio.get('artist', [''])[0]
        album_name = audio.get('album', [''])[0]
        year = audio.get('date', [''])[0]
        genre = audio.get('genre', [''])[0]

        # Установка значений в поля интерфейса
        self.lineEdit_title.setText(book_title)
        self.lineEdit_artist.setText(author_name)
        self.lineEdit_album.setText(album_name)
        self.lineEdit_year.setText(year)
        self.lineEdit_genre.setText(genre)


    def remove_selected_files(self):
        # Реализация удаления выбранных файлов из listWidget
        selected_items = self.listWidget.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Предупреждение", "Нет выбранных файлов для удаления.")
            return

        for item in selected_items:
            self.file_paths.remove(item.text())
            self.listWidget.takeItem(self.listWidget.row(item))



    def upload_cover(self):
        # Реализация загрузки обложки
        options = QFileDialog.Options()
        cover_image_path, _ = QFileDialog.getOpenFileName(self, "Выберите изображение обложки", "",
                                                          "Images (*.png *.jpg *.bmp);;All Files (*)", options=options)


        if cover_image_path:
            # Показать изображение
            self.cover_image_path = cover_image_path
            pixmap = QPixmap(cover_image_path)
            if pixmap.isNull():
                QMessageBox.warning(self, "Ошибка", "Не удалось загрузить изображение.")
            else:
                self.label_cover_of_book.setPixmap(
                    pixmap.scaled(self.label_cover_of_book.size(), aspectRatioMode=QtCore.Qt.KeepAspectRatio))
        else:
            QMessageBox.warning(self, "Предупреждение", "Изображение не выбрано.")

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