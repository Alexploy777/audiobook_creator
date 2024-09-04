import os
from pydub import AudioSegment
from mutagen.mp4 import MP4, MP4Cover
from PyQt5.QtCore import Qt
from data.config import Config # Подключаем Config из data/config


def convert_files(file_paths, output_dir, cover_image_path, metadata_list, progress_callback):
    try:
        # Настройки конвертации
        bit_rate = Config.AUDIO_BITRATE

        for index, file_path in enumerate(file_paths):
            # Чтение MP3 файла
            audio = AudioSegment.from_mp3(file_path)

            # Применение метаданных
            if metadata_list[index]:
                audio.export(
                    os.path.join(output_dir, f'{metadata_list[index]["title"]}.m4b'),
                    format='mp4',
                    bitrate=bit_rate,
                    tags={
                        'title': metadata_list[index]["title"],
                        'artist': metadata_list[index]["artist"],
                        'album': metadata_list[index]["album"],
                        'year': metadata_list[index]["year"],
                        'genre': metadata_list[index]["genre"]
                    }
                )

                # Добавление обложки
                if cover_image_path:
                    mp4_file = MP4(os.path.join(output_dir, f'{metadata_list[index]["title"]}.m4b'))
                    with open(cover_image_path, 'rb') as img_file:
                        cover_data = img_file.read()
                        mp4_file['covr'] = [MP4Cover(cover_data, imageformat=MP4Cover.FORMAT_JPEG)]
                    mp4_file.save()

            # Обновление прогресс-бара
            progress = int((index + 1) / len(file_paths) * 100)
            progress_callback(progress)

        progress_callback(100)  # Установка прогресса на 100% по завершению
    except Exception as e:
        raise RuntimeError(f"Ошибка при конвертации файлов: {str(e)}")
