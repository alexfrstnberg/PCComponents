import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QTableWidgetItem
import pandas as pd
from Components.Component import *

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
       
        l1 = QtWidgets.QLabel(self.centralwidget)
        l1.setText("<h1 style='color:magenta;'>Components DB</h1>")
        l1.move(290, 23)
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(20, 70, 75, 23))
        self.add.setText("Add")
        self.add.clicked.connect(self._addRow)


        self.delete_2 = QtWidgets.QPushButton(self.centralwidget)
        self.delete_2.setGeometry(QtCore.QRect(110, 70, 75, 23))
        self.delete_2.setText("Delete")
        self.delete_2.clicked.connect(self._removeRow)



        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(200, 70, 75, 23))
        self.save.setText("Save")
        self.save.clicked.connect(self.exportToExcel)


        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 110, 646, 451))
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(1)
        self.fill_cells()
        self.tableWidget.setObjectName("tableWidget")


        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslate_table(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslate_table(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
   
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Country"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Prod date"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Price"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Quantity"))

    def exportToExcel(self):
        columnHeaders = []

        # create column header list
        for j in range(self.tableWidget.model().columnCount()):
            columnHeaders.append(self.tableWidget.horizontalHeaderItem(j).text())

        list = []
        # create dataframe object recordset
        for row in range(self.tableWidget.rowCount()):
            name = self.tableWidget.item(row, 0).text()
            country = self.tableWidget.item(row, 1).text() 
            prod_date = self.tableWidget.item(row, 2).text()
            price = self.tableWidget.item(row, 3).text()
            quantity = self.tableWidget.item(row, 4).text()
            item = Component(name, country, prod_date, price, quantity)
            list.append(item)
            
        df = pd.DataFrame([vars(i) for i in list])
        df.to_excel('Components.xlsx', index=False)
        print('Excel file exported') 
  
    def fill_cells(self):
        for i in range(self.tableWidget.model().columnCount()):
            self.tableWidget.setItem(self.tableWidget.model().rowCount()-1, i, QTableWidgetItem(''))

    def _addRow(self):
        rowCount = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowCount)  
        self.fill_cells()

    def _removeRow(self):
        if self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(self.tableWidget.rowCount()-1)
    
    

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
MainWindow.show()
sys.exit(app.exec_())
