# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QFrame, QShortcut, QPushButton, QMainWindow, QWidget, QLabel, QVBoxLayout, QCheckBox, \
    QHBoxLayout, QProgressBar, QToolTip
from PyQt5.QtCore import Qt, QRect, QCoreApplication, QMetaObject, QSize
from PyQt5.QtGui import QIcon, QKeySequence, QFont
import sys
import os


def resource_path(relative_path):
    """Determine resource path if app is built or run natively."""
    if hasattr(sys, 'frozen'):
        return os.path.join(sys._MEIPASS, relative_path)  # skipcq: PYL-W0212
    return os.path.join(os.path.abspath('.'), relative_path)


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon(resource_path('icon.ico')))
        self.setFixedSize(540, 470)

    def setupUi(self):
        self.centralwidget = QWidget(self)
        with open(resource_path('style.css'), 'r') as file:
            self.centralwidget.setStyleSheet(file.read())
        self.appswidget = QWidget(self.centralwidget)
        self.appswidget.setGeometry(50, 0, 490, 470)
        self.appswidget.setProperty('class', 'appswidget')
        self.sidebar = QFrame(self.centralwidget)
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

        self.layout_widget_checkboxes = QWidget(self.appswidget)
        self.layout_widget_checkboxes.setGeometry(QRect(20, 55, 155, 311))
        self.layout_checkboxes = QVBoxLayout(self.layout_widget_checkboxes)
        self.layout_checkboxes.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.layout_widget_checkboxes)
        self.checkBox_2 = QCheckBox(self.layout_widget_checkboxes)
        self.checkBox_3 = QCheckBox(self.layout_widget_checkboxes)
        self.checkBox_4 = QCheckBox(self.layout_widget_checkboxes)
        self.checkBox_5 = QCheckBox(self.layout_widget_checkboxes)
        self.checkBox_6 = QCheckBox(self.layout_widget_checkboxes)
        self.checkBox_7 = QCheckBox(self.layout_widget_checkboxes)
        self.checkBox_8 = QCheckBox(self.layout_widget_checkboxes)
        self.checkBox_9 = QCheckBox(self.layout_widget_checkboxes)
        self.checkBox_10 = QCheckBox(self.layout_widget_checkboxes)
        self.checkBox_11 = QCheckBox(self.layout_widget_checkboxes)
        checkbox_column_1 = (self.checkBox, self.checkBox_2, self.checkBox_3, self.checkBox_4, self.checkBox_5, self.checkBox_6,
                             self.checkBox_7, self.checkBox_8, self.checkBox_9, self.checkBox_10, self.checkBox_11
                             )
        for checkbox in checkbox_column_1:
            self.layout_checkboxes.addWidget(checkbox)

        self.layout_widget_checkboxes_2 = QWidget(self.appswidget)
        self.layout_widget_checkboxes_2.setGeometry(QRect(175, 55, 155, 311))
        self.layout_checkboxes_2 = QVBoxLayout(self.layout_widget_checkboxes_2)
        self.layout_checkboxes_2.setContentsMargins(0, 0, 0, 0)
        self.checkBox_12 = QCheckBox(self.layout_widget_checkboxes_2)
        self.checkBox_13 = QCheckBox(self.layout_widget_checkboxes_2)
        self.checkBox_14 = QCheckBox(self.layout_widget_checkboxes_2)
        self.checkBox_15 = QCheckBox(self.layout_widget_checkboxes_2)
        self.checkBox_16 = QCheckBox(self.layout_widget_checkboxes_2)
        self.checkBox_17 = QCheckBox(self.layout_widget_checkboxes_2)
        self.checkBox_18 = QCheckBox(self.layout_widget_checkboxes_2)
        self.checkBox_19 = QCheckBox(self.layout_widget_checkboxes_2)
        self.checkBox_20 = QCheckBox(self.layout_widget_checkboxes_2)
        self.checkBox_21 = QCheckBox(self.layout_widget_checkboxes_2)
        self.checkBox_22 = QCheckBox(self.layout_widget_checkboxes_2)
        checkbox_column_2 = (self.checkBox_12, self.checkBox_13, self.checkBox_14, self.checkBox_15, self.checkBox_16, self.checkBox_17,
                             self.checkBox_18, self.checkBox_19, self.checkBox_20, self.checkBox_21, self.checkBox_22
                             )
        for checkbox in checkbox_column_2:
            self.layout_checkboxes_2.addWidget(checkbox)

        self.layout_widget_checkboxes_3 = QWidget(self.appswidget)
        self.layout_widget_checkboxes_3.setGeometry(QRect(330, 55, 155, 311))
        self.layout_checkboxes_3 = QVBoxLayout(self.layout_widget_checkboxes_3)
        self.layout_checkboxes_3.setContentsMargins(0, 0, 0, 0)
        self.checkBox_23 = QCheckBox(self.layout_widget_checkboxes_3)
        self.checkBox_24 = QCheckBox(self.layout_widget_checkboxes_3)
        self.checkBox_25 = QCheckBox(self.layout_widget_checkboxes_3)
        self.checkBox_26 = QCheckBox(self.layout_widget_checkboxes_3)
        self.checkBox_27 = QCheckBox(self.layout_widget_checkboxes_3)
        self.checkBox_28 = QCheckBox(self.layout_widget_checkboxes_3)
        self.checkBox_29 = QCheckBox(self.layout_widget_checkboxes_3)
        self.checkBox_30 = QCheckBox(self.layout_widget_checkboxes_3)
        self.checkBox_31 = QCheckBox(self.layout_widget_checkboxes_3)
        self.checkBox_32 = QCheckBox(self.layout_widget_checkboxes_3)
        self.checkBox_33 = QCheckBox(self.layout_widget_checkboxes_3)
        checkbox_column_3 = (self.checkBox_23, self.checkBox_24, self.checkBox_25, self.checkBox_26, self.checkBox_27, self.checkBox_28,
                             self.checkBox_29, self.checkBox_30, self.checkBox_31, self.checkBox_32, self.checkBox_33
                             )
        for checkbox in checkbox_column_3:
            self.layout_checkboxes_3.addWidget(checkbox)

        self.label_note = QLabel(self.appswidget)
        self.label_note.setFont(self.font)
        self.label_note.setGeometry(QRect(20, 370, 350, 16))

        self.layout_widget_labels = QWidget(self.appswidget)
        self.layout_widget_labels.setGeometry(QRect(20, 390, 350, 16))
        self.layout_labels = QHBoxLayout(self.layout_widget_labels)
        self.layout_labels.setContentsMargins(0, 0, 0, 0)
        self.label_space = QLabel(self.appswidget)
        self.label_space.setFont(self.font)
        self.layout_labels.addWidget(self.label_space)
        self.label_size = QLabel(self.appswidget)
        self.label_size.setFont(self.font)
        self.layout_labels.addWidget(self.label_size)

        self.layout_widget_buttons = QWidget(self.appswidget)
        self.layout_widget_buttons.setGeometry(QRect(20, 420, 454, 31))
        self.layout_buttons = QHBoxLayout(self.layout_widget_buttons)
        self.layout_buttons.setContentsMargins(0, 0, 0, 0)
        self.button_select_all = QPushButton(self.layout_widget_buttons)
        self.button_select_all.setIcon(QIcon(':/icon/check_icon.png'))
        self.button_select_all.setIconSize(QSize(18, 18))
        self.button_select_all.setLayoutDirection(Qt.RightToLeft)
        self.layout_buttons.addWidget(self.button_select_all)
        self.button_select_all.setMinimumSize(100, 30)
        self.button_select_all.setProperty('class', 'Aqua')
        self.button_deselect_all = QPushButton(self.layout_widget_buttons)
        self.button_deselect_all.setIcon(QIcon(':/icon/cancel_icon.png'))
        self.button_deselect_all.setIconSize(QSize(18, 18))
        self.button_deselect_all.setLayoutDirection(Qt.RightToLeft)
        self.layout_buttons.addWidget(self.button_deselect_all)
        self.button_deselect_all.setMinimumSize(100, 30)
        self.button_deselect_all.setProperty('class', 'Aqua')
        self.layout_buttons.addStretch()
        self.button_uninstall = QPushButton(self.layout_widget_buttons)
        self.button_uninstall.setIcon(QIcon(':/icon/trash_icon.png'))
        self.button_uninstall.setIconSize(QSize(18, 18))
        self.button_uninstall.setLayoutDirection(Qt.RightToLeft)
        self.layout_buttons.addWidget(self.button_uninstall)
        self.button_uninstall.setMinimumSize(100, 30)
        self.button_uninstall.setProperty('class', 'Grapefruit')

        self.setCentralWidget(self.centralwidget)
        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QCoreApplication.translate

        self.setWindowTitle(_translate("Title", "PyDebloatX"))
        self.label_info.setText(_translate("Label", ""))

        self.checkBox.setText(_translate("AppName", "3D Builder"))
        self.checkBox_2.setText(_translate("AppName", "3D Viewer"))
        self.checkBox_3.setText(_translate("AppName", "Alarms and Clock"))
        self.checkBox_4.setText(_translate("AppName", "Calculator"))
        self.checkBox_5.setText(_translate("AppName", "Calendar and Mail"))
        self.checkBox_6.setText(_translate("AppName", "Camera"))
        self.checkBox_7.setText(_translate("AppName", "Get Help"))
        self.checkBox_8.setText(_translate("AppName", "Groove Music"))
        self.checkBox_9.setText(_translate("AppName", "Maps"))
        self.checkBox_10.setText(_translate("AppName", "Messaging"))
        self.checkBox_11.setText(_translate("AppName", "Mixed Reality Portal"))

        self.checkBox_12.setText(_translate("AppName", "Mobile Plans"))
        self.checkBox_13.setText(_translate("AppName", "Money"))
        self.checkBox_14.setText(_translate("AppName", "Movies && TV"))
        self.checkBox_15.setText(_translate("AppName", "News"))
        self.checkBox_16.setText(_translate("AppName", "Office"))
        self.checkBox_17.setText(_translate("AppName", "OneNote"))
        self.checkBox_18.setText(_translate("AppName", "Paint 3D"))
        self.checkBox_19.setText(_translate("AppName", "People"))
        self.checkBox_20.setText(_translate("AppName", "Photos"))
        self.checkBox_21.setText(_translate("AppName", "Skype"))
        self.checkBox_22.setText(_translate("AppName", "Snip && Sketch"))

        self.checkBox_23.setText(_translate("AppName", "Solitaire"))
        self.checkBox_24.setText(_translate("AppName", "Sports"))
        self.checkBox_25.setText(_translate("AppName", "Spotify"))
        self.checkBox_26.setText(_translate("AppName", "Sticky Notes"))
        self.checkBox_27.setText(_translate("AppName", "Tips"))
        self.checkBox_28.setText(_translate("AppName", "Voice Recorder"))
        self.checkBox_29.setText(_translate("AppName", "Weather"))
        self.checkBox_30.setText(_translate("AppName", "Windows Feedback"))
        self.checkBox_31.setText(_translate("AppName", "Xbox"))
        self.checkBox_32.setText(_translate("AppName", "Xbox Game Bar"))
        self.checkBox_33.setText(_translate("AppName", "Your Phone"))

        self.label_note.setText(_translate("Label", ""))
        self.label_space.setText(_translate("Label", "Total amount of disk space:"))
        self.label_size.setText(_translate("Label", "0 MB"))

        self.button_select_all.setText(_translate("Button", "Select All"))
        self.button_deselect_all.setText(_translate("Button", "Deselect All"))

        self.button_uninstall.setText(_translate("Button", "Uninstall"))

        QToolTip.setFont(self.font)
        self.checkBox.setToolTip(_translate('ToolTip', 'View, create, and personalize 3D objects.'))
        self.checkBox_2.setToolTip(_translate('ToolTip', 'View 3D models and animations in real-time.'))
        self.checkBox_3.setToolTip(_translate('ToolTip', 'A combination of alarm clock, world clock, timer, and stopwatch.'))
        self.checkBox_4.setToolTip(_translate('ToolTip', 'A calculator that includes standard, scientific, and programmer modes, as well as a unit converter.'))
        self.checkBox_5.setToolTip(_translate('ToolTip', 'Stay up to date with email and schedule managing.'))
        self.checkBox_6.setToolTip(_translate('ToolTip', 'Point and shoot to take pictures on Windows 10.'))
        self.checkBox_7.setToolTip(_translate('ToolTip', 'Provide a way to ask a question and get recommended solutions or contact assisted support.'))
        self.checkBox_8.setToolTip(_translate('ToolTip', 'Listen to music on Windows, iOS, and Android devices.'))
        self.checkBox_9.setToolTip(_translate('ToolTip', 'Search for places to get directions, business info, and reviews.'))
        self.checkBox_10.setToolTip(_translate('ToolTip', 'Quick, reliable SMS, MMS and RCS messaging from your phone.'))
        self.checkBox_11.setToolTip(_translate('ToolTip', 'Discover Windows Mixed Reality and dive into more than 3,000 games and VR experiences from Steam VR and Microsoft Store.'))

        self.checkBox_12.setToolTip(_translate('ToolTip', 'Sign up for a data plan and connect with mobile operators in your area. You will need a supported SIM card.'))
        self.checkBox_13.setToolTip(_translate('ToolTip', 'Finance calculators, currency exchange rates and commodity prices from around the world.'))
        self.checkBox_14.setToolTip(_translate('ToolTip', 'All your movies and TV shows, all in one place, on all your devices.'))
        self.checkBox_15.setToolTip(_translate('ToolTip', 'Deliver breaking news and trusted, in-depth reporting from the world\'s best journalists.'))
        self.checkBox_16.setToolTip(_translate('ToolTip', 'Find all your Office apps and files in one place.'))
        self.checkBox_17.setToolTip(_translate('ToolTip', 'Digital notebook for capturing and organizing everything across your devices.'))
        self.checkBox_18.setToolTip(_translate('ToolTip', 'Make 2D masterpieces or 3D models that you can play with from all angles.'))
        self.checkBox_19.setToolTip(_translate('ToolTip', 'Connect with all your friends, family, colleagues, and acquaintances in one place.'))
        self.checkBox_20.setToolTip(_translate('ToolTip', 'View and edit your photos and videos, make movies, and create albums.'))
        self.checkBox_21.setToolTip(_translate('ToolTip', 'Instant message, voice or video call application.'))
        self.checkBox_22.setToolTip(_translate('ToolTip', 'Quickly annotate screenshots, photos and other images and save, paste or share with other apps.'))

        self.checkBox_23.setToolTip(_translate('ToolTip', 'Solitaire is one of the most played computer card games of all time.'))
        self.checkBox_24.setToolTip(_translate('ToolTip', 'Live scores and in-depth game experiences for more than 150 leagues.'))
        self.checkBox_25.setToolTip(_translate('ToolTip', 'Play your favorite songs and albums free on Windows 10 with Spotify.'))
        self.checkBox_26.setToolTip(_translate('ToolTip', 'Create notes, type, ink or add a picture, add text formatting, or stick them to the desktop.'))
        self.checkBox_27.setToolTip(_translate('ToolTip', 'Provide users with information and tips about operating system features.'))
        self.checkBox_28.setToolTip(_translate('ToolTip', 'Record sounds, lectures, interviews, and other events.'))
        self.checkBox_29.setToolTip(_translate('ToolTip', 'Latest weather conditions, accurate 10-day and hourly forecasts.'))
        self.checkBox_30.setToolTip(_translate('ToolTip', 'Provide feedback about Windows and apps by sharing suggestions or problems.'))
        self.checkBox_31.setToolTip(_translate('ToolTip', 'Browse the catalogue, view recommendations, and discover PC games with Xbox Game Pass.'))
        self.checkBox_32.setToolTip(_translate('ToolTip', 'Instant access to widgets for screen capture and sharing, and chatting with Xbox friends.'))
        self.checkBox_33.setToolTip(_translate('ToolTip', 'Link your Android phone and PC to view and reply to text messages, access mobile apps, and receive notifications.'))
