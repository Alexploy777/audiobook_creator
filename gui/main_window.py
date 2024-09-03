# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(563, 665)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ConversionSettingsPanel = QtWidgets.QGroupBox(self.centralwidget)
        self.ConversionSettingsPanel.setObjectName("ConversionSettingsPanel")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.ConversionSettingsPanel)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_audio_quality = QtWidgets.QLabel(self.ConversionSettingsPanel)
        self.label_audio_quality.setObjectName("label_audio_quality")
        self.verticalLayout_7.addWidget(self.label_audio_quality)
        self.comboBox_audio_quality = QtWidgets.QComboBox(self.ConversionSettingsPanel)
        self.comboBox_audio_quality.setObjectName("comboBox_audio_quality")
        self.verticalLayout_7.addWidget(self.comboBox_audio_quality)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.pushButton_output_file = QtWidgets.QPushButton(self.ConversionSettingsPanel)
        self.pushButton_output_file.setObjectName("pushButton_output_file")
        self.verticalLayout_8.addWidget(self.pushButton_output_file)
        self.label_output_file = QtWidgets.QLabel(self.ConversionSettingsPanel)
        self.label_output_file.setObjectName("label_output_file")
        self.verticalLayout_8.addWidget(self.label_output_file)
        self.gridLayout_2.addWidget(self.ConversionSettingsPanel, 1, 1, 1, 1)
        self.groupBox_files = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_files.setObjectName("groupBox_files")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_files)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_files)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.listWidget = QtWidgets.QListWidget(self.groupBox_files)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_files)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.gridLayout_2.addWidget(self.groupBox_files, 0, 0, 2, 1)
        self.MetadataPanel = QtWidgets.QGroupBox(self.centralwidget)
        self.MetadataPanel.setObjectName("MetadataPanel")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.MetadataPanel)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_book_name = QtWidgets.QLabel(self.MetadataPanel)
        self.label_book_name.setObjectName("label_book_name")
        self.verticalLayout_2.addWidget(self.label_book_name)
        self.lineEdit_title = QtWidgets.QLineEdit(self.MetadataPanel)
        self.lineEdit_title.setObjectName("lineEdit_title")
        self.verticalLayout_2.addWidget(self.lineEdit_title)
        self.verticalLayout_6.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_autor_name = QtWidgets.QLabel(self.MetadataPanel)
        self.label_autor_name.setObjectName("label_autor_name")
        self.verticalLayout_3.addWidget(self.label_autor_name)
        self.lineEdit_artist = QtWidgets.QLineEdit(self.MetadataPanel)
        self.lineEdit_artist.setObjectName("lineEdit_artist")
        self.verticalLayout_3.addWidget(self.lineEdit_artist)
        self.verticalLayout_6.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_album_name = QtWidgets.QLabel(self.MetadataPanel)
        self.label_album_name.setObjectName("label_album_name")
        self.verticalLayout_4.addWidget(self.label_album_name)
        self.lineEdit_album = QtWidgets.QLineEdit(self.MetadataPanel)
        self.lineEdit_album.setObjectName("lineEdit_album")
        self.verticalLayout_4.addWidget(self.lineEdit_album)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_album_name_3 = QtWidgets.QLabel(self.MetadataPanel)
        self.label_album_name_3.setObjectName("label_album_name_3")
        self.verticalLayout_10.addWidget(self.label_album_name_3)
        self.lineEdit_year = QtWidgets.QLineEdit(self.MetadataPanel)
        self.lineEdit_year.setObjectName("lineEdit_year")
        self.verticalLayout_10.addWidget(self.lineEdit_year)
        self.verticalLayout_6.addLayout(self.verticalLayout_10)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_genre_name = QtWidgets.QLabel(self.MetadataPanel)
        self.label_genre_name.setObjectName("label_genre_name")
        self.verticalLayout_5.addWidget(self.label_genre_name)
        self.lineEdit_genre = QtWidgets.QLineEdit(self.MetadataPanel)
        self.lineEdit_genre.setObjectName("lineEdit_genre")
        self.verticalLayout_5.addWidget(self.lineEdit_genre)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_cover_of_book = QtWidgets.QLabel(self.MetadataPanel)
        self.label_cover_of_book.setMinimumSize(QtCore.QSize(150, 150))
        self.label_cover_of_book.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cover_of_book.setObjectName("label_cover_of_book")
        self.gridLayout.addWidget(self.label_cover_of_book, 2, 0, 1, 1)
        self.pushButton_upload_cover = QtWidgets.QPushButton(self.MetadataPanel)
        self.pushButton_upload_cover.setObjectName("pushButton_upload_cover")
        self.gridLayout.addWidget(self.pushButton_upload_cover, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout)
        self.gridLayout_2.addWidget(self.MetadataPanel, 0, 1, 1, 1)
        self.ControlPanel = QtWidgets.QGroupBox(self.centralwidget)
        self.ControlPanel.setObjectName("ControlPanel")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.ControlPanel)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_stop_and_clean = QtWidgets.QPushButton(self.ControlPanel)
        self.pushButton_stop_and_clean.setObjectName("pushButton_stop_and_clean")
        self.horizontalLayout.addWidget(self.pushButton_stop_and_clean)
        self.pushButton_convert = QtWidgets.QPushButton(self.ControlPanel)
        self.pushButton_convert.setObjectName("pushButton_convert")
        self.horizontalLayout.addWidget(self.pushButton_convert)
        self.gridLayout_2.addWidget(self.ControlPanel, 2, 0, 1, 2)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 563, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ConversionSettingsPanel.setTitle(_translate("MainWindow", "Панель настроек конвертации"))
        self.label_audio_quality.setText(_translate("MainWindow", "Качество аудио"))
        self.pushButton_output_file.setText(_translate("MainWindow", "выходной файл"))
        self.label_output_file.setText(_translate("MainWindow", "TextLabel"))
        self.groupBox_files.setTitle(_translate("MainWindow", "Файлы для обработки"))
        self.pushButton.setText(_translate("MainWindow", "Добавить файлы"))
        self.pushButton_2.setText(_translate("MainWindow", "Удалить выбранные"))
        self.MetadataPanel.setTitle(_translate("MainWindow", "Панель  метаданных"))
        self.label_book_name.setText(_translate("MainWindow", "Название книги"))
        self.label_autor_name.setText(_translate("MainWindow", "Автор"))
        self.label_album_name.setText(_translate("MainWindow", "Альбом"))
        self.label_album_name_3.setText(_translate("MainWindow", "Год"))
        self.label_genre_name.setText(_translate("MainWindow", "Жанр"))
        self.label_cover_of_book.setText(_translate("MainWindow", "Photo"))
        self.pushButton_upload_cover.setText(_translate("MainWindow", "Загрузить обложку"))
        self.ControlPanel.setTitle(_translate("MainWindow", "Панель управления"))
        self.pushButton_stop_and_clean.setText(_translate("MainWindow", "Отменить и очистить"))
        self.pushButton_convert.setText(_translate("MainWindow", "Конвертировать"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
