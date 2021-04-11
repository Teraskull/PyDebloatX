from PySide6.QtCore import Qt, QThread, Signal, QPoint, QRect, QLocale, QTranslator, QCoreApplication, QThreadPool, \
    QObject, QRunnable
from PySide6.QtGui import QCursor, QPixmap, QIcon, QFont
from PySide6.QtWidgets import QApplication, QMessageBox
from gui_about import Ui_AboutWindow
from gui_main import Ui_MainWindow
from os.path import getsize, join
from packaging import version
import webbrowser
import subprocess
import requests
import img_res  # skipcq: PYL-W0611
import json
import sys
import os


__version__ = "1.12.0"


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
        about.label_version.setText(QCoreApplication.translate("Label", "Version") + f" {__version__}")
        self.total_size = 0
        self.is_link_menu = False
        self.main_title = QCoreApplication.translate("Label", "Select the default Windows 10 apps to uninstall:\n(Hover over app names to view description)")
        self.store_title = QCoreApplication.translate("Label", "Click on an app name to view it in Microsoft Store.")
        self.refresh_title = QCoreApplication.translate("Label", "Refreshing list of installed apps...")
        self.size_text = QCoreApplication.translate("Label", "MB")
        self.github_dialog = QCoreApplication.translate("MessageBox", "Visit the PyDebloatX GitHub page?")
        self.quit_dialog = QCoreApplication.translate("MessageBox", "Quit PyDebloatX?")
        self.dialog_yes = QCoreApplication.translate("Button", "Yes")
        self.dialog_no = QCoreApplication.translate("Button", "No")
        self.dialog_ok = QCoreApplication.translate("Button", "OK")
        self.success_text = QCoreApplication.translate("MessageBox", "All selected apps were successfully uninstalled.")
        self.main_widgets = (ui.refresh_btn, ui.refresh_bind, ui.store_btn, ui.store_bind, ui.button_select_all, ui.button_deselect_all, ui.button_uninstall)
        self.apps_dict = ui.apps_dict

        ui.progressbar.setValue(0)
        ui.progressbar.setMaximum(len(self.apps_dict))
        ui.progressbar.setFont(ui.font)
        ui.layout_widget_labels.adjustSize()
        for layout in (ui.layout_checkboxes, ui.layout_checkboxes_2, ui.layout_checkboxes_3):
            layout.addStretch()
            layout.setSpacing(14)
        for layout_widget in (ui.layout_widget_checkboxes, ui.layout_widget_checkboxes_2, ui.layout_widget_checkboxes_3):
            layout_widget.adjustSize()
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
        for checkbox in ui.checkbox_list:
            checkbox.clicked.connect(self.enable_buttons)

        self.app_refresh()
        self.check_updates()

    def store_menu(self):
        """Toggle between Main view and Store view."""
        widgets = (ui.layout_widget_buttons, ui.label_space, ui.label_size)
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

    def check_updates(self):
        """Check for updates."""
        self.check_updates_thread = CheckUpdates()
        self.check_updates_thread.version_signal.connect(self.show_updates)
        self.check_updates_thread.start()

    def show_updates(self, latest_version):
        """Show updates."""
        if version.parse(latest_version) > version.parse(__version__):
            msg_update = QCoreApplication.translate("MessageBox", "PyDebloatX {0} is available.\n\nVisit download page?").format(latest_version)
            if self.message_box(msg_update, 2) == QMessageBox.Yes:
                webbrowser.open_new('https://github.com/Teraskull/PyDebloatX/releases')

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
        ui.label_refresh.setText(QCoreApplication.translate("Label", "Uninstalling {0}, %n app(s) left...", "", apps_left).format(app_name))
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
                    ui.layout_widget_labels.adjustSize()
            if any(i.isChecked() for i in self.installed_apps):
                ui.button_uninstall.setDisabled(False)
                ui.button_deselect_all.setDisabled(False)
            else:
                ui.button_uninstall.setDisabled(True)
                ui.button_deselect_all.setDisabled(True)
                ui.label_size.setText(f'{self.total_size} {self.size_text}')

            if all(i.isChecked() for i in self.installed_apps):
                ui.button_select_all.setDisabled(True)
            else:
                ui.button_select_all.setDisabled(False)
        else:
            for i in self.apps_dict:
                if not i.isChecked():
                    i.setChecked(True)
                    webbrowser.open_new(f'ms-windows-store://pdp{self.apps_dict[i]["link"]}')

    def message_box(self, message: str, buttons: int = 1) -> int:
        '''
        Message box with "Yes/No" or "OK" buttons. Defaults to "OK".\n
            Parameters:\n
                message (str): Message shown inside the message box.
                buttons (int): Amount of buttons, 1 - "OK" button, 2 - "Yes/No" buttons.
            Returns:\n
                choice (int): ID of the clicked button.
        '''
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
        msg_box.setIconPixmap(pixmap)
        with open(resource_path('style.css'), 'r') as file:
            msg_box.setStyleSheet(file.read())
        msg_box.move(ui.frameGeometry().center() - QRect(QPoint(), msg_box.sizeHint()).center())
        choice = msg_box.exec_()
        return choice

    def app_homepage(self):
        """Open GitHub app homepage after confirmation."""
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
        confirm_uninstall = QCoreApplication.translate("MessageBox", "Uninstall %n app(s)?", "", apps)
        space_freed_text = QCoreApplication.translate("MessageBox", "MB of space will be freed.")
        msg_uninstall = f"{confirm_uninstall}\n\n{self.total_size:.2f} {space_freed_text}"

        if self.message_box(msg_uninstall, 2) == QMessageBox.Yes:
            for widget in self.main_widgets:
                widget.setEnabled(False)
            ui.label_info.hide()
            self.progress = 0
            ui.progressbar.setMaximum(apps)
            ui.progressbar.show()

            self.new_thread_list = []
            for item, i in enumerate(self.selected_apps):
                i.setEnabled(False)
                i.setChecked(False)
                self.new_thread_list.append(UninstallApps(self.apps_dict, i))
                self.new_thread_list[item].signals.progress_signal.connect(self.uninstall_progress)
            self.newPoolThread = RunThreadPool(self.new_thread_list)
            self.newPoolThread.start()


class CheckUpdates(QThread):
    """Check for updates and get the latest version number."""
    version_signal = Signal(str)

    def run(self):
        try:
            api_url = 'https://api.github.com/repos/Teraskull/PyDebloatX/releases/latest'
            api_data = requests.get(api_url, timeout=(5, 0.7)).json()
            # API rate limit exceeded (https://docs.github.com/rest/overview/resources-in-the-rest-api#rate-limiting)
            if 'tag_name' in api_data:
                latest_version = api_data['tag_name']
                self.version_signal.emit(latest_version)
        except requests.exceptions.RequestException:
            pass


class CheckApps(QThread):
    """Refresh list of installed apps."""
    progress_signal = Signal()
    app_signal = Signal(object)

    def __init__(self, apps_dict):
        super().__init__()
        self.apps_dict = apps_dict

    def run(self):
        si = subprocess.STARTUPINFO()
        si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        x = subprocess.Popen(["powershell", "Get-AppxPackage -PackageTypeFilter Main | Select Name, InstallLocation | ConvertTo-JSON"],
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
                    if name.find(temp_name, 0, len(name)) != -1 and name.find("XboxGameCallableUI", 0, len(name)) == -1:
                        flag = True
                        self.apps_dict[i]["size"] += get_dir_size(item["InstallLocation"]) / 1024 / 1024

            if flag:
                self.app_signal.emit(i)

            self.progress_signal.emit()


class RunThreadPool(QThread):
    """Run thread pool for uninstalling selected apps."""
    def __init__(self, new_thread_list):
        super().__init__()
        self.new_thread_list = new_thread_list

    def run(self):
        pool = QThreadPool()
        for new_thread in self.new_thread_list:
            pool.start(new_thread)
        pool.waitForDone()


class UninstallSignals(QObject):
    """PyQt signal emitting class for uninstalling apps."""
    progress_signal = Signal(object)


class UninstallApps(QRunnable):
    """Uninstall selected apps."""
    def __init__(self, apps_dict, i):
        super().__init__()
        self.signals = UninstallSignals()
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
        self.signals.progress_signal.emit(self.i)


if __name__ == '__main__':
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    app = QApplication(sys.argv)
    app.setFont(QFont("Tahoma"))
    locale = QLocale()
    trans = QTranslator()
    if trans.load(locale, "", "", resource_path("Language"), ".qm"):
        app.installTranslator(trans)
    about = Ui_AboutWindow()
    about.setupUi()
    ui = Ui_MainWindow()
    ui.setupUi()
    ui.show()
    logic = Logic()
    sys.exit(app.exec_())
