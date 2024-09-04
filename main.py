import sys

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, \
    QMessageBox  # Импортируем класс QMainWindow и QApplication

from core.audio_processing import AudioProcessor  # Подключаем AudioProcessor из core/audio_processing.py
from core.audio_processing import convert_files
from core.metadata import MetadataManager  # Подключаем MetadataManager из core/metadata.py
from data.config import Config  # Подключаем Config из data/config
from data.file_manager import FileManager  # Подключаем FileManager из data/file_manager
from gui import Ui_MainWindow  # Подключаем класс MainWindow из gui.py


class ConvertThread(QThread):
    progress_updated = pyqtSignal(int)
    conversion_finished = pyqtSignal()

    def __init__(self, audio_processor, file_paths, output_path, bitrate):
        super().__init__()
        self.audio_processor = audio_processor
        self.file_paths = file_paths
        self.output_path = output_path
        self.bitrate = bitrate

    def run(self):
        self.audio_processor.combine_and_convert_to_m4b(self.file_paths, self.output_path, self.bitrate, self.update_progress)
        self.conversion_finished.emit()

    def update_progress(self, progress):
        self.progress_updated.emit(progress)


class AudiobookCreator(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(AudiobookCreator, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Audiobook Creator')

        Config.load_config()  # Загружаем конфигурацию при запуске приложения

        self.file_manager = FileManager()
        self.metadata_manager = MetadataManager()
        self.audio_processor = AudioProcessor(ffmpeg_path="external/ffmpeg.exe")  # Укажите путь к ffmpeg

        self.init_ui()

    def init_ui(self):
        self.comboBox_audio_quality.addItems(["64k", "128k", "256k", "320k"])  # Добавляем варианты битрейта
        self.comboBox_audio_quality.setCurrentText(Config.AUDIO_BITRATE)  # Устанавливаем текущее значение из Config

        self.comboBox_audio_quality.currentTextChanged.connect(self.update_audio_bitrate)

        self.pushButton.clicked.connect(self.add_files)
        self.pushButton_2.clicked.connect(self.remove_selected_files)
        self.pushButton_upload_cover.clicked.connect(self.upload_cover)
        self.pushButton_convert.clicked.connect(self.start_conversion) #
        self.pushButton_stop_and_clean.clicked.connect(self.stop_and_clean)

        self.listWidget.itemSelectionChanged.connect(self.display_metadata)

    def update_audio_bitrate(self, bitrate):
        Config.set_audio_bitrate(bitrate)

    def add_files(self):
        self.file_manager.add_files(self.listWidget)

    def remove_selected_files(self):
        if self.file_manager.remove_files(self.listWidget):
            self.metadata_manager.clear_metadata(
                self.lineEdit_title,
                self.lineEdit_artist,
                self.lineEdit_album,
                self.lineEdit_year,
                self.lineEdit_genre,
                self.label_cover_of_book
            )

    def display_metadata(self):
        selected_items = self.listWidget.selectedItems()
        if not selected_items:
            self.metadata_manager.clear_metadata(
                self.lineEdit_title,
                self.lineEdit_artist,
                self.lineEdit_album,
                self.lineEdit_year,
                self.lineEdit_genre,
                self.label_cover_of_book
            )
            return

        file_path = selected_items[0].text()
        metadata, audio = self.metadata_manager.extract_metadata(file_path)
        self.lineEdit_title.setText(metadata["title"])
        self.lineEdit_artist.setText(metadata["artist"])
        self.lineEdit_album.setText(metadata["album"])
        self.lineEdit_year.setText(metadata["year"])
        self.lineEdit_genre.setText(metadata["genre"])

        self.metadata_manager.extract_and_show_cover(audio, self.label_cover_of_book)

    def convert_files(self):
        pass

    def start_conversion(self):
        output_path, _ = QFileDialog.getSaveFileName(self, "Сохранить аудиокнигу", "", "M4B Files (*.m4b)")
        if not output_path:
            return

        bitrate = self.comboBox_audio_quality.currentText()
        file_paths = self.file_manager.file_paths

        self.thread = ConvertThread(self.audio_processor, file_paths, output_path, bitrate)
        self.thread.progress_updated.connect(self.update_progress)
        self.thread.conversion_finished.connect(self.conversion_finished)

        self.thread.start()


    # def convert_files_action(self):
    #     output_dir = QFileDialog.getExistingDirectory(self, "Выберите папку для сохранения")
    #     if output_dir:
    #         metadata_list = []
    #         for i in range(self.listWidget.count()):
    #             item = self.listWidget.item(i)
    #             file_path = item.text()
    #             metadata, _ = self.metadata_manager.extract_metadata(file_path)
    #             metadata_list.append(metadata)
    #
    #         convert_files(
    #             file_paths=self.file_manager.file_paths,
    #             output_dir=output_dir,
    #             cover_image_path=self.file_manager.cover_image_path,
    #             metadata_list=metadata_list,
    #             progress_callback=self.update_progress
    #         )

    def update_progress(self, value):
        self.progressBar.setValue(value)

    def conversion_finished(self):
        QMessageBox.information(self, "Готово", "Конвертация завершена!")
        self.progressBar.setValue(0)

    def stop_and_clean(self):
        pass


    def upload_cover(self):
        self.file_manager.upload_cover(self.label_cover_of_book)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = AudiobookCreator()
    w.show()
    sys.exit(app.exec_())