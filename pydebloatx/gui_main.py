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

        self.update_btn = QPushButton(self.sidebar)
        self.update_btn.setGeometry(QRect(0, 204, 51, 51))
        self.update_btn.setProperty('class', 'sidebar_btns')
        self.update_btn.setIcon(QIcon(':/icon/update_icon.png'))
        self.update_btn.setIconSize(QSize(24, 24))
        self.update_btn.hide()

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

        self.layout_widget_checkboxes_2 = QWidget(self.appswidget)
        self.layout_widget_checkboxes_2.setGeometry(QRect(175, 55, 155, 311))
        self.layout_checkboxes_2 = QVBoxLayout(self.layout_widget_checkboxes_2)
        self.layout_checkboxes_2.setContentsMargins(0, 0, 0, 0)

        self.layout_widget_checkboxes_3 = QWidget(self.appswidget)
        self.layout_widget_checkboxes_3.setGeometry(QRect(330, 55, 155, 311))
        self.layout_checkboxes_3 = QVBoxLayout(self.layout_widget_checkboxes_3)
        self.layout_checkboxes_3.setContentsMargins(0, 0, 0, 0)

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
        QToolTip.setFont(self.font)

        self.setWindowTitle(_translate("Title", "PyDebloatX"))
        self.label_info.setText(_translate("Label", ""))

        self.app_name_list = (
            _translate("AppName", "3D Builder"),
            _translate("AppName", "3D Viewer"),
            _translate("AppName", "Alarms and Clock"),
            _translate("AppName", "Calculator"),
            _translate("AppName", "Calendar and Mail"),
            _translate("AppName", "Camera"),
            _translate("AppName", "Feedback Hub"),
            _translate("AppName", "Get Help"),
            _translate("AppName", "Groove Music"),
            _translate("AppName", "Maps"),
            _translate("AppName", "Messaging"),

            _translate("AppName", "Mixed Reality Portal"),
            _translate("AppName", "Mobile Plans"),
            _translate("AppName", "Money"),
            _translate("AppName", "Movies && TV"),
            _translate("AppName", "News"),
            _translate("AppName", "Office"),
            _translate("AppName", "OneNote"),
            _translate("AppName", "Paint 3D"),
            _translate("AppName", "People"),
            _translate("AppName", "Photos"),
            _translate("AppName", "Skype"),

            _translate("AppName", "Snip && Sketch"),
            _translate("AppName", "Solitaire"),
            _translate("AppName", "Sports"),
            _translate("AppName", "Spotify"),
            _translate("AppName", "Sticky Notes"),
            _translate("AppName", "Tips"),
            _translate("AppName", "Voice Recorder"),
            _translate("AppName", "Weather"),
            _translate("AppName", "Xbox"),
            _translate("AppName", "Xbox Game Bar"),
            _translate("AppName", "Your Phone")
        )
        self.tooltip_list = (
            _translate('ToolTip', 'View, create, and personalize 3D objects.'),
            _translate('ToolTip', 'View 3D models and animations in real-time.'),
            _translate('ToolTip', 'A combination of alarm clock, world clock, timer, and stopwatch.'),
            _translate('ToolTip', 'A calculator that includes standard, scientific, and programmer modes, as well as a unit converter.'),
            _translate('ToolTip', 'Stay up to date with email and schedule managing.'),
            _translate('ToolTip', 'Point and shoot to take pictures on Windows 10.'),
            _translate('ToolTip', 'Provide feedback about Windows and apps by sharing suggestions or problems.'),
            _translate('ToolTip', 'Provide a way to ask a question and get recommended solutions or contact assisted support.'),
            _translate('ToolTip', 'Listen to music on Windows, iOS, and Android devices.'),
            _translate('ToolTip', 'Search for places to get directions, business info, and reviews.'),
            _translate('ToolTip', 'Quick, reliable SMS, MMS and RCS messaging from your phone.'),

            _translate('ToolTip', 'Discover Windows Mixed Reality and dive into more than 3,000 games and VR experiences from Steam VR and Microsoft Store.'),
            _translate('ToolTip', 'Sign up for a data plan and connect with mobile operators in your area. You will need a supported SIM card.'),
            _translate('ToolTip', 'Finance calculators, currency exchange rates and commodity prices from around the world.'),
            _translate('ToolTip', 'All your movies and TV shows, all in one place, on all your devices.'),
            _translate('ToolTip', 'Deliver breaking news and trusted, in-depth reporting from the world\'s best journalists.'),
            _translate('ToolTip', 'Find all your Office apps and files in one place.'),
            _translate('ToolTip', 'Digital notebook for capturing and organizing everything across your devices.'),
            _translate('ToolTip', 'Make 2D masterpieces or 3D models that you can play with from all angles.'),
            _translate('ToolTip', 'Connect with all your friends, family, colleagues, and acquaintances in one place.'),
            _translate('ToolTip', 'View and edit your photos and videos, make movies, and create albums.'),
            _translate('ToolTip', 'Instant message, voice or video call application.'),

            _translate('ToolTip', 'Quickly annotate screenshots, photos and other images and save, paste or share with other apps.'),
            _translate('ToolTip', 'Solitaire is one of the most played computer card games of all time.'),
            _translate('ToolTip', 'Live scores and in-depth game experiences for more than 150 leagues.'),
            _translate('ToolTip', 'Play your favorite songs and albums free on Windows 10 with Spotify.'),
            _translate('ToolTip', 'Create notes, type, ink or add a picture, add text formatting, or stick them to the desktop.'),
            _translate('ToolTip', 'Provide users with information and tips about operating system features.'),
            _translate('ToolTip', 'Record sounds, lectures, interviews, and other events.'),
            _translate('ToolTip', 'Latest weather conditions, accurate 10-day and hourly forecasts.'),
            _translate('ToolTip', 'Browse the catalogue, view recommendations, and discover PC games with Xbox Game Pass.'),
            _translate('ToolTip', 'Instant access to widgets for screen capture and sharing, and chatting with Xbox friends.'),
            _translate('ToolTip', 'Link your Android phone and PC to view and reply to text messages, access mobile apps, and receive notifications.')
        )
        self.app_data_list = (
            {"name": "*Microsoft.3DBuilder*", "link": "/?PFN=Microsoft.3DBuilder_8wekyb3d8bbwe", "size": 0},
            {"name": "*Microsoft.Microsoft3DViewer*", "link": "/?PFN=Microsoft.Microsoft3DViewer_8wekyb3d8bbwe", "size": 0},
            {"name": "*Microsoft.WindowsAlarms*", "link": "/?PFN=Microsoft.WindowsAlarms_8wekyb3d8bbwe", "size": 0},
            {"name": "*Microsoft.WindowsCalculator*", "link": "/?PFN=Microsoft.WindowsCalculator_8wekyb3d8bbwe", "size": 0},
            {"name": "*microsoft.windowscommunicationsapps*", "link": "/?PFN=Microsoft.windowscommunicationsapps_8wekyb3d8bbwe", "size": 0},
            {"name": "*Microsoft.WindowsCamera*", "link": "/?PFN=Microsoft.WindowsCamera_8wekyb3d8bbwe", "size": 0},
            {"name": "*Microsoft.WindowsFeedbackHub*", "link": "/?PFN=Microsoft.WindowsFeedbackHub_8wekyb3d8bbwe", "size": 0},
            {"name": "*Microsoft.GetHelp*", "link": "/?PFN=Microsoft.Gethelp_8wekyb3d8bbwe", "size": 0},
            {"name": "*Microsoft.ZuneMusic*", "link": "/?PFN=Microsoft.ZuneMusic_8wekyb3d8bbwe", "size": 0},
            {"name": "*Microsoft.WindowsMaps*", "link": "/?PFN=Microsoft.WindowsMaps_8wekyb3d8bbwe", "size": 0},
            {"name": "*Microsoft.Messaging*", "link": "/?PFN=Microsoft.Messaging_8wekyb3d8bbwe", "size": 0},

            {"name": "*Microsoft.MixedReality.Portal*", "link": "/?PFN=Microsoft.MixedReality.Portal_8wekyb3d8bbwe", "size": 0},
            {"name": "*Microsoft.OneConnect*", "link": "?productId=9NBLGGH5PNB1", "size": 0},
            {"name": "*Microsoft.BingFinance*", "link": "?productId=9WZDNCRFHV4V", "size": 0},
            {"name": "*Microsoft.ZuneVideo*", "link": "/?PFN=Microsoft.ZuneVideo_8wekyb3d8bbwe", "size": 0},
            {"name": "*Microsoft.BingNews*", "link": "/?PFN=Microsoft.BingNews_8wekyb3d8bbwe", "size": 0},
            {"name": "*Microsoft.MicrosoftOfficeHub*", "link": "/?PFN=Microsoft.MicrosoftOfficeHub_8wekyb3d8bbwe", "size": 0},
            {"name": "*Microsoft.Office.OneNote*", "link": "/?PFN=Microsoft.Office.OneNote_8wekyb3d8bbwe", "size": 0},
            {"name": "*Microsoft.MSPaint*", "link": "/?PFN=Microsoft.MSPaint_8wekyb3d8bbwe", "size": 0},
            {"name": "*Microsoft.People*", "link": "/?PFN=Microsoft.People_8wekyb3d8bbwe", "size": 0},
            {"name": "*Microsoft.Windows.Photos*", "link": "/?PFN=Microsoft.Windows.Photos_8wekyb3d8bbwe", "size": 0},
            {"name": "*Microsoft.SkypeApp*", "link": "/?PFN=Microsoft.SkypeApp_kzf8qxf38zg5c", "size": 0},

            {"name": "*Microsoft.ScreenSketch*", "link": "/?PFN=Microsoft.ScreenSketch_8wekyb3d8bbwe", "size": 0},
            {"name": "*Microsoft.MicrosoftSolitaireCollection*", "link": "/?PFN=Microsoft.MicrosoftSolitaireCollection_8wekyb3d8bbwe", "size": 0},
            {"name": "*Microsoft.BingSports*", "link": "?productId=9WZDNCRFHVH4", "size": 0},
            {"name": "*SpotifyAB.SpotifyMusic*", "link": "/?PFN=SpotifyAB.SpotifyMusic_zpdnekdrzrea0", "size": 0},
            {"name": "*Microsoft.MicrosoftStickyNotes*", "link": "/?PFN=Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe", "size": 0},
            {"name": "*Microsoft.Getstarted*", "link": "/?PFN=Microsoft.Getstarted_8wekyb3d8bbwe", "size": 0},
            {"name": "*Microsoft.WindowsSoundRecorder*", "link": "/?PFN=Microsoft.WindowsSoundRecorder_8wekyb3d8bbwe", "size": 0},
            {"name": "*Microsoft.BingWeather*", "link": "/?PFN=Microsoft.BingWeather_8wekyb3d8bbwe", "size": 0},
            {"name": "*Microsoft.GamingApp*", "link": "/?PFN=Microsoft.GamingApp_8wekyb3d8bbwe", "size": 0},
            {"name": "*Xbox*", "link": "/?PFN=Microsoft.XboxGameOverlay_8wekyb3d8bbwe", "size": 0},
            {"name": "*Microsoft.YourPhone*", "link": "/?PFN=Microsoft.YourPhone_8wekyb3d8bbwe", "size": 0}
        )

        self.checkbox_list = []
        for i in range(0, 33):
            self.checkbox_list.append(QCheckBox())
            if i >= 22:
                self.layout_checkboxes_3.addWidget(self.checkbox_list[i])
            elif i >= 11:
                self.layout_checkboxes_2.addWidget(self.checkbox_list[i])
            else:
                self.layout_checkboxes.addWidget(self.checkbox_list[i])

        self.apps_dict = {}
        for i, checkbox in enumerate(self.checkbox_list):
            checkbox.setText(self.app_name_list[i])
            checkbox.setToolTip(self.tooltip_list[i])
            checkbox.setFont(self.font)
            self.apps_dict[checkbox] = self.app_data_list[i]

        self.label_note.setText(_translate("Label", ""))
        self.label_space.setText(_translate("Label", "Total amount of disk space:"))
        self.label_size.setText(_translate("Label", "0 MB"))

        self.button_select_all.setText(_translate("Button", "Select All"))
        self.button_deselect_all.setText(_translate("Button", "Deselect All"))

        self.button_uninstall.setText(_translate("Button", "Uninstall"))
