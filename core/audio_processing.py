import subprocess
import os
from io import BytesIO

class AudioProcessor:
    def __init__(self, ffmpeg_path):
        self.ffmpeg_path = ffmpeg_path

    def convert_and_combine(self, file_paths, output_path, bitrate, metadata, cover_image, progress_callback):
        try:
            # Команда для объединения файлов через пайп и добавления метаданных
            command = [
                self.ffmpeg_path, '-y', '-f', 'concat', '-safe', '0', '-i', 'pipe:0',
                '-c', 'copy', *self._get_metadata(metadata), '-f', 'mp3', 'pipe:1'
            ]

            # Открываем процесс для записи данных в stdin и чтения результата через stdout
            process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            try:
                # Передача аудиофайлов через пайп в ffmpeg
                for file_path in file_paths:
                    with open(file_path, 'rb') as audio_file:
                        while True:
                            chunk = audio_file.read(1024)  # читаем по 1024 байта
                            if not chunk:
                                break
                            process.stdin.write(chunk)  # запись в stdin процесса

                process.stdin.close()  # закрываем stdin для сигнала завершения ввода

                # Следим за прогрессом и выводом ошибок
                self._monitor_progress(process.stderr, progress_callback)

                # Читаем результат процесса
                intermediate_audio = process.stdout.read()

                # Дожидаемся завершения процесса
                return_code = process.wait()

                if return_code != 0:
                    stderr_output = process.stderr.read().decode('utf-8', 'ignore')
                    raise RuntimeError(f"FFmpeg завершился с ошибкой: {stderr_output}")

            except Exception as e:
                process.kill()
                raise RuntimeError(f"Ошибка при выполнении команды: {e}")

        except BrokenPipeError:
            raise RuntimeError("Ошибка: пайп был закрыт до завершения передачи данных.")

        # Добавление обложки (если есть)
        if cover_image:
            self._add_cover(intermediate_audio, cover_image, output_path, bitrate, metadata)


    def _add_cover(self, audio_data, cover_image, output_path, bitrate, metadata):
        # Используем пайпы для передачи обложки и аудиоданных
        command = [
            self.ffmpeg_path, '-i', 'pipe:0', '-i', 'pipe:1', '-map', '0:0', '-map', '1:0',
            '-c:a', 'aac', '-b:a', bitrate, '-c:v', 'mjpeg', '-metadata:s:v', 'title="Album cover"',
            '-metadata:s:v', 'comment="Cover (Front)"', '-disposition:v', 'attached_pic',
            '-f', 'mp4', output_path
        ]

        with subprocess.Popen(command, stdin=subprocess.PIPE, stderr=subprocess.PIPE) as process:
            # Передаем аудиоданные и данные обложки через пайп
            process.stdin.write(audio_data)
            process.stdin.write(cover_image)
            process.stdin.close()

            # Мониторим прогресс
            self._monitor_progress(process.stderr, lambda p: print(f"Adding cover: {p}%"))

    def _monitor_progress(self, stderr_pipe, progress_callback):
        # Читаем вывод stderr для получения информации о прогрессе
        while True:
            line = stderr_pipe.readline()
            if not line:
                break

            # Пример строки вывода ffmpeg, откуда можно извлечь прогресс:
            # "size=  12345kB time=00:01:23.45 bitrate= 123.4kbits/s speed=1.23x"
            if b'time=' in line:
                # Извлекаем текущий прогресс
                time_str = line.split(b'time=')[1].split()[0].decode('utf-8')
                progress = self._parse_ffmpeg_time(time_str)
                progress_callback(progress)

    def _parse_ffmpeg_time(self, time_str):
        # Преобразуем строку времени "00:01:23.45" в прогресс (в процентах)
        h, m, s = map(float, time_str.split(':'))
        total_seconds = h * 3600 + m * 60 + s
        return int((total_seconds / self.total_duration) * 100)

    def _get_metadata(self, metadata):
        result = []
        for key, value in metadata.items():
            if value:
                result.extend(['-metadata', f"{key}={value}"])
        return result
