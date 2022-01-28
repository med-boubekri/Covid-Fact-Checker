# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import  QFileDialog,QMessageBox
from pathlib import Path
import os

HOME = str(Path.home())

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(433, 272)
        MainWindow.setMinimumSize(QtCore.QSize(30, 30))
        self.main_widget = QtWidgets.QWidget(MainWindow)
        self.main_widget.setObjectName("main_widget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.main_widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(19, 9, 371, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.vertical_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.vertical_layout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout.setObjectName("vertical_layout")
        spacerItem = QtWidgets.QSpacerItem(10, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.vertical_layout.addItem(spacerItem)
        self.brows_layout = QtWidgets.QHBoxLayout()
        self.brows_layout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.brows_layout.setObjectName("brows_layout")
        self.file_path_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.file_path_edit.setObjectName("file_path_edit")
        self.brows_layout.addWidget(self.file_path_edit)
        self.browse_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.browse_button.setObjectName("browse_button")
        self.brows_layout.addWidget(self.browse_button)
        self.vertical_layout.addLayout(self.brows_layout)
        spacerItem1 = QtWidgets.QSpacerItem(10, 70, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.vertical_layout.addItem(spacerItem1)
        self.launch_layout = QtWidgets.QHBoxLayout()
        self.launch_layout.setObjectName("launch_layout")
        spacerItem2 = QtWidgets.QSpacerItem(90, 50, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.launch_layout.addItem(spacerItem2)
        self.real_or_fake = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.real_or_fake.setMinimumSize(QtCore.QSize(70, 50))
        self.real_or_fake.setIconSize(QtCore.QSize(30, 30))
        self.real_or_fake.setObjectName("real_or_fake")
        self.launch_layout.addWidget(self.real_or_fake)
        spacerItem3 = QtWidgets.QSpacerItem(90, 10, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.launch_layout.addItem(spacerItem3)
        self.vertical_layout.addLayout(self.launch_layout)
        MainWindow.setCentralWidget(self.main_widget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 433, 21))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionRecent = QtWidgets.QAction(MainWindow)
        self.actionRecent.setObjectName("actionRecent")
        self.actionSource = QtWidgets.QAction(MainWindow)
        self.actionSource.setObjectName("actionSource")
        self.actionLICENSE = QtWidgets.QAction(MainWindow)
        self.actionLICENSE.setObjectName("actionLICENSE")
        self.actionRecent_2 = QtWidgets.QAction(MainWindow)
        self.actionRecent_2.setObjectName("actionRecent_2")
        self.menu_file.addAction(self.actionRecent_2)
        self.menu_help.addAction(self.actionSource)
        self.menu_help.addSeparator()
        self.menu_help.addAction(self.actionLICENSE)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.browse_button.clicked.connect(self.browsfiles)
        self.real_or_fake.clicked.connect(self.startmodel)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.browse_button.setText(_translate("MainWindow", "Browse"))
        self.real_or_fake.setText(_translate("MainWindow", "Real or Fake"))
        self.menu_file.setTitle(_translate("MainWindow", "File"))
        self.menu_help.setTitle(_translate("MainWindow", "About"))
        self.actionRecent.setText(_translate("MainWindow", "Recent"))
        self.actionSource.setText(_translate("MainWindow", "Source Code"))
        self.actionLICENSE.setText(_translate("MainWindow", "License"))
        self.actionRecent_2.setText(_translate("MainWindow", "Recent Files"))
    def browsfiles(self) : 
        fname = QFileDialog.getOpenFileName(self.main_widget , 'Open File' , HOME , "TXT (*.txt))")
        self.file_path_edit.setText(fname[0])
    def startmodel(self) : 
        if self.file_path_edit.text() != "" :
            print("We got  a file olla")
        else : 
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText("File not specified or extension not known \n ")
            msg.setWindowTitle("Error")
            msg.exec_()
            return
        file  = self.file_path_edit.text() 
        if os.access('does_not_exist.txt', os.R_OK) == False : 
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText("cannot access file\n ")
            msg.setWindowTitle("Error")
            msg.exec_()
            return
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

