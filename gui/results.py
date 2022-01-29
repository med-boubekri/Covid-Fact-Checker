# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\results.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from  PyQt5.QtGui import QColor
from PyQt5.QtWidgets import  QFileDialog,QMessageBox
import csv 
from pathlib import Path
import xlsxwriter 
import re 

HOME = str(Path.home())

class Ui_Results(object):
    def __init__(self , results) :
        if results : self.results = results
    def setupUi(self, Results):
        self.Results = Results
        Results.setObjectName("Results")
        Results.resize(611, 418)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Results)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.table_results = QtWidgets.QTableWidget(Results)
        self.table_results.setRowCount(0)
        self.table_results.setObjectName("table_results")
        self.table_results.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.table_results.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_results.setHorizontalHeaderItem(1, item)
        header = self.table_results.horizontalHeader()      
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.verticalLayout.addWidget(self.table_results)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.line = QtWidgets.QFrame(Results)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Save_to_file = QtWidgets.QPushButton(Results)
        self.Save_to_file.setEnabled(True)
        self.Save_to_file.setIconSize(QtCore.QSize(50, 50))
        self.Save_to_file.setObjectName("Save_to_file")
        self.horizontalLayout.addWidget(self.Save_to_file)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.showresults()
        self.retranslateUi(Results)
        QtCore.QMetaObject.connectSlotsByName(Results)
        self.Save_to_file.clicked.connect(self.save)
    def save(self) : 
        name = QFileDialog.getSaveFileName(self.Results ,  'Save File' , HOME ,"CSV (*csv);; EXCEL (*xlsx)")
        print(name)
        index = 0 
        columns = ["id" , "tweets" , "result"]
        check =lambda  x: re.sub(r"^[^\.]+" , '',x)
        ext = check(name[0])
        file_name = name[0]
        if name[1] == 'CSV (*csv)' : 
            if ext == '' :
                file_name += '.csv'
            elif ext != '' and ext != '.csv' : 
                return self.error("Extension isn't csv")
            with open(name[1], "w", newline='') as outfile:
                writer = csv.writer(outfile) 
                writer.writerow(columns)
                for key in self.results.keys() :
                    writer.writerow([index , key , self.results[key]])
                    index += 1
        elif name[1] == 'EXCEL (*xlsx)'  :
            if ext == '' :
                file_name += '.csv'
            elif ext != '' and ext != '.csv' : 
                return self.error("Extension isn't excel")
            workbook = xlsxwriter.Workbook(file_name)
            worksheet = workbook.add_worksheet()
            index = 0
            worksheet.write("A1" , "ID")
            worksheet.write("B1" , "tweet")
            worksheet.write("C1" , "resut")
            for key in self.results.keys() :
                    worksheet.write("A"+ str(index+2) , str(index))
                    worksheet.write("B"+ str(index+2) , str(key))
                    worksheet.write("C"+ str(index+2) , str(self.results[key]))
                    index += 1
            workbook.close()

    def showresults(self) : 
        for key in self.results.keys() : 
            rowPosition = self.table_results.rowCount()
            self.table_results.insertRow(rowPosition)
            real = QtWidgets.QTableWidgetItem(self.results[key])
            if self.results[key].lower() == "real" : 
                real.setBackground(QColor(0 , 255 , 77))
            else : 
                real.setBackground(QColor(255 , 230 , 0))
            tweet = QtWidgets.QTableWidgetItem(key)
            self.table_results.setItem(rowPosition, 0, tweet)
            self.table_results.setItem(rowPosition, 1, real)
            
    def retranslateUi(self, Results):
        _translate = QtCore.QCoreApplication.translate
        Results.setWindowTitle(_translate("Results", "Form"))
        item = self.table_results.horizontalHeaderItem(0)
        item.setText(_translate("Results", "Tweet"))
        item = self.table_results.horizontalHeaderItem(1)
        item.setText(_translate("Results", "Result"))
        self.Save_to_file.setText(_translate("Results", "Save Results"))
    def error(self ,message) : 
        """generate a error Message Box"""
        print(message)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText(message)
        msg.setWindowTitle("Error")
        msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Results = QtWidgets.QWidget()
    with open("src/style.css") as fd : 
        app.setStyleSheet(fd.read())
    d= {"helllo": "Real" , "hehe" : 'Fake'}
    ui = Ui_Results(d)
    ui.setupUi(Results)
    Results.show()
    sys.exit(app.exec_())

