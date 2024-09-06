from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TYER, TCON, APIC
from PyQt5.QtWidgets import QLabel

class MetadataManager:
    def extract_metadata(self, file_path):
        try:
            audio = MP3(file_path, ID3=ID3)
            metadata = {
                "title": self.get_tag(audio, TIT2, "Неизвестно"),
                "artist": self.get_tag(audio, TPE1, "Неизвестно"),
                "album": self.get_tag(audio, TALB, "Неизвестно"),
                "year": self.get_tag(audio, TYER, "Неизвестно"),
                "genre": self.get_tag(audio, TCON, "Неизвестно")
            }
            return metadata, audio
        except Exception as e:
            return {}, None

    def get_tag(self, audio, tag, default_value):
        try:
            return audio[tag].text[0] if tag in audio else default_value
        except Exception:
            return default_value

    def extract_and_show_cover(self, audio, label: QLabel):
        try:
            for tag in audio.tags.values():
                if isinstance(tag, APIC):
                    image_data = tag.data
                    label.setPixmap(image_data)  # Загружаем и отображаем обложку в QLabel
                    break
        except Exception:
            label.clear()  # Если не удалось загрузить обложку, очищаем QLabel

    def extract_cover_image(self, label: QLabel):
        pixmap = label.pixmap()
        if pixmap:
            image_data = pixmap.toImage()
            return image_data
        return None

    def clear_metadata(self, title, artist, album, year, genre, label_cover):
        title.clear()
        artist.clear()
        album.clear()
        year.clear()
        genre.clear()
        label_cover.clear()
