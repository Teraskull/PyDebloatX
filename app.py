from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QCursor, QPixmap, QIcon
from gui_about import Ui_AboutWindow
from gui_main import Ui_MainWindow
import webbrowser
import subprocess
import img_res
import sys


__version__ = "1.5.0"


class Logic():
    def __init__(self):
        about.label_version.setText(f"Version {__version__}")
        self.total_size = 0
        self.checkbox_dict = {
            ui.checkBox: "*Microsoft.3DBuilder*", ui.checkBox_2: "*Microsoft.Microsoft3DViewer*", ui.checkBox_3: "*Microsoft.WindowsAlarms*",
            ui.checkBox_4: "*Microsoft.WindowsCalculator*", ui.checkBox_5: "*microsoft.windowscommunicationsapps*", ui.checkBox_6: "*Microsoft.WindowsCamera*",
            ui.checkBox_7: "*Microsoft.GetHelp*", ui.checkBox_8: "*Microsoft.ZuneMusic*", ui.checkBox_9: "*Microsoft.WindowsMaps*",

            ui.checkBox_10: "*Microsoft.Messaging*", ui.checkBox_11: "*Microsoft.BingFinance*", ui.checkBox_12: "*Microsoft.ZuneVideo*",
            ui.checkBox_13: "*Microsoft.BingNews*", ui.checkBox_14: "*Microsoft.MicrosoftOfficeHub*", ui.checkBox_15: "*Microsoft.Office.OneNote*",
            ui.checkBox_16: "*Microsoft.MSPaint*", ui.checkBox_17: "*Microsoft.People*", ui.checkBox_18: "*Microsoft.Windows.Photos*",

            ui.checkBox_19: "*Microsoft.SkypeApp*", ui.checkBox_20: "*Microsoft.MicrosoftSolitaireCollection*", ui.checkBox_21: "*Microsoft.BingSports*",
            ui.checkBox_22: "*Microsoft.Getstarted*", ui.checkBox_23: "*Microsoft.WindowsSoundRecorder*", ui.checkBox_24: "*Microsoft.BingWeather*",
            ui.checkBox_25: "*Microsoft.WindowsFeedbackHub*", ui.checkBox_26: "*xbox* | Where-Object {$_.name -notmatch 'xboxgamecallableui'}", ui.checkBox_27: "*Microsoft.YourPhone*",
        }
        self.size_dict = {
            ui.checkBox: 35.02, ui.checkBox_2: 121.46, ui.checkBox_3: 11.87,
            ui.checkBox_4: 9.27, ui.checkBox_5: 230.90, ui.checkBox_6: 49.05,
            ui.checkBox_7: 11.89, ui.checkBox_8: 50.34, ui.checkBox_9: 29.93,

            ui.checkBox_10: 30.08, ui.checkBox_11: 31.92, ui.checkBox_12: 51.80,
            ui.checkBox_13: 33.70, ui.checkBox_14: 29.97, ui.checkBox_15: 156.01,
            ui.checkBox_16: 65.79, ui.checkBox_17: 31.97, ui.checkBox_18: 346.04,

            ui.checkBox_19: 104.70, ui.checkBox_20: 134.37, ui.checkBox_21: 30.92,
            ui.checkBox_22: 16.62, ui.checkBox_23: 12.40, ui.checkBox_24: 30.59,
            ui.checkBox_25: 35.02, ui.checkBox_26: 119.06, ui.checkBox_27: 64.59,
        }
        ui.progressbar.setValue(0)
        ui.progressbar.setMaximum(len(self.checkbox_dict))
        ui.button_uninstall.clicked.connect(self.uninstall)
        ui.button_select_all.clicked.connect(self.select_all)
        ui.button_deselect_all.clicked.connect(self.deselect_all)
        ui.refresh_btn.clicked.connect(self.app_refresh)
        ui.refresh_bind.activated.connect(self.app_refresh)
        ui.homepage_btn.clicked.connect(self.app_homepage)
        ui.homepage_bind.activated.connect(self.app_homepage)
        ui.about_btn.clicked.connect(self.app_about)
        ui.about_bind.activated.connect(self.app_about)
        ui.quit_btn.clicked.connect(self.app_quit)
        ui.quit_bind.activated.connect(self.app_quit)
        about.button_quit_about.clicked.connect(self.about_close)
        for i in self.checkbox_dict:
            i.clicked.connect(self.enable_buttons)
            with open("style.css", 'r') as file:
                i.setStyleSheet(file.read())

        self.workerThread = QThread()
        self.thread_list = []
        for item, i in enumerate(self.checkbox_dict):
            self.thread_list.append(CheckApps(self.checkbox_dict, i))
            self.thread_list[item].moveToThread(self.workerThread)
            self.thread_list[item].app_signal.connect(self.enable_installed)
            self.thread_list[item].progress_signal.connect(self.update_progress)
        self.app_refresh()

    def app_refresh(self):
        self.installed_apps = []
        self.progress = 0
        for i in self.checkbox_dict:
            i.setEnabled(False)
            i.setChecked(False)
        ui.progressbar.show()
        ui.refresh_btn.setDisabled(True)
        ui.refresh_bind.setEnabled(False)
        ui.button_select_all.setDisabled(True)
        ui.button_deselect_all.setDisabled(True)
        ui.button_uninstall.setDisabled(True)
        ui.refresh_btn.setIcon(QIcon(':/icon/no_refresh_icon.png'))
        ui.button_select_all.setIcon(QIcon(':/icon/no_check_icon.png'))
        ui.button_uninstall.setIcon(QIcon(':/icon/no_trash_icon.png'))
        ui.button_deselect_all.setIcon(QIcon(':/icon/no_cancel_icon.png'))
        QApplication.setOverrideCursor(QCursor(Qt.BusyCursor))
        ui.label_info.setText('Refreshing list of installed apps...')
        for new_thread in self.thread_list:
            new_thread.start()

    def thread_finished(self):
        ui.progressbar.hide()
        ui.progressbar.setValue(0)
        QApplication.setOverrideCursor(QCursor())
        ui.label_info.setText('Select the default Windows 10 apps to uninstall (Hover over items to view description):')
        ui.refresh_btn.setDisabled(False)
        ui.refresh_bind.setEnabled(True)
        ui.refresh_btn.setIcon(QIcon(':/icon/refresh_icon.png'))
        self.enable_buttons()

    def enable_installed(self, i):
        i.setEnabled(True)
        self.installed_apps.append(i)
        self.enable_buttons()

    def update_progress(self):
        self.progress += 1
        ui.progressbar.setValue(self.progress)
        if self.progress >= len(self.checkbox_dict):
            self.thread_finished()

    def enable_buttons(self):
        self.total_size = 0
        for i in self.installed_apps:
            if i.isChecked():
                self.total_size += self.size_dict[i]
                ui.label_size.setText(f'{self.total_size:.2f} MB')
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
            ui.label_size.setText('0 MB')

        if all(i.isChecked() for i in self.installed_apps):
            ui.button_select_all.setDisabled(True)
            ui.button_select_all.setIcon(QIcon(':/icon/no_check_icon.png'))
        else:
            ui.button_select_all.setDisabled(False)
            ui.button_select_all.setIcon(QIcon(':/icon/check_icon.png'))

    @staticmethod
    def app_homepage():
        webbrowser.open_new('https://github.com/Teraskull/PyDebloatX')

    @staticmethod
    def app_about():
        about.setWindowModality(Qt.ApplicationModal)
        about.show()

    @staticmethod
    def about_close():
        about.close()

    @staticmethod
    def app_quit():
        pixmap = QPixmap('icon.ico').scaledToWidth(35, Qt.SmoothTransformation)
        msg_quit = QMessageBox()
        msg_quit.setText("Quit PyDebloatX?")
        msg_quit.addButton(QMessageBox.Yes).setProperty('class', 'button_yes')
        msg_quit.addButton(QMessageBox.No).setProperty('class', 'button_no')
        msg_quit.setWindowFlags(Qt.Dialog | Qt.CustomizeWindowHint)
        msg_quit.setWindowIcon(QIcon('icon.ico'))
        msg_quit.setWindowTitle("PyDebloatX")
        msg_quit.setIconPixmap(pixmap)
        with open("style.css", 'r') as file:
            msg_quit.setStyleSheet(file.read())
        msg_quit_result = msg_quit.exec_()
        if msg_quit_result == QMessageBox.Yes:
            app.quit()

    def select_all(self):
        for i in self.installed_apps:
            if not i.isChecked():
                i.setChecked(True)
        self.enable_buttons()

    def deselect_all(self):
        for i in self.installed_apps:
            if i.isChecked():
                i.setChecked(False)
        self.enable_buttons()

    def uninstall(self):
        j = 0
        for i in self.installed_apps:
            if i.isChecked():
                j += 1
        pixmap = QPixmap('icon.ico').scaledToWidth(35, Qt.SmoothTransformation)

        msg_confirm = QMessageBox()
        msg_confirm.setText(f"Uninstall {j} app{'s' if j > 1 else ''}?\n\n{self.total_size:.2f} MB of of disk space will be available.")
        msg_confirm.addButton(QMessageBox.Yes).setProperty('class', 'button_yes')
        msg_confirm.addButton(QMessageBox.No).setProperty('class', 'button_no')
        msg_confirm.setWindowFlags(Qt.Dialog | Qt.CustomizeWindowHint)
        msg_confirm.setWindowIcon(QIcon('icon.ico'))
        msg_confirm.setWindowTitle("PyDebloatX")
        msg_confirm.setIconPixmap(pixmap)
        with open("style.css", 'r') as file:
            msg_confirm.setStyleSheet(file.read())
        msg_confirm_result = msg_confirm.exec_()

        if msg_confirm_result == QMessageBox.Yes:
            for i in self.checkbox_dict:
                if i.isChecked():
                    subprocess.Popen(["powershell", f"(Get-AppxPackage {self.checkbox_dict[i]} | Remove-AppxPackage)"], shell=True)
                    i.setChecked(False)
                    i.setEnabled(False)
                    self.installed_apps.remove(i)
            self.deselect_all()

            msg_proceed = QMessageBox()
            msg_proceed.setText(f"Uninstalling {j} app{'s' if j > 1 else ''}.")
            msg_proceed.addButton(QMessageBox.Ok).setProperty('class', 'button_yes')
            msg_proceed.setWindowFlags(Qt.Dialog | Qt.CustomizeWindowHint)
            msg_proceed.setWindowTitle("PyDebloatX")
            msg_proceed.setIconPixmap(pixmap)
            with open("style.css", 'r') as file:
                msg_proceed.setStyleSheet(file.read())
            msg_proceed.exec_()


class CheckApps(QThread):
    progress_signal = pyqtSignal()
    app_signal = pyqtSignal(object)

    def __init__(self, checkbox_dict, i):
        super().__init__()
        self.checkbox_dict = checkbox_dict
        self.i = i

    def run(self):
        x = subprocess.Popen(["powershell", f"(Get-AppxPackage {self.checkbox_dict[self.i]}) -and $?"], stdout=subprocess.PIPE, shell=True)
        if x.communicate()[0].decode().strip() == "True":
            self.app_signal.emit(self.i)
        self.progress_signal.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    about = Ui_AboutWindow()
    about.setupUi()
    ui = Ui_MainWindow()
    ui.setupUi()
    ui.show()
    logic = Logic()
    sys.exit(app.exec_())
