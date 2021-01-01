# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QFrame, QShortcut, QPushButton, QMainWindow, QWidget, QLabel, QVBoxLayout, QCheckBox, \
    QHBoxLayout, QProgressBar, QToolTip
from PyQt5.QtCore import Qt, QRect, QCoreApplication, QMetaObject, QSize
from PyQt5.QtGui import QIcon, QKeySequence, QFont
import os
import sys

# Determines resource path if app is built or run natively
def resource_path(relative_path):
    if hasattr(sys, 'frozen'):
        return os.path.join(sys._MEIPASS, relative_path) # skipcq: PYL-W0212
    return os.path.join(os.path.abspath('.'), relative_path)

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setWindowIcon(QIcon(resource_path('icon.ico')))
        self.setFixedSize(531, 470)

    def setupUi(self):
        self.centralwidget = QWidget(self)
        with open(resource_path('style.css'), 'r') as file:
            self.centralwidget.setStyleSheet(file.read())
        self.appswidget = QWidget(self.centralwidget)
        self.appswidget.setGeometry(50, 0, 481, 470)
        self.appswidget.setProperty('class', 'appswidget')
        self.sidebar = QFrame(self)
        self.sidebar.setFrameShape(QFrame.StyledPanel)
        self.sidebar.setGeometry(0, 0, 50, 470)
        self.sidebar.setProperty('class', 'sidebar')

        self.refresh_btn = QPushButton(self.sidebar)
        self.refresh_btn.setGeometry(QRect(0, 0, 51, 51))
        self.refresh_btn.setProperty('class', 'sidebar_btns')
        self.refresh_btn.setIcon(QIcon(':/icon/refresh_icon.png'))
        self.refresh_btn.setIconSize(QSize(24, 24))
        self.refresh_bind = QShortcut(QKeySequence('Ctrl+R'), self)

        self.store_btn = QPushButton(self.sidebar)
        self.store_btn.setGeometry(QRect(0, 51, 51, 51))
        self.store_btn.setProperty('class', 'sidebar_btns')
        self.store_btn.setIcon(QIcon(':/icon/store_icon.png'))
        self.store_btn.setIconSize(QSize(24, 24))
        self.store_bind = QShortcut(QKeySequence('Ctrl+S'), self)

        self.homepage_btn = QPushButton(self.sidebar)
        self.homepage_btn.setGeometry(QRect(0, 102, 51, 51))
        self.homepage_btn.setProperty('class', 'sidebar_btns')
        self.homepage_btn.setIcon(QIcon(':/icon/github_icon.png'))
        self.homepage_btn.setIconSize(QSize(24, 24))
        self.homepage_bind = QShortcut(QKeySequence('Ctrl+G'), self)

        self.about_btn = QPushButton(self.sidebar)
        self.about_btn.setGeometry(QRect(0, 153, 51, 51))
        self.about_btn.setProperty('class', 'sidebar_btns')
        self.about_btn.setIcon(QIcon(':/icon/about_icon.png'))
        self.about_btn.setIconSize(QSize(24, 24))
        self.about_bind = QShortcut(QKeySequence('Ctrl+A'), self)

        self.quit_btn = QPushButton(self.sidebar)
        self.quit_btn.setGeometry(QRect(0, 420, 51, 51))
        self.quit_btn.setProperty('class', 'sidebar_btns_quit')
        self.quit_btn.setIcon(QIcon(':/icon/quit_icon.png'))
        self.quit_btn.setIconSize(QSize(24, 24))
        self.quit_bind = QShortcut(QKeySequence('Ctrl+Q'), self)

        self.font = QFont()
        self.font.setPointSize(8)
        self.font.setStyleStrategy(QFont.PreferAntialias)

        self.label_refresh = QLabel(self.appswidget)
        self.label_refresh.setFont(self.font)
        self.label_refresh.setGeometry(QRect(20, 10, 441, 15))

        self.label_info = QLabel(self.appswidget)
        self.label_info.setFont(self.font)
        self.label_info.setGeometry(QRect(20, 15, 441, 30))

        self.progressbar = QProgressBar(self.appswidget)
        self.progressbar.setGeometry(QRect(20, 35, 441, 20))

        self.verticalLayoutWidget = QWidget(self.appswidget)
        self.verticalLayoutWidget.setGeometry(QRect(20, 55, 121, 311))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_2 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_3 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_4 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_5 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_6 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_7 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_8 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_9 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_10 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_11 = QCheckBox(self.verticalLayoutWidget)
        checkbox_column_1 = (self.checkBox, self.checkBox_2, self.checkBox_3, self.checkBox_4, self.checkBox_5, self.checkBox_6,
                             self.checkBox_7, self.checkBox_8, self.checkBox_9, self.checkBox_10, self.checkBox_11
                             )
        for checkbox in checkbox_column_1:
            self.verticalLayout.addWidget(checkbox)

        self.verticalLayoutWidget_2 = QWidget(self.appswidget)
        self.verticalLayoutWidget_2.setGeometry(QRect(170, 55, 131, 311))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.checkBox_12 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_13 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_14 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_15 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_16 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_17 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_18 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_19 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_20 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_21 = QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_22 = QCheckBox(self.verticalLayoutWidget_2)
        checkbox_column_2 = (self.checkBox_12, self.checkBox_13, self.checkBox_14, self.checkBox_15, self.checkBox_16, self.checkBox_17,
                             self.checkBox_18, self.checkBox_19, self.checkBox_20, self.checkBox_21, self.checkBox_22
                             )
        for checkbox in checkbox_column_2:
            self.verticalLayout_2.addWidget(checkbox)

        self.verticalLayoutWidget_3 = QWidget(self.appswidget)
        self.verticalLayoutWidget_3.setGeometry(QRect(330, 55, 131, 311))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.checkBox_23 = QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_24 = QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_25 = QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_26 = QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_27 = QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_28 = QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_29 = QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_30 = QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_31 = QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_32 = QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_33 = QCheckBox(self.verticalLayoutWidget_3)
        checkbox_column_3 = (self.checkBox_23, self.checkBox_24, self.checkBox_25, self.checkBox_26, self.checkBox_27, self.checkBox_28,
                             self.checkBox_29, self.checkBox_30, self.checkBox_31, self.checkBox_32, self.checkBox_33
                             )
        for checkbox in checkbox_column_3:
            self.verticalLayout_3.addWidget(checkbox)

        self.label_note = QLabel(self.appswidget)
        self.label_note.setFont(self.font)
        self.label_note.setGeometry(QRect(20, 370, 350, 16))
        self.label_space = QLabel(self.appswidget)
        self.label_space.setFont(self.font)
        self.label_space.setGeometry(QRect(20, 390, 350, 16))
        self.label_size = QLabel(self.appswidget)
        self.label_size.setFont(self.font)
        self.label_size.setGeometry(QRect(155, 390, 200, 16))

        self.horizontalLayoutWidget_2 = QWidget(self.appswidget)
        self.horizontalLayoutWidget_2.setGeometry(QRect(20, 420, 220, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.button_select_all = QPushButton(self.horizontalLayoutWidget_2)
        self.button_select_all.setIcon(QIcon(':/icon/no_check_icon.png'))
        self.button_select_all.setIconSize(QSize(18, 18))
        self.button_select_all.setLayoutDirection(Qt.RightToLeft)
        self.horizontalLayout_2.addWidget(self.button_select_all)
        self.button_select_all.setMinimumSize(100, 30)
        self.button_select_all.setProperty('class', 'Aqua')
        self.button_deselect_all = QPushButton(self.horizontalLayoutWidget_2)
        self.button_deselect_all.setIcon(QIcon(':/icon/no_cancel_icon.png'))
        self.button_deselect_all.setIconSize(QSize(18, 18))
        self.button_deselect_all.setLayoutDirection(Qt.RightToLeft)
        self.horizontalLayout_2.addWidget(self.button_deselect_all)
        self.button_deselect_all.setMinimumSize(100, 30)
        self.button_deselect_all.setProperty('class', 'Aqua')

        self.horizontalLayoutWidget = QWidget(self.appswidget)
        self.horizontalLayoutWidget.setGeometry(QRect(354, 420, 107, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.button_uninstall = QPushButton(self.horizontalLayoutWidget)
        self.button_uninstall.setIcon(QIcon(':/icon/no_trash_icon.png'))
        self.button_uninstall.setIconSize(QSize(18, 18))
        self.button_uninstall.setLayoutDirection(Qt.RightToLeft)
        self.horizontalLayout.addWidget(self.button_uninstall)
        self.button_uninstall.setMinimumSize(100, 30)
        self.button_uninstall.setProperty('class', 'Grapefruit')

        with open(resource_path('style.css'), 'r') as file:
            widgets = (self.sidebar, self.refresh_btn, self.homepage_btn, self.about_btn, self.quit_btn,
                       self.progressbar, self.button_select_all, self.button_deselect_all, self.button_uninstall
                       )
            for widget in widgets:
                widget.setStyleSheet(file.read())

        self.setCentralWidget(self.centralwidget)
        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QCoreApplication.translate

        self.setWindowTitle(_translate("MainWindow", "PyDebloatX"))
        self.label_info.setText(_translate("MainWindow", "Refreshing list of installed apps..."))

        self.checkBox.setText(_translate("MainWindow", "3D Builder"))
        self.checkBox_2.setText(_translate("MainWindow", "3D Viewer"))
        self.checkBox_3.setText(_translate("MainWindow", "Alarms and Clock"))
        self.checkBox_4.setText(_translate("MainWindow", "Calculator"))
        self.checkBox_5.setText(_translate("MainWindow", "Calendar and Mail"))
        self.checkBox_6.setText(_translate("MainWindow", "Camera"))
        self.checkBox_7.setText(_translate("MainWindow", "Get Help"))
        self.checkBox_8.setText(_translate("MainWindow", "Groove Music"))
        self.checkBox_9.setText(_translate("MainWindow", "Maps"))
        self.checkBox_10.setText(_translate("MainWindow", "Messaging"))
        self.checkBox_11.setText(_translate("MainWindow", "Mixed Reality Portal"))

        self.checkBox_12.setText(_translate("MainWindow", "Mobile Plans"))
        self.checkBox_13.setText(_translate("MainWindow", "Money"))
        self.checkBox_14.setText(_translate("MainWindow", "Movies && TV"))
        self.checkBox_15.setText(_translate("MainWindow", "News"))
        self.checkBox_16.setText(_translate("MainWindow", "Office"))
        self.checkBox_17.setText(_translate("MainWindow", "OneNote"))
        self.checkBox_18.setText(_translate("MainWindow", "Paint 3D"))
        self.checkBox_19.setText(_translate("MainWindow", "People"))
        self.checkBox_20.setText(_translate("MainWindow", "Photos"))
        self.checkBox_21.setText(_translate("MainWindow", "Skype"))
        self.checkBox_22.setText(_translate("MainWindow", "Snip && Sketch"))

        self.checkBox_23.setText(_translate("MainWindow", "Solitaire"))
        self.checkBox_24.setText(_translate("MainWindow", "Sports"))
        self.checkBox_25.setText(_translate("MainWindow", "Spotify"))
        self.checkBox_26.setText(_translate("MainWindow", "Sticky Notes"))
        self.checkBox_27.setText(_translate("MainWindow", "Tips"))
        self.checkBox_28.setText(_translate("MainWindow", "Voice Recorder"))
        self.checkBox_29.setText(_translate("MainWindow", "Weather"))
        self.checkBox_30.setText(_translate("MainWindow", "Windows Feedback"))
        self.checkBox_31.setText(_translate("MainWindow", "Xbox"))
        self.checkBox_32.setText(_translate("MainWindow", "Xbox Game Bar"))
        self.checkBox_33.setText(_translate("MainWindow", "Your Phone"))

        self.label_note.setText(_translate("MainWindow", "NOTE: Microsoft Edge and Cortana cannot be uninstalled using this GUI."))
        self.label_space.setText(_translate("MainWindow", "Total amount of disk space:"))
        self.label_size.setText(_translate("MainWindow", "0 MB"))

        self.button_select_all.setText(_translate("MainWindow", "Select All"))
        self.button_deselect_all.setText(_translate("MainWindow", "Deselect All"))

        self.button_uninstall.setText(_translate("MainWindow", "Uninstall"))

        QToolTip.setFont(self.font)
        self.checkBox.setToolTip('View, create, and personalize 3D objects.')
        self.checkBox_2.setToolTip('View 3D models and animations in real-time.')
        self.checkBox_3.setToolTip('A combination of alarm clock, world clock, timer, and stopwatch.')
        self.checkBox_4.setToolTip('A calculator that includes standard, scientific, and programmer modes, as well as a unit converter.')
        self.checkBox_5.setToolTip('Stay up to date with email and schedule managing.')
        self.checkBox_6.setToolTip('Point and shoot to take pictures on Windows 10.')
        self.checkBox_7.setToolTip('Provide a way to ask a question and get recommended solutions or contact assisted support.')
        self.checkBox_8.setToolTip('Listen to music on Windows, iOS, and Android devices.')
        self.checkBox_9.setToolTip('Search for places to get directions, business info, and reviews.')
        self.checkBox_10.setToolTip('Quick, reliable SMS, MMS and RCS messaging from your phone.')
        self.checkBox_11.setToolTip('Discover Windows Mixed Reality and dive into more than 3,000 games and VR experiences from Steam®VR and Microsoft Store.')

        self.checkBox_12.setToolTip('Sign up for a data plan and connect with mobile operators in your area. You will need a supported SIM card.')
        self.checkBox_13.setToolTip('Finance calculators, currency exchange rates and commodity prices from around the world.')
        self.checkBox_14.setToolTip('All your movies and TV shows, all in one place, on all your devices.')
        self.checkBox_15.setToolTip('Deliver breaking news and trusted, in-depth reporting from the world\'s best journalists.')
        self.checkBox_16.setToolTip('Find all your Office apps and files in one place.')
        self.checkBox_17.setToolTip('Digital notebook for capturing and organizing everything across your devices.')
        self.checkBox_18.setToolTip('Make 2D masterpieces or 3D models that you can play with from all angles.')
        self.checkBox_19.setToolTip('Connect with all your friends, family, colleagues, and acquaintances in one place.')
        self.checkBox_20.setToolTip('View and edit your photos and videos, make movies, and create albums.')
        self.checkBox_21.setToolTip('Instant message, voice or video call application.')
        self.checkBox_22.setToolTip('Quickly annotate screenshots, photos and other images and save, paste or share with other apps.')

        self.checkBox_23.setToolTip('Solitaire is one of the most played computer card games of all time.')
        self.checkBox_24.setToolTip('Live scores and in-depth game experiences for more than 150 leagues.')
        self.checkBox_25.setToolTip('Play your favorite songs and albums free on Windows 10 with Spotify.')
        self.checkBox_26.setToolTip('Create notes, type, ink or add a picture, add text formatting, or stick them to the desktop.')
        self.checkBox_27.setToolTip('Provide users with information and tips about operating system features.')
        self.checkBox_28.setToolTip('Record sounds, lectures, interviews, and other events.')
        self.checkBox_29.setToolTip('Latest weather conditions, accurate 10-day and hourly forecasts.')
        self.checkBox_30.setToolTip('Provide feedback about Windows and apps by sharing suggestions or problems.')
        self.checkBox_31.setToolTip('Browse the catalogue, view recommendations, and discover PC games with Xbox Game Pass.')
        self.checkBox_32.setToolTip('Instant access to widgets for screen capture and sharing, and chatting with Xbox friends.')
        self.checkBox_33.setToolTip('Link your Android phone and PC to view and reply to text messages, access mobile apps, and receive notifications.')
