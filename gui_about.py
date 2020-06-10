# -*- coding: utf-8 -*-
from PyQt5.QtCore import Qt, QRect, QCoreApplication, QMetaObject
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QIcon, QFont, QPixmap


class Ui_AboutWindow(QMainWindow):
    def __init__(self):
        super(Ui_AboutWindow, self).__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.WindowCloseButtonHint)
        self.setWindowIcon(QIcon('icon.ico'))
        self.setFixedSize(240, 150)

    def setupUi(self):
        self.centralwidget = QWidget(self)
        self.centralwidget.setStyleSheet(open('style.css').read())
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 221, 81))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_logo = QLabel(self.verticalLayoutWidget)
        self.pixmap = QPixmap('icon.ico')
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
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 100, 221, 41))
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
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "About"))
        self.label_name.setText(_translate("MainWindow", "PyDebloatX"))
        self.label_version.setText(_translate("MainWindow", ""))
        self.label_copyright.setText(_translate("MainWindow", "Copyright © 2020 by"))
        self.label_author.setText(_translate("MainWindow", "Anton Grouchtchak."))
