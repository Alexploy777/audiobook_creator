import os
from pydub import AudioSegment
from mutagen.mp4 import MP4, MP4Cover

class AudioProcessor:
    def __init__(self, ffmpeg_path):
        self.ffmpeg_path = ffmpeg_path
        AudioSegment.converter = ffmpeg_path

    def convert_file_to_m4b(self, file_path, output_path, bitrate):
        audio = AudioSegment.from_mp3(file_path)
        audio.export(output_path, format="mp4", bitrate=bitrate, codec="aac")

    def combine_files(self, file_paths, output_path, progress_callback=None):
        combined = AudioSegment.empty()
        total_files = len(file_paths)

        for index, file_path in enumerate(file_paths):
            audio = AudioSegment.from_file(file_path, format="mp4")
            combined += audio

            # Обновляем прогресс на этапе объединения
            if progress_callback:
                progress = int((index + 1) / total_files * 100)
                progress_callback(progress)

        combined.export(output_path, format="mp4", codec="aac")

    def add_cover_and_metadata(self, output_path, metadata, cover_image_bytes=None):
        audio = MP4(output_path)

        # Добавление метаданных
        audio['\xa9nam'] = metadata.get("title")
        audio['\xa9ART'] = metadata.get("artist")
        audio['\xa9alb'] = metadata.get("album")
        audio['\xa9day'] = metadata.get("year")
        audio['\xa9gen'] = metadata.get("genre")

        # Добавление обложки из байтов
        if cover_image_bytes:
            cover = MP4Cover(cover_image_bytes, imageformat=MP4Cover.FORMAT_JPEG)
            audio['covr'] = [cover]

        audio.save()

    def convert_and_combine(self, mp3_files, output_path, bitrate, metadata, cover_image_bytes=None, progress_callback=None):
        total_steps = len(mp3_files) + 1  # +1 for combining step
        step_progress = 100 // total_steps

        converted_files = []
        for index, mp3_file in enumerate(mp3_files):
            temp_output = os.path.splitext(mp3_file)[0] + "_temp.m4b"
            self.convert_file_to_m4b(mp3_file, temp_output, bitrate)
            converted_files.append(temp_output)

            # Обновляем прогресс после каждого конвертированного файла
            if progress_callback:
                progress = (index + 1) * step_progress
                progress_callback(progress)

        # Объединение всех временных m4b файлов
        self.combine_files(converted_files, output_path, progress_callback)

        # Добавление метаданных и обложки
        self.add_cover_and_metadata(output_path, metadata, cover_image_bytes)

        # Удаление временных файлов
        for temp_file in converted_files:
            os.remove(temp_file)

        # Устанавливаем прогресс на 100% по завершении
        if progress_callback:
            progress_callback(100)
