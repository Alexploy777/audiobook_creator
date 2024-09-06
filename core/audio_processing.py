import subprocess
import os

class AudioProcessor:
    def __init__(self, ffmpeg_path):
        self.ffmpeg_path = ffmpeg_path

    def convert_and_combine(self, file_paths, output_path, bitrate, metadata, cover_image, progress_callback):
        global cover_image_path
        # try:
        # Создаем временный список для всех аудиофайлов
        temp_list = "file_list.txt"
        with open(temp_list, 'w', encoding='utf-8') as f:
            for file_path in file_paths:
                f.write(f"file '{file_path}'\n")

        # Команда ffmpeg для объединения аудио файлов
        intermediate_audio = 'intermediate.mp3'
        command = [
            self.ffmpeg_path, '-y', '-f', 'concat', '-safe', '0', '-i', temp_list,
            '-c', 'copy'
        ]

        # Добавляем метаданные к команде (они должны быть ДО вывода файла)
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

        command.append(intermediate_audio)  # Добавление выходного файла

        # Выполнение команды
        try:
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
            if process.returncode != 0:
                raise RuntimeError(f"Ошибка при объединении аудио файлов: {stderr.decode('utf-8')}")
            print(stdout.decode('utf-8'))
        except Exception as e:
            raise RuntimeError(f"Ошибка при выполнении команды: {e}")



        #Добавляем обложку (если есть)
        if cover_image:
            cover_image_path = "cover.jpg"
            with open(cover_image_path, 'wb') as f:
                f.write(cover_image)

            # Команда ffmpeg для добавления обложки
            command = [self.ffmpeg_path, '-i', intermediate_audio, '-i', cover_image_path, '-map', '0:0', '-map', '1:0', '-c:a',
                       'aac', '-b:a', bitrate, '-c:v', 'mjpeg', '-metadata:s:v', 'title="Album cover"', '-metadata:s:v',
                       'comment="Cover (Front)"', '-disposition:v', 'attached_pic', '-f', 'mp4']

            command.append(output_path)

            try:
                print('==========')
                process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                stdout, stderr = process.communicate()

                if process.returncode != 0:
                    raise RuntimeError(f"Ошибка при объединении аудио файлов: {stderr.decode('utf-8', 'ignore')}")
                print(stdout.decode('utf-8', 'ignore'))
            except UnicodeDecodeError as e:
                print(f"Ошибка кодировки: {e}")
            except Exception as e:
                raise RuntimeError(f"Ошибка при выполнении команды: {e}")

        #Удаляем временные файлы
        os.remove(temp_list)
        if cover_image:
            os.remove(cover_image_path)


# =======================
#             # Выполняем команду через subprocess
#             process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#
#             total_files = len(file_paths)
#             for i, _ in enumerate(file_paths, 1):
#                 progress = int((i / total_files) * 100)
#                 progress_callback(progress)
#
#             stdout, stderr = process.communicate()
#
#             if process.returncode != 0:
#                 raise Exception(f"Ошибка при конвертации: {stderr.decode('utf-8')}")
#
#             # Удаляем временные файлы
#             os.remove(temp_list)
#             if cover_image:
#                 os.remove(cover_image_path)
#
#         except Exception as e:
#             raise RuntimeError(f"Ошибка при конвертации и объединении файлов: {e}")
