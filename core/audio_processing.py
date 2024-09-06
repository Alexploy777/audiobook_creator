import subprocess
import os

class AudioProcessor:
    def __init__(self, ffmpeg_path):
        self.ffmpeg_path = ffmpeg_path

    def convert_and_combine(self, file_paths, output_path, bitrate, metadata, cover_image, progress_callback):
        # Создаем временный список для всех аудиофайлов
        temp_list = "file_list.txt"
        with open(temp_list, 'w', encoding='utf-8') as f:
            f.writelines(f"file '{file_path}'\n" for file_path in file_paths)

        # Команда ffmpeg для объединения аудио файлов и добавления метаданных
        intermediate_audio = 'intermediate.mp3'
        command = [
            self.ffmpeg_path, '-y', '-f', 'concat', '-safe', '0', '-i', temp_list,
            '-c', 'copy', *self._get_metadata(metadata), intermediate_audio
        ]

        # Выполнение команды объединения
        self._run_command(command, "Ошибка при объединении аудио файлов")

        # Добавление обложки (если есть)
        if cover_image:
            cover_image_path = "cover.jpg"
            with open(cover_image_path, 'wb') as f:
                f.write(cover_image)

            # Команда ffmpeg для добавления обложки
            command = [
                self.ffmpeg_path, '-i', intermediate_audio, '-i', cover_image_path,
                '-map', '0:0', '-map', '1:0', '-c:a', 'aac', '-b:a', bitrate,
                '-c:v', 'mjpeg', '-metadata:s:v', 'title="Album cover"',
                '-metadata:s:v', 'comment="Cover (Front)"', '-disposition:v', 'attached_pic',
                '-f', 'mp4', output_path
            ]

            # Выполнение команды добавления обложки
            self._run_command(command, "Ошибка при добавлении обложки")

        # Удаление временных файлов
        os.remove(temp_list)
        if cover_image:
            os.remove(cover_image_path)

    def _get_metadata(self, metadata):
        return [f'-metadata {key}={value}' for key, value in metadata.items() if value]

    def _run_command(self, command, error_message):
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if process.returncode != 0:
            raise RuntimeError(f"{error_message}: {stderr.decode('utf-8', 'ignore')}")
        print(stdout.decode('utf-8', 'ignore'))
