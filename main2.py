# main.py

from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QFileDialog, QMessageBox
)
from mutagen.id3 import ID3, APIC

from gui import Ui_MainWindow


class AudiobookCreator(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(AudiobookCreator, self).__init__()
        self.setupUi(self)

        # Подключение сигналов к слотам
        self.pushButton.clicked.connect(self.add_files)
        self.pushButton_2.clicked.connect(self.remove_selected_files)
        self.pushButton_upload_cover.clicked.connect(self.upload_cover)
        self.pushButton_convert.clicked.connect(self.convert_files)
        self.pushButton_stop_and_clean.clicked.connect(self.stop_and_clean)

        self.file_paths = []  # Список для хранения путей к файлам
        self.cover_image_path = None  # Путь к изображению обложки

        # Подключение сигнала выбора элемента списка к слоту
        self.listWidget.itemSelectionChanged.connect(self.display_metadata)

    def add_files(self):
        options = QFileDialog.Options()
        file_paths, _ = QFileDialog.getOpenFileNames(
            self,
            "Выберите MP3 файлы",
            "",
            "MP3 Files (*.mp3);;All Files (*)",
            options=options
        )

        if file_paths:
            for path in file_paths:
                if path not in self.file_paths:
                    self.file_paths.append(path)
                    self.listWidget.addItem(path)
                else:
                    QMessageBox.warning(self, "Предупреждение", f"Файл {path} уже добавлен.")

        # if file_paths:
        #     self.display_metadata()

    def remove_selected_files(self):
        selected_items = self.listWidget.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Предупреждение", "Нет выбранных файлов для удаления.")
            return

        for item in selected_items:
            file_path = item.text()
            if file_path in self.file_paths:
                self.file_paths.remove(file_path)
            self.listWidget.takeItem(self.listWidget.row(item))

        # Очистить метаданные и обложку, если удален последний файл
        if not self.file_paths:
            self.clear_metadata()

    def upload_cover(self):
        options = QFileDialog.Options()
        cover_image_path, _ = QFileDialog.getOpenFileName(
            self,
            "Выберите изображение обложки",
            "",
            "Images (*.png *.jpg *.bmp);;All Files (*)",
            options=options
        )

        if cover_image_path:
            # Показать изображение
            self.cover_image_path = cover_image_path
            pixmap = QPixmap(cover_image_path)
            if pixmap.isNull():
                QMessageBox.warning(self, "Ошибка", "Не удалось загрузить изображение.")
            else:
                self.label_cover_of_book.setPixmap(
                    pixmap.scaled(
                        self.label_cover_of_book.size(),
                        aspectRatioMode=QtCore.Qt.KeepAspectRatio
                    )
                )
        else:
            QMessageBox.warning(self, "Предупреждение", "Изображение не выбрано.")

    def convert_files(self):
        # Реализация метода для конвертации файлов
        pass

    def stop_and_clean(self):
        # Реализация метода для остановки и очистки
        pass

    def extract_metadata(self, file_path):
        metadata = {
            "title": "",
            "artist": "",
            "album": "",
            "year": "",
            "genre": ""
        }
        try:
            audio = ID3(file_path)

            # Извлечение названия (Title)
            if 'TIT2' in audio:
                metadata["title"] = audio['TIT2'].text[0]

            # Извлечение исполнителя (Artist)
            if 'TPE1' in audio:
                metadata["artist"] = audio['TPE1'].text[0]

            # Извлечение альбома (Album)
            if 'TALB' in audio:
                metadata["album"] = audio['TALB'].text[0]

            # Извлечение года выпуска (Year)
            if 'TDRC' in audio:
                metadata["year"] = str(audio['TDRC'].text[0])

            # Извлечение жанра (Genre)
            if 'TCON' in audio:
                metadata["genre"] = audio['TCON'].text[0]

            return metadata, audio
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка при извлечении метаданных: {str(e)}")
            return metadata, None

    def display_metadata(self):
        selected_items = self.listWidget.selectedItems()
        if not selected_items:
            self.clear_metadata()
            return

        # Для простоты отображаем метаданные первого выбранного файла
        file_path = selected_items[0].text()
        metadata, audio = self.extract_metadata(file_path)

        # Отображение метаданных в интерфейсе
        self.lineEdit_title.setText(metadata["title"])
        self.lineEdit_artist.setText(metadata["artist"])
        self.lineEdit_album.setText(metadata["album"])
        self.lineEdit_year.setText(metadata["year"])
        self.lineEdit_genre.setText(metadata["genre"])

        # Извлечение и отображение обложки
        self.extract_and_show_cover(audio, file_path)

    def extract_and_show_cover(self, file_path, audio):
        if audio is None:
            self.label_cover_of_book.clear()
            return

        try:
            # Ищем тег APIC (изображение обложки)
            for tag in audio.values():
                if isinstance(tag, APIC):
                    image_data = tag.data
                    pixmap = QPixmap()
                    pixmap.loadFromData(image_data)
                    if pixmap.isNull():
                        QMessageBox.warning(self, "Ошибка", "Не удалось загрузить изображение обложки.")
                    else:
                        self.label_cover_of_book.setPixmap(
                            pixmap.scaled(
                                self.label_cover_of_book.size(),
                                aspectRatioMode=QtCore.Qt.KeepAspectRatio
                            )
                        )
                    break
            else:
                # Нет обложки в метаданных
                self.label_cover_of_book.clear()
                QMessageBox.information(self, "Информация", "Обложка не найдена в выбранном файле.")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка при извлечении обложки: {str(e)}")

    def clear_metadata(self):
        self.lineEdit_title.clear()
        self.lineEdit_artist.clear()
        self.lineEdit_album.clear()
        self.lineEdit_year.clear()
        self.lineEdit_genre.clear()
        self.label_cover_of_book.clear()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    w = AudiobookCreator()
    w.show()
    sys.exit(app.exec_())
