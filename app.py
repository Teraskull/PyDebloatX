from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from gui_about import Ui_AboutWindow
from gui_main import Ui_MainWindow
from PyQt5.QtGui import QCursor
import webbrowser
import subprocess
import sys


app_version = "1.3.1"


class Logic():
    def __init__(self):
        about.label_version.setText(f"Version {app_version}")
        self.installed_apps = []
        self.checkbox_dict = {
            ui.checkBox: "*Microsoft.Microsoft3DViewer*", ui.checkBox_2: "*Microsoft.WindowsAlarms*", ui.checkBox_3: "*Microsoft.WindowsCalculator*",
            ui.checkBox_4: "*microsoft.windowscommunicationsapps*", ui.checkBox_5: "*Microsoft.WindowsCamera*", ui.checkBox_6: "*Microsoft.GetHelp*",
            ui.checkBox_7: "*Microsoft.Getstarted*", ui.checkBox_8: "*Microsoft.ZuneMusic*", ui.checkBox_9: "*Microsoft.WindowsMaps*",

            ui.checkBox_10: "*Microsoft.Messaging*", ui.checkBox_11: "*Microsoft.BingFinance*", ui.checkBox_12: "*Microsoft.ZuneVideo*",
            ui.checkBox_13: "*Microsoft.BingNews*", ui.checkBox_14: "*Microsoft.MicrosoftOfficeHub*", ui.checkBox_15: "*Microsoft.Office.OneNote*",
            ui.checkBox_16: "*Microsoft.MSPaint*", ui.checkBox_17: "*Microsoft.People*", ui.checkBox_18: "*Microsoft.Windows.Photos*",

            ui.checkBox_19: "*Microsoft.SkypeApp*", ui.checkBox_20: "*Microsoft.MicrosoftSolitaireCollection*", ui.checkBox_21: "*Microsoft.BingSports*",
            ui.checkBox_22: "*Microsoft.WindowsStore*", ui.checkBox_23: "*Microsoft.WindowsSoundRecorder*", ui.checkBox_24: "*Microsoft.BingWeather*",
            ui.checkBox_25: "*Microsoft.WindowsFeedbackHub*", ui.checkBox_26: "*xbox* | Where-Object {$_.name -notmatch 'xboxgamecallableui'}", ui.checkBox_27: "*Microsoft.YourPhone*",
        }
        ui.button_deselect_all.setDisabled(True)
        ui.button_uninstall.setDisabled(True)
        self.worker = Worker()
        self.worker.start()
        self.worker.finished.connect(self.thread_finished)
        self.worker.progress_signal.connect(self.update_progress)

    def logic_setup(self):
        ui.actionRefresh.triggered.connect(self.app_refresh)
        ui.actionHomepage.triggered.connect(self.app_homepage)
        ui.actionAbout.triggered.connect(self.app_about)
        ui.actionQuit.triggered.connect(self.app_quit)
        ui.button_uninstall.clicked.connect(self.uninstall)
        ui.button_select_all.clicked.connect(self.select_all)
        ui.button_deselect_all.clicked.connect(self.deselect_all)
        for i in self.checkbox_dict:
            i.clicked.connect(self.enable_buttons)

    def thread_finished(self):
        ui.progressbar.hide()
        ui.progressbar.setValue(0)
        QApplication.setOverrideCursor(QCursor())
        ui.label_info.setText('Select the default Windows 10 apps to uninstall:')
        ui.actionRefresh.setDisabled(False)
        ui.button_select_all.setDisabled(False)
        for i in self.installed_apps:
            i.setEnabled(True)

    @staticmethod
    def update_progress(progress):
        ui.progressbar.setValue(progress)

    def enable_buttons(self):
        if any(i.isChecked() for i in self.installed_apps):
            ui.button_uninstall.setDisabled(False)
            ui.button_deselect_all.setDisabled(False)
        else:
            ui.button_deselect_all.setDisabled(True)
            ui.button_uninstall.setDisabled(True)

        if all(i.isChecked() for i in self.installed_apps):
            ui.button_select_all.setDisabled(True)
        else:
            ui.button_select_all.setDisabled(False)

    def app_refresh(self):
        self.worker.start()

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
        buttonReply = QMessageBox.question(ui, 'PyDebloatX', f"Uninstall {j} selected app(s)?", QMessageBox.Yes | QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            for i in self.checkbox_dict:
                if i.isChecked():
                    subprocess.Popen(f'powershell Get-AppxPackage {self.checkbox_dict[i]} | Remove-AppxPackage')
                    i.setChecked(False)
                    i.setEnabled(False)
            self.deselect_all()
            QMessageBox.information(ui, 'PyDebloatX', f"Uninstalling {j} app(s).", QMessageBox.Ok)


class Worker(QThread):
    end_signal = pyqtSignal()
    progress_signal = pyqtSignal(int)

    def run(self):
        logic.installed_apps = []
        ui.progressbar.show()
        ui.actionRefresh.setDisabled(True)
        ui.button_select_all.setDisabled(True)
        QApplication.setOverrideCursor(QCursor(Qt.BusyCursor))
        progress = 100 / 27
        for i in logic.checkbox_dict:
            i.setEnabled(False)
        for i in logic.checkbox_dict:
            x = subprocess.Popen(["powershell", f"(Get-AppxPackage {logic.checkbox_dict[i]}) -and ($true)"], stdout=subprocess.PIPE).communicate()[0]
            progress += 100 / 27
            self.progress_signal.emit(int(progress))
            if x.decode().strip() == "True":
                logic.installed_apps.append(i)
        self.end_signal.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    about = Ui_AboutWindow()
    about.setupUi()
    ui = Ui_MainWindow()
    ui.setupUi()
    logic = Logic()
    logic.logic_setup()
    ui.show()
    sys.exit(app.exec_())
