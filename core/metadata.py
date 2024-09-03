from PyQt5 import QtCore
from mutagen.id3 import ID3, APIC, ID3TimeStamp
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox

class MetadataManager:

    @staticmethod
    def extract_metadata(file_path):
        metadata = {
            "title": "",
            "artist": "",
            "album": "",
            "year": "",
            "genre": ""
        }
        try:
            audio = ID3(file_path)

            if 'TIT2' in audio:
                metadata["title"] = str(audio['TIT2'].text[0])

            if 'TPE1' in audio:
                metadata["artist"] = str(audio['TPE1'].text[0])

            if 'TALB' in audio:
                metadata["album"] = str(audio['TALB'].text[0])

            if 'TDRC' in audio:
                metadata["year"] = str(audio['TDRC'].text[0])

            if 'TCON' in audio:
                metadata["genre"] = str(audio['TCON'].text[0])

            return metadata, audio
        except Exception as e:
            return metadata, None

    @staticmethod
    def extract_and_show_cover(audio, label_cover_of_book):
        if audio is None:
            label_cover_of_book.clear()
            return

        try:
            for tag in audio.values():
                if isinstance(tag, APIC):
                    image_data = tag.data
                    pixmap = QPixmap()
                    pixmap.loadFromData(image_data)
                    if pixmap.isNull():
                        QMessageBox.warning(None, "Ошибка", "Не удалось загрузить изображение обложки.")
                    else:
                        label_cover_of_book.setPixmap(
                            pixmap.scaled(
                                label_cover_of_book.size(),
                                aspectRatioMode=QtCore.Qt.KeepAspectRatio
                            )
                        )
                    break
            else:
                label_cover_of_book.clear()
                QMessageBox.information(None, "Информация", "Обложка не найдена в выбранном файле.")
        except Exception as e:
            QMessageBox.critical(None, "Ошибка", f"Ошибка при извлечении обложки: {str(e)}")

    @staticmethod
    def clear_metadata(lineEdit_title, lineEdit_artist, lineEdit_album, lineEdit_year, lineEdit_genre, label_cover_of_book):
        lineEdit_title.clear()
        lineEdit_artist.clear()
        lineEdit_album.clear()
        lineEdit_year.clear()
        lineEdit_genre.clear()
        label_cover_of_book.clear()
