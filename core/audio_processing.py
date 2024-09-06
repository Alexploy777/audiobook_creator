import subprocess
import os

class AudioProcessor:
    def __init__(self, ffmpeg_path="ffmpeg"):
        self.ffmpeg_path = ffmpeg_path

    def convert_and_combine(self, file_paths, output_path, bitrate, metadata, cover_image, progress_callback):
        try:
            # Создаем временный список для всех аудиофайлов
            temp_list = "file_list.txt"
            with open(temp_list, 'w', encoding='utf-8') as f:
                for file_path in file_paths:
                    f.write(f"file '{file_path}'\n")

            # Подготавливаем команду для ffmpeg
            command = [
                self.ffmpeg_path, '-y', '-f', 'concat', '-safe', '0', '-i', temp_list,
                '-b:a', bitrate, '-vn', '-c:a', 'aac', output_path
            ]

            # Добавляем метаданные к команде
            if metadata["title"]:
                command.extend(['-metadata', f"title={metadata['title']}"])
            if metadata["artist"]:
                command.extend(['-metadata', f"artist={metadata['artist']}"])
            if metadata["album"]:
                command.extend(['-metadata', f"album={metadata['album']}"])
            if metadata["year"]:
                command.extend(['-metadata', f"year={metadata['year']}"])
            if metadata["genre"]:
                command.extend(['-metadata', f"genre={metadata['genre']}"])

            # Добавляем обложку (если есть)
            if cover_image:
                cover_image_path = "cover.jpg"
                with open(cover_image_path, 'wb') as f:
                    f.write(cover_image)
                command.extend(['-i', cover_image_path, '-c:v', 'mjpeg'])

            # Выполняем команду через subprocess
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            total_files = len(file_paths)
            for i, _ in enumerate(file_paths, 1):
                progress = int((i / total_files) * 100)
                progress_callback(progress)

            stdout, stderr = process.communicate()

            if process.returncode != 0:
                raise Exception(f"Ошибка при конвертации: {stderr.decode('utf-8')}")

            # Удаляем временные файлы
            os.remove(temp_list)
            if cover_image:
                os.remove(cover_image_path)

        except Exception as e:
            raise RuntimeError(f"Ошибка при конвертации и объединении файлов: {e}")
