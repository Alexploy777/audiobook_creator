from PyQt5.QtWidgets import QMainWindow

from core.metadata import MetadataManager
from data.file_manager import FileManager
from gui import Ui_MainWindow


class AudiobookCreator(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(AudiobookCreator, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Audiobook Creator')

        self.file_manager = FileManager()
        self.metadata_manager = MetadataManager()
        self.init_ui()

    def init_ui(self):
        self.pushButton.clicked.connect(self.add_files)
        self.pushButton_2.clicked.connect(self.remove_selected_files)
        self.pushButton_upload_cover.clicked.connect(self.upload_cover)
        self.pushButton_convert.clicked.connect(self.convert_files)
        self.pushButton_stop_and_clean.clicked.connect(self.stop_and_clean)

        self.cover_image_path = None
        self.listWidget.itemSelectionChanged.connect(self.display_metadata)

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
