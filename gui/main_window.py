# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QFileDialog,QMessageBox
from pathlib import Path
from gui.src.clean import CleanData
from gui.src.model import Train
from gui.results import Ui_Results
import os, sys 

HOME = str(Path.home())

class Ui_MainWindow(object):
    def __init__(self , model):
        self.model = model
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(433, 272)
        MainWindow.setFixedSize(QtCore.QSize(433, 272))
        MainWindow.setWindowIcon(QtGui.QIcon("images/logo.png"))
        self.main_widget = QtWidgets.QWidget(MainWindow)
        self.main_widget.setObjectName("main_widget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.main_widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(19, 9, 371, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.vertical_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.vertical_layout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout.setObjectName("vertical_layout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setMaximumSize(QtCore.QSize(10000, 25))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.vertical_layout.addWidget(self.label)
        self.brows_layout = QtWidgets.QHBoxLayout()
        self.brows_layout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.brows_layout.setObjectName("brows_layout")
        self.file_path_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.file_path_edit.setMinimumSize(QtCore.QSize(60, 30))
        self.file_path_edit.setObjectName("file_path_edit")
        self.brows_layout.addWidget(self.file_path_edit)
        self.browse_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.browse_button.setMinimumSize(QtCore.QSize(80, 30))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Tweet Spam Covid 19 Detector v1.0 "))
        self.label.setText(_translate("MainWindow", "Please choose a file containing the tweets"))
        self.browse_button.setText(_translate("MainWindow", "Browse"))
        self.real_or_fake.setText(_translate("MainWindow", "Real or Fake"))
        self.menu_file.setTitle(_translate("MainWindow", "File"))
        self.menu_help.setTitle(_translate("MainWindow", "About"))
        self.actionRecent.setText(_translate("MainWindow", "Recent"))
        self.actionSource.setText(_translate("MainWindow", "Source Code"))
        self.actionLICENSE.setText(_translate("MainWindow", "License"))
        self.actionRecent_2.setText(_translate("MainWindow", "Recent Files"))
    def browsfiles(self) : 
        fname = QFileDialog.getOpenFileName(self.main_widget , 'Open File' , HOME , "TXT (*.txt)")
        self.file_path_edit.setText(fname[0])
    def startmodel(self) : 
        if self.file_path_edit.text()  == "": 
            self.error("file not found")
            return
        file  = self.file_path_edit.text() 
        if os.access(file, os.R_OK) == False : 
            self.error("cannot access file")
            return
        number_lines = 0
        results = {}
        with open(file , 'r' , errors="ignore") as fd : 
            lines = fd.readlines()
            for line in lines : 
                line = line.strip()
                if line == "" : 
                    continue
                results[line] = self.predict(line)
                number_lines += 1
        self.nextpage(results)
    def nextpage(self , results) :
        """redirect to the results page"""
        self.Results = QtWidgets.QWidget()
        self.ui = Ui_Results(results)
        self.ui.setupUi(self.Results)
        self.Results.show()
    def predict(self , line) :
        """predict a tweet if it is real (true) or fake (false)"""
        line = line.strip()
        tweet_cleaned = CleanData.clean(line)
        real = self.model.predict(tweet_cleaned)
        if real :
            return "Real"
        else : 
            return "Fake"
    def error(self ,message) : 
        """generate a error Message Box"""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText(message + "\n ")
        msg.setWindowTitle("Error")
        msg.exec_()



def main(): 
    #Clean Train Set
    os.chdir("gui")
    inFile = "../Dataset/TrainSet.xlsx"
    outFile = "../results/Cleaned_DS_test.csv"
    train_set_data = CleanData( inFile , debug=True  , test = False)
    #Clean Test set
    inFile= "../Dataset/TestSet.xlsx"
    test_set_data = CleanData( inFile , debug=True , test = True )
    #Training the model
    tester = Train(train_set_data.Dataset ,train_set_data.targets , test_set_data.Dataset , test_set_data.targets , debug=True)
    #Starting the app
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    with open("src/style.css") as fd : 
        app.setStyleSheet(fd.read())
    ui = Ui_MainWindow(tester)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
