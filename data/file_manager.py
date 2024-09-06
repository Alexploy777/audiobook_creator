# data/file_manager.py
from PyQt5.QtWidgets import QFileDialog, QListWidget

class FileManager:
    def __init__(self):
        self.file_paths = []  # Список выбранных MP3 файлов

    def add_files(self, list_widget: QListWidget):
        files, _ = QFileDialog.getOpenFileNames(None, "Выберите MP3 файлы", "", "MP3 Files (*.mp3)")
        if files:
            self.file_paths.extend(files)
            for file in files:
                list_widget.addItem(file)

    def remove_files(self, list_widget: QListWidget):
        selected_items = list_widget.selectedItems()
        if not selected_items:
            return False

        for item in selected_items:
            list_widget.takeItem(list_widget.row(item))
            self.file_paths.remove(item.text())

        return True

    def upload_cover(self, label_cover):
        cover_path, _ = QFileDialog.getOpenFileName(None, "Загрузить обложку", "", "Image Files (*.jpg *.jpeg *.png)")
        if cover_path:
            label_cover.setText(cover_path)  # Просто отображаем путь к обложке (позже будем загружать само изображение)

