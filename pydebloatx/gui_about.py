# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt, QRect, QCoreApplication, QMetaObject
from PyQt5.QtGui import QIcon, QFont, QPixmap
import sys
import os


def resource_path(relative_path):
    """Determine resource path if app is built or run natively."""
    if hasattr(sys, 'frozen'):
        return os.path.join(sys._MEIPASS, relative_path)  # skipcq: PYL-W0212
    return os.path.join(os.path.abspath('.'), relative_path)


class Ui_AboutWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.setWindowIcon(QIcon(resource_path('icon.ico')))
        self.setFixedSize(241, 190)

    def setupUi(self):
        self.centralwidget = QWidget(self)
        with open(resource_path('style.css'), 'r') as file:
            self.centralwidget.setStyleSheet(file.read())
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 221, 81))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_logo = QLabel(self.verticalLayoutWidget)
        self.pixmap = QPixmap(resource_path('icon.ico'))
        self.pixmap = self.pixmap.scaledToWidth(30, Qt.SmoothTransformation)
        self.label_logo.setPixmap(self.pixmap)
        self.verticalLayout.addWidget(self.label_logo, 0, Qt.AlignHCenter)
        self.label_name = QLabel(self.verticalLayoutWidget)
        font = QFont()
        font.setPointSize(13)
        font.setStyleStrategy(QFont.PreferAntialias)
        self.label_name.setFont(font)
        self.label_name.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout.addWidget(self.label_name, 0, Qt.AlignHCenter)
        self.label_version = QLabel(self.verticalLayoutWidget)
        font = QFont()
        font.setPointSize(10)
        self.label_version.setFont(font)
        self.label_version.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout.addWidget(self.label_version, 0, Qt.AlignHCenter)
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 100, 221, 81))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_copyright = QLabel(self.verticalLayoutWidget_2)
        font = QFont()
        font.setPointSize(10)
        self.label_copyright.setFont(font)
        self.label_copyright.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_2.addWidget(self.label_copyright, 0, Qt.AlignHCenter)
        self.label_author = QLabel(self.verticalLayoutWidget_2)
        font = QFont()
        font.setPointSize(10)
        self.label_author.setFont(font)
        self.label_author.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_2.addWidget(self.label_author, 0, Qt.AlignHCenter)
        self.button_quit_about = QPushButton(self.verticalLayoutWidget_2)
        self.verticalLayout_2.addWidget(self.button_quit_about)
        self.button_quit_about.setMinimumSize(100, 30)
        self.button_quit_about.setProperty('class', 'Aqua')

        with open(resource_path('style.css'), 'r') as file:
            self.button_quit_about.setStyleSheet(file.read())

        self.setCentralWidget(self.centralwidget)
        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("AboutWindow", "About"))
        self.label_name.setText(_translate("AboutWindow", "PyDebloatX"))
        self.label_version.setText(_translate("AboutWindow", ""))
        self.label_copyright.setText(_translate("AboutWindow", "Copyright") + " © 2020-2021")
        self.label_author.setText(_translate("AboutWindow", "Anton Grouchtchak."))
        self.button_quit_about.setText(_translate("AboutWindow", "OK"))
