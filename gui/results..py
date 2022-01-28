# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\results.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Results(object):
    def setupUi(self, Results):
        Results.setObjectName("Results")
        Results.resize(573, 418)
        Results.setFixedSize(QtCore.QSize(573, 418))
        self.widget = QtWidgets.QWidget(Results)
        self.widget.setGeometry(QtCore.QRect(9, 9, 551, 381))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.table_results = QtWidgets.QTableWidget(self.widget)
        self.table_results.setRowCount(0)
        self.table_results.setObjectName("table_results")
        self.table_results.setColumnCount(2)
        header = self.table_results.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.table_results.setRowCount(self.table_results.rowCount() + 1)
        self.table_results.setItem(self.table_results.rowCount(), 0, QtWidgets.QTableWidgetItem("Hello there"))
        item = QtWidgets.QTableWidgetItem()
        self.table_results.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_results.setHorizontalHeaderItem(1, item)
        self.verticalLayout.addWidget(self.table_results)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setEnabled(True)
        self.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Results)
        QtCore.QMetaObject.connectSlotsByName(Results)

    def retranslateUi(self, Results):
        _translate = QtCore.QCoreApplication.translate
        Results.setWindowTitle(_translate("Results", "Form"))
        item = self.table_results.horizontalHeaderItem(0)
        item.setText(_translate("Results", "tweet"))
        item = self.table_results.horizontalHeaderItem(1)
        item.setText(_translate("Results", "result"))
        self.pushButton.setText(_translate("Results", "Save Results"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Results = QtWidgets.QWidget()
    ui = Ui_Results()
    ui.setupUi(Results)
    Results.show()
    sys.exit(app.exec_())

