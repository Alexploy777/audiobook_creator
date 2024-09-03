from PyQt5.QtWidgets import QFileDialog, QMessageBox

class FileManager:
    def __init__(self):
        self.file_paths = []

    def add_files(self, listWidget):
        options = QFileDialog.Options()
        file_paths, _ = QFileDialog.getOpenFileNames(None, "Выберите MP3 файлы", "", "MP3 Files (*.mp3);;All Files (*)", options=options)
        if file_paths:
            for path in file_paths:
                if path not in self.file_paths:
                    self.file_paths.append(path)
                    listWidget.addItem(path)
                else:
                    QMessageBox.warning(None, "Предупреждение", f"Файл {path} уже добавлен.")
            if listWidget.count() > 0:
                listWidget.setCurrentRow(0)

    def remove_files(self, listWidget):
        selected_items = listWidget.selectedItems()
        if not selected_items:
            QMessageBox.warning(None, "Предупреждение", "Нет выбранных файлов для удаления.")
            return

        for item in selected_items:
            file_path = item.text()
            if file_path in self.file_paths:
                self.file_paths.remove(file_path)
            listWidget.takeItem(listWidget.row(item))

        if not self.file_paths:
            return True
        return False
