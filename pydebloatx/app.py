from PyQt5.QtCore import Qt, QThread, pyqtSignal, QPoint, QRect, QLocale, QTranslator
from PyQt5.QtGui import QCursor, QPixmap, QIcon, QFont
from PyQt5.QtWidgets import QApplication, QMessageBox
from gui_about import Ui_AboutWindow
from gui_main import Ui_MainWindow
from os.path import getsize, join
import webbrowser
import subprocess
import img_res  # skipcq: PYL-W0611
import json
import sys
import os


__version__ = "1.9.0"


def resource_path(relative_path):
    """Determine resource path if app is built or run natively."""
    if hasattr(sys, 'frozen'):
        return os.path.join(sys._MEIPASS, relative_path)  # skipcq: PYL-W0212
    return os.path.join(os.path.abspath('.'), relative_path)


def get_dir_size(dir_path):
    """Get directory size of installed apps."""
    dir_size = 0
    for root, _, files in os.walk(dir_path):
        dir_size += sum([getsize(join(root, name)) for name in files])
    return dir_size


class Logic():
    def __init__(self):
        about.label_version.setText(f"Version {__version__}")
        self.total_size = 0
        self.is_link_menu = False
        self.main_title = 'Select the default Windows 10 apps to uninstall:\n(Hover over app names to view description)'
        self.store_title = 'Click on an app name to view it in Microsoft Store.'
        self.refresh_title = 'Refreshing list of installed apps...'
        self.size_text = 'MB'
        self.github_dialog = 'Visit the PyDebloatX GitHub page?'
        self.quit_dialog = 'Quit PyDebloatX?'
        self.dialog_yes = 'Yes'
        self.dialog_no = 'No'
        self.dialog_ok = 'OK'
        self.uninstall_text = 'Uninstall'
        self.uninstalling_text = 'Uninstalling'
        self.left_text = 'left'
        self.success_text = 'All selected apps were successfully uninstalled.'
        self.app_singular = 'app'
        self.app_genitive_singular = 'apps'
        self.app_genitive_plural = 'apps'
        self.size_available_text = 'MB of space will be freed.'
        self.main_widgets = (ui.refresh_btn, ui.refresh_bind, ui.store_btn, ui.store_bind, ui.button_select_all, ui.button_deselect_all, ui.button_uninstall)

        self.apps_dict = {
            ui.checkBox: {"name": "*Microsoft.3DBuilder*", "link": "/?PFN=Microsoft.3DBuilder_8wekyb3d8bbwe", "size": 0},
            ui.checkBox_2: {"name": "*Microsoft.Microsoft3DViewer*", "link": "/?PFN=Microsoft.Microsoft3DViewer_8wekyb3d8bbwe", "size": 0},
            ui.checkBox_3: {"name": "*Microsoft.WindowsAlarms*", "link": "/?PFN=Microsoft.WindowsAlarms_8wekyb3d8bbwe", "size": 0},
            ui.checkBox_4: {"name": "*Microsoft.WindowsCalculator*", "link": "/?PFN=Microsoft.WindowsCalculator_8wekyb3d8bbwe", "size": 0},
            ui.checkBox_5: {"name": "*microsoft.windowscommunicationsapps*", "link": "/?PFN=Microsoft.windowscommunicationsapps_8wekyb3d8bbwe", "size": 0},
            ui.checkBox_6: {"name": "*Microsoft.WindowsCamera*", "link": "/?PFN=Microsoft.WindowsCamera_8wekyb3d8bbwe", "size": 0},
            ui.checkBox_7: {"name": "*Microsoft.GetHelp*", "link": "/?PFN=Microsoft.Gethelp_8wekyb3d8bbwe", "size": 0},
            ui.checkBox_8: {"name": "*Microsoft.ZuneMusic*", "link": "/?PFN=Microsoft.ZuneMusic_8wekyb3d8bbwe", "size": 0},
            ui.checkBox_9: {"name": "*Microsoft.WindowsMaps*", "link": "/?PFN=Microsoft.WindowsMaps_8wekyb3d8bbwe", "size": 0},
            ui.checkBox_10: {"name": "*Microsoft.Messaging*", "link": "/?PFN=Microsoft.Messaging_8wekyb3d8bbwe", "size": 0},
            ui.checkBox_11: {"name": "*Microsoft.MixedReality.Portal*", "link": "/?PFN=Microsoft.MixedReality.Portal_8wekyb3d8bbwe", "size": 0},

            ui.checkBox_12: {"name": "*Microsoft.OneConnect*", "link": "?productId=9NBLGGH5PNB1", "size": 0},
            ui.checkBox_13: {"name": "*Microsoft.BingFinance*", "link": "?productId=9WZDNCRFHV4V", "size": 0},
            ui.checkBox_14: {"name": "*Microsoft.ZuneVideo*", "link": "/?PFN=Microsoft.ZuneVideo_8wekyb3d8bbwe", "size": 0},
            ui.checkBox_15: {"name": "*Microsoft.BingNews*", "link": "/?PFN=Microsoft.BingNews_8wekyb3d8bbwe", "size": 0},
            ui.checkBox_16: {"name": "*Microsoft.MicrosoftOfficeHub*", "link": "/?PFN=Microsoft.MicrosoftOfficeHub_8wekyb3d8bbwe", "size": 0},
            ui.checkBox_17: {"name": "*Microsoft.Office.OneNote*", "link": "/?PFN=Microsoft.Office.OneNote_8wekyb3d8bbwe", "size": 0},
            ui.checkBox_18: {"name": "*Microsoft.MSPaint*", "link": "/?PFN=Microsoft.MSPaint_8wekyb3d8bbwe", "size": 0},
            ui.checkBox_19: {"name": "*Microsoft.People*", "link": "/?PFN=Microsoft.People_8wekyb3d8bbwe", "size": 0},
            ui.checkBox_20: {"name": "*Microsoft.Windows.Photos*", "link": "/?PFN=Microsoft.Windows.Photos_8wekyb3d8bbwe", "size": 0},
            ui.checkBox_21: {"name": "*Microsoft.SkypeApp*", "link": "/?PFN=Microsoft.SkypeApp_kzf8qxf38zg5c", "size": 0},
            ui.checkBox_22: {"name": "*Microsoft.ScreenSketch*", "link": "/?PFN=Microsoft.ScreenSketch_8wekyb3d8bbwe", "size": 0},

            ui.checkBox_23: {"name": "*Microsoft.MicrosoftSolitaireCollection*", "link": "/?PFN=Microsoft.MicrosoftSolitaireCollection_8wekyb3d8bbwe", "size": 0},
            ui.checkBox_24: {"name": "*Microsoft.BingSports*", "link": "?productId=9WZDNCRFHVH4", "size": 0},
            ui.checkBox_25: {"name": "*SpotifyAB.SpotifyMusic*", "link": "/?PFN=SpotifyAB.SpotifyMusic_zpdnekdrzrea0", "size": 0},
            ui.checkBox_26: {"name": "*Microsoft.MicrosoftStickyNotes*", "link": "/?PFN=Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe", "size": 0},
            ui.checkBox_27: {"name": "*Microsoft.Getstarted*", "link": "/?PFN=Microsoft.Getstarted_8wekyb3d8bbwe", "size": 0},
            ui.checkBox_28: {"name": "*Microsoft.WindowsSoundRecorder*", "link": "/?PFN=Microsoft.WindowsSoundRecorder_8wekyb3d8bbwe", "size": 0},
            ui.checkBox_29: {"name": "*Microsoft.BingWeather*", "link": "/?PFN=Microsoft.BingWeather_8wekyb3d8bbwe", "size": 0},
            ui.checkBox_30: {"name": "*Microsoft.WindowsFeedbackHub*", "link": "/?PFN=Microsoft.WindowsFeedbackHub_8wekyb3d8bbwe", "size": 0},
            ui.checkBox_31: {"name": "*Microsoft.GamingApp*", "link": "/?PFN=Microsoft.GamingApp_8wekyb3d8bbwe", "size": 0},
            ui.checkBox_32: {"name": "*Xbox*", "link": "/?PFN=Microsoft.XboxGameOverlay_8wekyb3d8bbwe", "size": 0},
            ui.checkBox_33: {"name": "*Microsoft.YourPhone*", "link": "/?PFN=Microsoft.YourPhone_8wekyb3d8bbwe", "size": 0}
        }

        ui.progressbar.setValue(0)
        ui.progressbar.setMaximum(len(self.apps_dict))
        ui.progressbar.setFont(ui.font)
        ui.button_uninstall.clicked.connect(self.uninstall)
        ui.button_select_all.clicked.connect(self.select_all)
        ui.button_deselect_all.clicked.connect(self.deselect_all)
        ui.refresh_btn.clicked.connect(self.app_refresh)
        ui.refresh_bind.activated.connect(self.app_refresh)
        ui.store_btn.clicked.connect(self.store_menu)
        ui.store_bind.activated.connect(self.store_menu)
        ui.homepage_btn.clicked.connect(self.app_homepage)
        ui.homepage_bind.activated.connect(self.app_homepage)
        ui.about_btn.clicked.connect(self.app_about)
        ui.about_bind.activated.connect(self.app_about)
        ui.quit_btn.clicked.connect(self.app_quit)
        ui.quit_bind.activated.connect(self.app_quit)
        about.button_quit_about.clicked.connect(about.close)
        for i in self.apps_dict:
            i.setFont(ui.font)
            i.clicked.connect(self.enable_buttons)
            with open(resource_path('style.css'), 'r') as file:
                i.setStyleSheet(file.read())

        self.app_refresh()

    def store_menu(self):
        """Toggle between Main view and Store view."""
        widgets = (ui.horizontalLayoutWidget, ui.horizontalLayoutWidget_2, ui.label_note, ui.label_space, ui.label_size)
        if self.is_link_menu:
            self.is_link_menu = False
            ui.label_info.setText(self.main_title)
            ui.store_btn.setIcon(QIcon(':/icon/store_icon.png'))
            for i in self.apps_dict:
                i.setEnabled(False)
                i.setChecked(False)
            for i in self.installed_apps:
                i.setEnabled(True)
            for i in self.selected_apps:
                i.setChecked(True)
            self.enable_buttons()
            for widget in widgets:
                widget.show()
        else:
            self.is_link_menu = True
            ui.label_info.setText(self.store_title)
            ui.store_btn.setIcon(QIcon(':/icon/back_icon.png'))
            for i in self.apps_dict:
                i.setEnabled(True)
                i.setChecked(True)
            for widget in widgets:
                widget.hide()

    def app_refresh(self):
        """Create threads to refresh list of installed apps."""
        if self.is_link_menu:
            self.store_menu()
        self.installed_apps = []
        self.progress = 0
        for i in self.apps_dict:
            i.setEnabled(False)
            i.setChecked(False)
        ui.label_refresh.show()
        ui.label_info.hide()
        ui.progressbar.show()
        for widget in self.main_widgets:
            widget.setEnabled(False)
        ui.refresh_btn.setIcon(QIcon(':/icon/no_refresh_icon.png'))
        ui.button_select_all.setIcon(QIcon(':/icon/no_check_icon.png'))
        ui.button_uninstall.setIcon(QIcon(':/icon/no_trash_icon.png'))
        ui.button_deselect_all.setIcon(QIcon(':/icon/no_cancel_icon.png'))
        QApplication.setOverrideCursor(QCursor(Qt.BusyCursor))
        ui.label_refresh.setText(self.refresh_title)

        self.check_thread = CheckApps(self.apps_dict)
        self.check_thread.app_signal.connect(self.enable_installed)
        self.check_thread.progress_signal.connect(self.update_progress)
        self.check_thread.start()

    def thread_finished(self):
        """Set up Main view after finishing a task."""
        ui.progressbar.hide()
        ui.label_refresh.hide()
        ui.label_info.show()
        ui.progressbar.setValue(0)
        QApplication.setOverrideCursor(QCursor())
        ui.label_info.setText(self.main_title)
        for widget in (ui.refresh_btn, ui.refresh_bind, ui.store_btn, ui.store_bind):
            widget.setEnabled(True)
        ui.refresh_btn.setIcon(QIcon(':/icon/refresh_icon.png'))
        self.enable_buttons()

    def enable_installed(self, i):
        """Enable checkboxes while refreshing list of installed apps."""
        i.setEnabled(True)
        self.installed_apps.append(i)
        self.enable_buttons()

    def update_progress(self):
        """Update progress bar while refreshing list of installed apps."""
        self.progress += 1
        ui.progressbar.setValue(self.progress)
        if self.progress >= len(self.apps_dict):
            self.thread_finished()

    def uninstall_progress(self, i):
        """Update progress bar and label while uninstalling selected apps."""
        self.progress += 1
        ui.progressbar.setValue(self.progress)
        self.installed_apps.remove(i)
        app_name = i.text().replace(' && ', ' & ')
        apps_left = len(self.selected_apps) - self.progress + 1
        ui.label_refresh.setText(f"{self.uninstalling_text} {app_name}, {apps_left} {self.app_genitive_plural if apps_left > 1 else self.app_singular} {self.left_text}...")
        ui.label_refresh.show()
        if self.progress >= len(self.selected_apps):
            self.thread_finished()
            self.message_box(self.success_text)

    def enable_buttons(self):
        """Enable buttons or open Microsoft Store when clicking checkboxes."""
        if not self.is_link_menu:
            self.total_size = 0
            self.selected_apps = []
            for i in self.installed_apps:
                if i.isChecked():
                    self.selected_apps.append(i)
                    self.total_size += self.apps_dict[i]["size"]
                    ui.label_size.setText(f'{self.total_size:.2f} {self.size_text}')
            if any(i.isChecked() for i in self.installed_apps):
                ui.button_uninstall.setDisabled(False)
                ui.button_deselect_all.setDisabled(False)
                ui.button_uninstall.setIcon(QIcon(':/icon/trash_icon.png'))
                ui.button_deselect_all.setIcon(QIcon(':/icon/cancel_icon.png'))
            else:
                ui.button_uninstall.setDisabled(True)
                ui.button_deselect_all.setDisabled(True)
                ui.button_uninstall.setIcon(QIcon(':/icon/no_trash_icon.png'))
                ui.button_deselect_all.setIcon(QIcon(':/icon/no_cancel_icon.png'))
                ui.label_size.setText(f'{self.total_size} {self.size_text}')

            if all(i.isChecked() for i in self.installed_apps):
                ui.button_select_all.setDisabled(True)
                ui.button_select_all.setIcon(QIcon(':/icon/no_check_icon.png'))
            else:
                ui.button_select_all.setDisabled(False)
                ui.button_select_all.setIcon(QIcon(':/icon/check_icon.png'))
        else:
            for i in self.apps_dict:
                if not i.isChecked():
                    i.setChecked(True)
                    webbrowser.open_new(f'ms-windows-store://pdp{self.apps_dict[i]["link"]}')

    def message_box(self, message: str, buttons: int = 1) -> int:
        """
        Message box with "Yes/No" or "OK" buttons. Defaults to "OK".\n
            Parameters:\n
                message (str): Message shown inside the message box.
                buttons (int): Amount of buttons, 1 - "OK" button, 2 - "Yes/No" buttons.
            Returns:\n
                choice (int): ID of the clicked button.
        """
        pixmap = QPixmap(resource_path('icon.ico')).scaledToWidth(35, Qt.SmoothTransformation)
        msg_box = QMessageBox()
        msg_box.setFont(ui.font)
        msg_box.setText(message)
        if buttons == 2:
            msg_yes = msg_box.addButton(QMessageBox.Yes)
            msg_no = msg_box.addButton(QMessageBox.No)
            msg_yes.setText(self.dialog_yes)
            msg_no.setText(self.dialog_no)
            msg_yes.setProperty('class', 'button_yes')
            msg_no.setProperty('class', 'button_no')
        msg_box.setWindowFlags(Qt.Dialog | Qt.CustomizeWindowHint)
        msg_box.setWindowIcon(QIcon(resource_path('icon.ico')))
        msg_box.setWindowTitle("PyDebloatX")
        msg_box.setIconPixmap(pixmap)
        with open(resource_path('style.css'), 'r') as file:
            msg_box.setStyleSheet(file.read())
        msg_box.move(ui.frameGeometry().center() - QRect(QPoint(), msg_box.sizeHint()).center())
        choice = msg_box.exec_()
        return choice

    def app_homepage(self):
        if self.message_box(self.github_dialog, 2) == QMessageBox.Yes:
            webbrowser.open_new('https://github.com/Teraskull/PyDebloatX')

    @staticmethod
    def app_about():
        """Show 'About' window."""
        about.setWindowModality(Qt.ApplicationModal)
        about.move(ui.geometry().center() - about.rect().center())
        about.show()

    def app_quit(self):
        """Quit app after confirmation."""
        if self.message_box(self.quit_dialog, 2) == QMessageBox.Yes:
            app.quit()

    def select_all(self):
        """Select all checkboxes for installed apps."""
        for i in self.installed_apps:
            if not i.isChecked():
                i.setChecked(True)
        self.enable_buttons()

    def deselect_all(self):
        """Deselect all checkboxes for installed apps."""
        for i in self.installed_apps:
            if i.isChecked():
                i.setChecked(False)
        self.enable_buttons()

    def uninstall(self):
        """Create threads to uninstall selected apps after confirmation."""
        apps = len(self.selected_apps)
        msg_uninstall = f"{self.uninstall_text} {apps} {self.app_genitive_plural if apps > 1 else self.app_singular}?\n\n{self.total_size:.2f} {self.size_available_text}"

        if self.message_box(msg_uninstall, 2) == QMessageBox.Yes:
            for widget in self.main_widgets:
                widget.setEnabled(False)
            ui.label_info.hide()
            self.progress = 0
            ui.progressbar.setMaximum(apps)
            ui.progressbar.show()

            self.newWorkerThread = QThread()
            self.new_thread_list = []
            for item, i in enumerate(self.selected_apps):
                i.setEnabled(False)
                i.setChecked(False)
                self.new_thread_list.append(UninstallApps(self.apps_dict, i))
                self.new_thread_list[item].moveToThread(self.newWorkerThread)
                self.new_thread_list[item].progress_signal.connect(self.uninstall_progress)
            for new_thread in self.new_thread_list:
                new_thread.start()


class CheckApps(QThread):
    """Refresh list of installed apps."""
    progress_signal = pyqtSignal()
    app_signal = pyqtSignal(object)

    def __init__(self, apps_dict):
        super().__init__()
        self.apps_dict = apps_dict

    def run(self):
        si = subprocess.STARTUPINFO()
        si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        x = subprocess.Popen(["powershell", "Get-AppxPackage | Select Name, InstallLocation | ConvertTo-JSON"],
                             stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=False, startupinfo=si, text=True)
        names_str = x.communicate()[0]
        names_list = json.loads(names_str)

        for i in self.apps_dict:
            temp_name = self.apps_dict[i]["name"].strip("*")
            self.apps_dict[i]["size"] = 0
            flag = False
            if temp_name != "Xbox":
                for item in names_list:
                    name = item["Name"]
                    if name.find(temp_name, 0, len(name)) != -1:
                        flag = True
                        self.apps_dict[i]["size"] += get_dir_size(item["InstallLocation"]) / 1024 / 1024
                        break
            else:
                for item in names_list:
                    name = item["Name"]
                    if name.find(temp_name, 0, len(name)) != -1:
                        if name.find("XboxGameCallableUI", 0, len(name)) == -1:
                            flag = True
                            self.apps_dict[i]["size"] += get_dir_size(item["InstallLocation"]) / 1024 / 1024

            if flag:
                self.app_signal.emit(i)

            self.progress_signal.emit()


class UninstallApps(QThread):
    """Uninstall selected apps."""
    progress_signal = pyqtSignal(object)

    def __init__(self, apps_dict, i):
        super().__init__()
        self.apps_dict = apps_dict
        self.i = i

    def run(self):
        package_name = self.apps_dict[self.i]["name"]
        if "Xbox" in package_name:
            package_name = "*Xbox* | Where-Object {$_.name -notmatch 'XboxGameCallableUI'}"
        si = subprocess.STARTUPINFO()
        si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        x = subprocess.Popen(
            ["powershell", f'try {{Get-AppxPackage {package_name} -OutVariable app | Remove-AppPackage -ea stop;[bool]$app}} catch {{$false}}'],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=False, startupinfo=si
        )
        x.communicate()[0]
        self.progress_signal.emit(self.i)


if __name__ == '__main__':
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    app = QApplication(sys.argv)
    app.setFont(QFont("Tahoma"))
    locale = QLocale()
    trans = QTranslator()
    if trans.load(locale, "", "", "Language", ".qm"):
        app.installTranslator(trans)
    about = Ui_AboutWindow()
    about.setupUi()
    ui = Ui_MainWindow()
    ui.setupUi()
    ui.show()
    logic = Logic()
    sys.exit(app.exec_())
