# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QMainWindow, QWidget, QLabel, QVBoxLayout, QPushButton
from PySide6.QtCore import Qt, QRect, QCoreApplication, QMetaObject
from PySide6.QtGui import QIcon, QFont, QPixmap
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
        self.layout_widget_about = QWidget(self.centralwidget)
        self.layout_widget_about.setGeometry(QRect(10, 10, 221, 81))
        self.layout_about = QVBoxLayout(self.layout_widget_about)
        self.layout_about.setContentsMargins(0, 0, 0, 0)

        self.label_logo = QLabel(self.layout_widget_about)
        self.pixmap = QPixmap(resource_path('icon.ico'))
        self.pixmap = self.pixmap.scaledToWidth(30, Qt.SmoothTransformation)
        self.label_logo.setPixmap(self.pixmap)
        self.layout_about.addWidget(self.label_logo, 0, Qt.AlignHCenter)

        self.title_font = QFont()
        self.title_font.setPointSize(13)
        self.font = QFont()
        self.font.setPointSize(10)

        self.label_title = QLabel(self.layout_widget_about)
        self.title_font.setStyleStrategy(QFont.PreferAntialias)
        self.label_title.setFont(self.title_font)
        self.label_title.setLayoutDirection(Qt.LeftToRight)
        self.layout_about.addWidget(self.label_title, 0, Qt.AlignHCenter)

        self.label_version = QLabel(self.layout_widget_about)
        self.label_version.setFont(self.font)
        self.label_version.setLayoutDirection(Qt.LeftToRight)
        self.layout_about.addWidget(self.label_version, 0, Qt.AlignHCenter)

        self.layout_widget_about_2 = QWidget(self.centralwidget)
        self.layout_widget_about_2.setGeometry(QRect(10, 100, 221, 81))
        self.layout_about_2 = QVBoxLayout(self.layout_widget_about_2)
        self.layout_about_2.setContentsMargins(0, 0, 0, 0)
        self.label_copyright = QLabel(self.layout_widget_about_2)
        self.label_copyright.setFont(self.font)
        self.label_copyright.setLayoutDirection(Qt.LeftToRight)
        self.layout_about_2.addWidget(self.label_copyright, 0, Qt.AlignHCenter)

        self.label_author = QLabel(self.layout_widget_about_2)
        self.label_author.setFont(self.font)
        self.label_author.setLayoutDirection(Qt.LeftToRight)
        self.layout_about_2.addWidget(self.label_author, 0, Qt.AlignHCenter)

        self.button_quit_about = QPushButton(self.layout_widget_about_2)
        self.layout_about_2.addWidget(self.button_quit_about)
        self.button_quit_about.setMinimumSize(100, 30)
        self.button_quit_about.setProperty('class', 'Aqua')

        self.setCentralWidget(self.centralwidget)
        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("AboutWindow", "About"))
        self.label_title.setText(QCoreApplication.translate("AboutWindow", "PyDebloatX"))
        self.label_version.setText(QCoreApplication.translate("AboutWindow", ""))
        self.label_copyright.setText(QCoreApplication.translate("AboutWindow", "Copyright") + " © 2020-2021")
        self.label_author.setText(QCoreApplication.translate("AboutWindow", "Anton Grouchtchak."))
        self.button_quit_about.setText(QCoreApplication.translate("AboutWindow", "OK"))
