# core/metadata.py
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TCON, APIC

class MetadataManager:
    def extract_metadata(self, file_path):
        audio = MP3(file_path, ID3=ID3)
        metadata = {
            "title": audio.get("TIT2", "Unknown Title"),
            "artist": audio.get("TPE1", "Unknown Artist"),
            "album": audio.get("TALB", "Unknown Album"),
            "genre": audio.get("TCON", "Unknown Genre"),
            "cover": None
        }
        # Извлекаем обложку, если она есть
        for tag in audio.tags.values():
            if isinstance(tag, APIC):
                metadata["cover"] = tag.data
                break
        return metadata
