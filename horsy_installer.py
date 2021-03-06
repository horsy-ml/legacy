from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from modules.path import add_to_path, add_var
import modules.images
import urllib.request
import os
import threading
import ctypes
import winshell
from win32com.client import Dispatch
import pythoncom


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(502, 364)
        MainWindow.setMinimumSize(QtCore.QSize(502, 364))
        MainWindow.setMaximumSize(QtCore.QSize(502, 364))
        MainWindow.setWindowOpacity(0.98)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/horsy_white32x32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QWidget{\n"
                                 "    background-color: rgb(30, 30, 30);\n"
                                 "}\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horsy_logo_lefttop = QtWidgets.QLabel(self.centralwidget)
        self.horsy_logo_lefttop.setGeometry(QtCore.QRect(10, 10, 32, 32))
        self.horsy_logo_lefttop.setStyleSheet("background: none;")
        self.horsy_logo_lefttop.setText("")
        self.horsy_logo_lefttop.setPixmap(QtGui.QPixmap(":/images/horsy_white32x32.png"))
        self.horsy_logo_lefttop.setObjectName("horsy_logo_lefttop")
        self.path_box = QtWidgets.QLineEdit(self.centralwidget)
        self.path_box.setGeometry(QtCore.QRect(20, 70, 351, 51))
        self.path_box.setStyleSheet("background-color: rgb(74, 76, 83);\n"
                                    "border-radius: 5px;    \n"
                                    "color: rgb(242, 242, 242);")
        self.path_box.setInputMask("")
        self.path_box.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.path_box.setObjectName("path_box")
        self.choose_path_button = QtWidgets.QPushButton(self.centralwidget)
        self.choose_path_button.setEnabled(True)
        self.choose_path_button.setGeometry(QtCore.QRect(380, 70, 101, 50))
        self.choose_path_button.setMinimumSize(QtCore.QSize(0, 50))
        self.choose_path_button.setStyleSheet("QPushButton {\n"
                                              "    color: rgb(204, 204, 204);\n"
                                              "    border-width: 1px;\n"
                                              "    border-radius:6px;\n"
                                              "    border-style: solid;\n"
                                              "    background-color: rgb(28, 30, 33);\n"
                                              "    border-color: rgb(66, 143, 225);\n"
                                              "}\n"
                                              "QPushButton:hover{\n"
                                              "    border-width: 2px;\n"
                                              "}\n"
                                              "QPushButton:pressed{\n"
                                              "    background-color: rgb(50, 60, 63);\n"
                                              "}\n"
                                              "QPushButton:disabled{\n"
                                              "    border-width: 0px;\n"
                                              "    background-color: rgb(92, 99, 109);\n"
                                              "}")
        self.choose_path_button.setObjectName("choose_path_button")
        self.horsy_text_lefttop = QtWidgets.QLabel(self.centralwidget)
        self.horsy_text_lefttop.setGeometry(QtCore.QRect(50, 10, 231, 30))
        self.horsy_text_lefttop.setStyleSheet("color: white;\n"
                                              "font: 18pt \"MS Shell Dlg 2\";\n"
                                              "background: none;")
        self.horsy_text_lefttop.setObjectName("horsy_text_lefttop")
        self.path_message = QtWidgets.QTextBrowser(self.centralwidget)
        self.path_message.setGeometry(QtCore.QRect(20, 50, 321, 21))
        self.path_message.setStyleSheet("color: white;\n"
                                        "border: none;\n"
                                        "background-color: rgba(255, 255, 255, 0);")
        self.path_message.setAcceptRichText(False)
        self.path_message.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.path_message.setObjectName("path_message")
        self.install_horsy_check = QtWidgets.QCheckBox(self.centralwidget)
        self.install_horsy_check.setEnabled(False)
        self.install_horsy_check.setGeometry(QtCore.QRect(20, 130, 91, 17))
        self.install_horsy_check.setStyleSheet("color: white;")
        self.install_horsy_check.setChecked(True)
        self.install_horsy_check.setObjectName("install_horsy_chech")
        self.install_gui_check = QtWidgets.QCheckBox(self.centralwidget)
        self.install_gui_check.setEnabled(True)
        self.install_gui_check.setGeometry(QtCore.QRect(30, 150, 111, 17))
        self.install_gui_check.setStyleSheet("color: white;")
        self.install_gui_check.setChecked(True)
        self.install_gui_check.setObjectName("install_gui_check")
        self.install_button = QtWidgets.QPushButton(self.centralwidget)
        self.install_button.setEnabled(True)
        self.install_button.setGeometry(QtCore.QRect(150, 300, 201, 50))
        self.install_button.setMinimumSize(QtCore.QSize(0, 50))
        self.install_button.setStyleSheet("QPushButton {\n"
                                          "    color: rgb(204, 204, 204);\n"
                                          "    border-width: 1px;\n"
                                          "    border-radius:6px;\n"
                                          "    border-style: solid;\n"
                                          "    background-color: rgb(28, 30, 33);\n"
                                          "    border-color: rgb(66, 143, 225);\n"
                                          "}\n"
                                          "QPushButton:hover{\n"
                                          "    border-width: 2px;\n"
                                          "}\n"
                                          "QPushButton:pressed{\n"
                                          "    background-color: rgb(50, 60, 63);\n"
                                          "}\n"
                                          "QPushButton:disabled{\n"
                                          "    border-width: 0px;\n"
                                          "    background-color: rgb(92, 99, 109);\n"
                                          "}")
        self.install_button.setObjectName("install_button")
        self.logs_box = QtWidgets.QTextBrowser(self.centralwidget)
        self.logs_box.setGeometry(QtCore.QRect(20, 180, 461, 101))
        self.logs_box.setMinimumSize(QtCore.QSize(0, 0))
        self.logs_box.setMaximumSize(QtCore.QSize(1000, 1000))
        self.logs_box.setStyleSheet("background-color: rgb(74, 76, 83);\n"
                                    "border-radius: 5px;    \n"
                                    "color: rgb(242, 242, 242);")
        self.logs_box.setAcceptRichText(False)
        self.logs_box.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.logs_box.setObjectName("logs_box")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 150, 16, 16))
        self.label.setStyleSheet("color: white;\n"
                                 "background: none")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "horsy legacy - installation"))
        self.path_box.setPlaceholderText(_translate("MainWindow", "Installation folder, apps will be stored here"))
        self.choose_path_button.setText(_translate("MainWindow", "Choose path"))
        self.horsy_text_lefttop.setText(_translate("MainWindow", "hlegacy - installation"))
        self.path_message.setHtml(_translate("MainWindow",
                                             "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                             "p, li { white-space: pre-wrap; }\n"
                                             "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Installation folder, apps will be stored here</p></body></html>"))
        self.install_horsy_check.setText(_translate("MainWindow", "Install horsy"))
        self.install_gui_check.setText(_translate("MainWindow", "Install horsy GUI"))
        self.install_button.setText(_translate("MainWindow", "Install"))
        self.logs_box.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.logs_box.setPlaceholderText(_translate("MainWindow", "Logs"))
        self.label.setText(_translate("MainWindow", "-"))

    def openFile(self, MainWindow):
        self.path_box.setText(str(os.path.join(QtWidgets.QFileDialog.getExistingDirectory(
            self.centralwidget, 'Installation folder')) + "\horsy").replace("/", "\\").replace('\\\\', '\\'))


ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
ui.path_box.setText(os.path.expanduser("~") + "\horsy")
MainWindow.show()


def install():
    path_to_install = os.path.join(ui.path_box.text()).replace("/", "\\").replace('\\\\', '\\')
    ui.logs_box.clear()
    if path_to_install == "":
        ui.logs_box.append("Please choose path to install")
        return
    if not os.path.exists(path_to_install):
        os.makedirs(path_to_install)
    if not os.path.exists(path_to_install + "\\apps"):
        os.makedirs(path_to_install + "\\apps")
    threads = list()
    ui.logs_box.append("Adding task to download horsy")
    threads.append(threading.Thread(target=urllib.request.urlretrieve,
                                    args=("https://github.com/horsy-ml/legacy/raw/master/bin/horsy.exe",
                                          os.path.join(path_to_install) + '/horsy.exe'), ))
    if ui.install_gui_check.isChecked():
        ui.logs_box.append("Adding task to download horsygui")
        threads.append(threading.Thread(target=urllib.request.urlretrieve,
                                        args=("https://github.com/horsy-ml/legacy/raw/master/bin/horsygui.exe",
                                              os.path.join(path_to_install) + '/horsygui.exe'), ))
    try:
        ui.logs_box.append("Starting tasks")
        for thread in threads:
            thread.start()
    except:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()

    ui.logs_box.append("Adding to PATH")
    add_var(path_to_install)
    add_to_path(os.path.join(path_to_install))
    ui.logs_box.append("Downloading version file")
    urllib.request.urlretrieve("https://github.com/horsy-ml/legacy/raw/master/web_vars/version",
                               os.path.join(path_to_install) + '/apps/version')
    ui.logs_box.append("Version specified")

    def wait_for_finish():
        for thread in threads:
            thread.join()
        ui.logs_box.append("Downloading finished")
        if ui.install_gui_check.isChecked():
            ui.logs_box.append("Creating shortcuts")
            desktop = winshell.desktop()
            path = os.path.join(desktop, "horsy legacy GUI.lnk")
            target = os.path.join(path_to_install) + '/horsygui.exe'
            wDir = os.path.join(path_to_install)
            icon = os.path.join(path_to_install) + '/horsygui.exe'
            pythoncom.CoInitializeEx(0)
            shell = Dispatch('WScript.Shell')
            shortcut = shell.CreateShortCut(path)
            shortcut.Targetpath = target
            shortcut.WorkingDirectory = wDir
            shortcut.IconLocation = icon
            shortcut.save()
        ui.logs_box.append("Installation complete")

    threading.Thread(target=wait_for_finish).start()


ui.choose_path_button.clicked.connect(ui.openFile)
ui.install_button.clicked.connect(install)

sys.exit(app.exec_())
