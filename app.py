from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from gui_about import Ui_AboutWindow
from gui_main import Ui_MainWindow
from PyQt5.QtGui import QCursor
import webbrowser
import subprocess
import sys


app_version = "1.3.4"


class Logic():
    def __init__(self):
        about.label_version.setText(f"Version {app_version}")
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
        ui.actionRefresh.triggered.connect(self.app_refresh)
        ui.actionHomepage.triggered.connect(self.app_homepage)
        ui.actionAbout.triggered.connect(self.app_about)
        ui.actionQuit.triggered.connect(self.app_quit)
        ui.button_uninstall.clicked.connect(self.uninstall)
        ui.button_select_all.clicked.connect(self.select_all)
        ui.button_deselect_all.clicked.connect(self.deselect_all)
        for i in self.checkbox_dict:
            i.clicked.connect(self.enable_buttons)
        self.worker = Worker(self.checkbox_dict)
        self.app_refresh()
        self.worker.finished.connect(self.thread_finished)
        self.worker.app_signal.connect(self.enable_installed)
        self.worker.progress_signal.connect(self.update_progress)

    def app_refresh(self):
        self.installed_apps = []
        for i in self.checkbox_dict:
            i.setEnabled(False)
            i.setChecked(False)
        ui.progressbar.show()
        ui.actionRefresh.setDisabled(True)
        ui.button_select_all.setDisabled(True)
        ui.button_deselect_all.setDisabled(True)
        ui.button_uninstall.setDisabled(True)
        QApplication.setOverrideCursor(QCursor(Qt.BusyCursor))
        ui.label_info.setText('Updating list of installed apps...')
        self.worker.start()

    def thread_finished(self):
        ui.progressbar.hide()
        ui.progressbar.setValue(0)
        QApplication.setOverrideCursor(QCursor())
        ui.label_info.setText('Select the default Windows 10 apps to uninstall (Hover over items to view description):')
        ui.actionRefresh.setDisabled(False)
        self.enable_buttons()

    def enable_installed(self, i):
        i.setEnabled(True)
        self.installed_apps.append(i)
        self.enable_buttons()

    @staticmethod
    def update_progress(progress):
        ui.progressbar.setValue(progress)

    def enable_buttons(self):
        self.total_size = 0
        for i in self.installed_apps:
            if i.isChecked():
                self.total_size += self.size_dict[i]
                ui.label_size.setText(f'{self.total_size:.2f} MB')
        if any(i.isChecked() for i in self.installed_apps):
            ui.button_uninstall.setDisabled(False)
            ui.button_deselect_all.setDisabled(False)
        else:
            ui.button_deselect_all.setDisabled(True)
            ui.button_uninstall.setDisabled(True)
            ui.label_size.setText('0 MB')

        if all(i.isChecked() for i in self.installed_apps):
            ui.button_select_all.setDisabled(True)
        else:
            ui.button_select_all.setDisabled(False)

    @staticmethod
    def app_homepage():
        webbrowser.open_new('https://github.com/Teraskull/PyDebloatX')

    @staticmethod
    def app_about():
        about.setWindowModality(Qt.ApplicationModal)
        about.show()

    @staticmethod
    def app_quit():
        buttonReply = QMessageBox.question(ui, 'PyDebloatX', "Quit PyDebloatX?", QMessageBox.Yes | QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
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
        buttonReply = QMessageBox.question(ui, 'PyDebloatX', f"Uninstall {j} app{'s' if j > 1 else ''}?\n\n{self.total_size:.2f} MB of of disk space will be available.", QMessageBox.Yes | QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            for i in self.installed_apps:
                if i.isChecked():
                    subprocess.Popen(["powershell", f"(Get-AppxPackage {self.checkbox_dict[i]} | Remove-AppxPackage)"], shell=True)
                    i.setChecked(False)
                    i.setEnabled(False)
            self.deselect_all()
            QMessageBox.information(ui, 'PyDebloatX', f"Uninstalling {j} app{'s' if j > 1 else ''}.", QMessageBox.Ok)


class Worker(QThread):
    end_signal = pyqtSignal()
    progress_signal = pyqtSignal(int)
    app_signal = pyqtSignal(object)

    def __init__(self, checkbox_dict):
        super().__init__()
        self.checkbox_dict = checkbox_dict

    def run(self):
        progress = 100 / 27
        for i in self.checkbox_dict:
            x = subprocess.Popen(["powershell", f"(Get-AppxPackage {self.checkbox_dict[i]}) -and $?"], stdout=subprocess.PIPE, shell=True)
            progress += 100 / 27
            self.progress_signal.emit(int(progress))
            if x.communicate()[0].decode().strip() == "True":
                self.app_signal.emit(i)
        self.end_signal.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    about = Ui_AboutWindow()
    about.setupUi()
    ui = Ui_MainWindow()
    ui.setupUi()
    logic = Logic()
    ui.show()
    sys.exit(app.exec_())
