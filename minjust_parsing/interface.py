from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QSize, Qt
import sys
import psycopg2

conn = psycopg2.connect(dbname='minjust', user='postgres', 
                        password='2718', host='localhost' , port=5432)
cursor = conn.cursor()

class Window(QMainWindow):
    
    page = 0
    pageSize = 15
    sortAsc = False
    orderBy = ''
    def __init__(self):
        super(Window, self).__init__()
        
        self.setWindowTitle( "Table")
        self.setGeometry(100,100,1500,768)
 
        central_widget = QWidget(self)                  # Создаём центральный виджет
        self.setCentralWidget(central_widget)           # Устанавливаем центральный виджет

        grid = QGridLayout()             # Создаём QGridLayout
        


        self.table = QTableWidget(self)  # Создаём таблицу
        self.table.setColumnCount(6)     # Устанавливаем колонки
        self.table.setHorizontalHeaderLabels(["Наименование НКО", "Учетный номер", "ОГРН","Форма","Вид отчета","Период"])
        self.table.horizontalHeader().sectionClicked.connect(self.onHeaderClicked)
        self.table.resizeColumnsToContents()

        cursor.execute(f"SELECT * FROM nko_table LIMIT {self.pageSize} ")
        self.fillTable(cursor)


        self.pageSize15 = QtWidgets.QPushButton(self)
        self.pageSize15.clicked.connect(lambda: self.getPageSize(15))
        self.pageSize15.setText('15')
        grid.addWidget(self.pageSize15, 0, 0) 

        self.pageSize30 = QtWidgets.QPushButton(self)
        self.pageSize30.clicked.connect(lambda: self.getPageSize(30))
        self.pageSize30.setText('30')
        grid.addWidget(self.pageSize30, 0, 1) 

        self.pageSize60 = QtWidgets.QPushButton(self)
        self.pageSize60.clicked.connect(lambda: self.getPageSize(60))
        self.pageSize60.setText('60')
        grid.addWidget(self.pageSize60, 0, 2) 

        #делаем ресайз колонок по содержимому
        self.table.resizeColumnsToContents()
        self.table.setColumnWidth(0,400)
        grid.addWidget(self.table, 1, 0,1,7)   # Добавляем таблицу в сетку

        self.btnBack = QtWidgets.QPushButton(self)
        self.btnBack.clicked.connect(self.pageBackward)
        self.btnBack.setText('Назад')
        grid.addWidget(self.btnBack, 2, 0) 

        self.btnBack = QtWidgets.QPushButton(self)
        self.btnBack.clicked.connect(self.pageBegin)
        self.btnBack.setText('В начало')
        grid.addWidget(self.btnBack, 2, 1) 
        
        self.btnBack = QtWidgets.QPushButton(self)
        self.btnBack.clicked.connect(self.pageEnd)
        self.btnBack.setText('В конец')
        grid.addWidget(self.btnBack, 2, 2) 

        self.btnForward = QtWidgets.QPushButton(self)
        self.btnForward.clicked.connect(self.pageForward)
        self.btnForward.setText('Вперед')
        grid.addWidget(self.btnForward, 2, 3 ) 




        self.labelNko = QtWidgets.QLabel(self)
        self.labelNko.setText('Наименование НКО')
        grid.addWidget(self.labelNko, 3, 0 ) 

        self.inputNko = QtWidgets.QLineEdit(self)
        grid.addWidget(self.inputNko, 4, 0 ) 

        self.confirmNko = QtWidgets.QPushButton(self)
        self.confirmNko.clicked.connect(self.nkoFind)
        self.confirmNko.setText('Найти')
        grid.addWidget(self.confirmNko, 5, 0 ) 


        self.labelAccName = QtWidgets.QLabel(self)
        self.labelAccName.setText('Учетный номер')
        
        grid.addWidget(self.labelNko, 3, 1 ) 

        self.inputAccName = QtWidgets.QLineEdit(self)
        grid.addWidget(self.inputAccName, 4, 1 ) 

        self.confirmAccName = QtWidgets.QPushButton(self)
        self.confirmAccName.clicked.connect(self.accNameFind)
        self.confirmAccName.setText('Найти')
        grid.addWidget(self.confirmAccName, 5, 1 ) 


        self.labelMSRN = QtWidgets.QLabel(self)
        self.labelMSRN.setText('ОГРН')
        grid.addWidget(self.labelMSRN, 3, 2 ) 

        self.inputMSRN = QtWidgets.QLineEdit(self)
        grid.addWidget(self.inputMSRN, 4, 2 ) 

        self.confirmMSRN = QtWidgets.QPushButton(self)
        self.confirmMSRN.clicked.connect(self.msrnFind)
        self.confirmMSRN.setText('Найти')
        grid.addWidget(self.confirmMSRN, 5, 2 ) 



        self.labelForm = QtWidgets.QLabel(self)
        self.labelForm.setText('Форма')
        grid.addWidget(self.labelForm, 3, 3 ) 

        self.inputForm = QtWidgets.QLineEdit(self)
        grid.addWidget(self.inputForm, 4, 3 ) 

        self.confirmForm = QtWidgets.QPushButton(self)
        self.confirmForm.clicked.connect(self.formFind)
        self.confirmForm.setText('Найти')
        grid.addWidget(self.confirmForm, 5, 3 ) 



        self.labelTypeReport = QtWidgets.QLabel(self)
        self.labelTypeReport.setText('Вид отчёта')
        grid.addWidget(self.labelTypeReport, 3, 4 ) 

        self.inputTypeReport = QtWidgets.QLineEdit(self)
        grid.addWidget(self.inputTypeReport, 4, 4 ) 

        self.confirmTypeReport = QtWidgets.QPushButton(self)
        self.confirmTypeReport.clicked.connect(self.typeReportFind)
        self.confirmTypeReport.setText('Найти')
        grid.addWidget(self.confirmTypeReport, 5, 4 ) 



        self.labelPeriod = QtWidgets.QLabel(self)
        self.labelPeriod.setText('Период')
        grid.addWidget(self.labelPeriod, 3, 5 ) 

        self.inputPeriod = QtWidgets.QLineEdit(self)
        grid.addWidget(self.inputPeriod, 4, 5 ) 

        self.confirmPeriod = QtWidgets.QPushButton(self)
        self.confirmPeriod.clicked.connect(self.periodFind)
        self.confirmPeriod.setText('Найти')
        grid.addWidget(self.confirmPeriod, 5, 5 )

        self.findTable = QTableWidget(self)  # Создаём таблицу
        self.findTable.setColumnCount(6)     # Устанавливаем колонки
        self.findTable.setHorizontalHeaderLabels(["Наименование НКО", "Учетный номер", "ОГРН","Форма","Вид отчета","Период"])
        self.findTable.horizontalHeader().sectionClicked.connect(self.onHeaderClicked)
        self.findTable.resizeColumnsToContents()
        grid.addWidget(self.findTable, 7, 0, 1, 7 ) 


        grid.setSpacing(20)
        central_widget.setLayout(grid)   # Устанавливаем данное размещение в центральный виджет


    def fillTable(self,cursor):
        # self.pageSize*(self.page)
        self.table.setRowCount(0)
        rowCounter = 0
        for row in cursor:
            itemCounter = 0
            self.table.insertRow(rowCounter)
            for  item in row:
                self.table.setItem(rowCounter, itemCounter, QTableWidgetItem(item))
                itemCounter += 1
            rowCounter +=1
    def fillFindTable(self,cursor):
        self.table.setColumnWidth(0,400)
        self.findTable.setRowCount(0)
        rowCounter = 0
        for row in cursor:
            itemCounter = 0
            self.findTable.insertRow(rowCounter)
            for  item in row:
                self.findTable.setItem(rowCounter, itemCounter, QTableWidgetItem(item))
                itemCounter += 1
            rowCounter +=1
        self.findTable.resizeColumnsToContents()

    def onHeaderClicked(self,logicalIndex):
        self.page -=1
        self.sortAsc = not self.sortAsc
        self.sortMode = 'ASC' if self.sortAsc else 'DESC'
        self.orderBy = f'ORDER BY {logicalIndex+1} {self.sortMode} '
        cursor.execute(f"SELECT * FROM nko_table {self.orderBy} LIMIT {self.pageSize} ")
        self.fillTable(cursor)
        
        
    def pageBackward(self):
        if(not (self.page == 0) ):
            self.page -=1
        else:

            pass
        cursor.execute(f"SELECT * FROM nko_table {self.orderBy} LIMIT {self.pageSize} OFFSET {self.pageSize*self.page}")
        self.fillTable(cursor)

    def pageForward(self):
        self.page +=1
        print(self.pageSize*self.page)
        cursor.execute(f"SELECT * FROM nko_table {self.orderBy} LIMIT {self.pageSize} OFFSET {self.pageSize*self.page}")
        self.fillTable(cursor)

    def getPageSize(self, num):
        self.pageSize = num
        self.page = 0
        cursor.execute(f"SELECT * FROM nko_table {self.orderBy} LIMIT {self.pageSize} ")
        self.fillTable(cursor)
    def pageBegin(self):
        self.page = 0
        cursor.execute(f"SELECT * FROM nko_table {self.orderBy} LIMIT {self.pageSize} ")
        self.fillTable(cursor)

    def pageEnd(self):
        self.page = 0
        cursor.execute(f"SELECT COUNT(*) FROM nko_table")
        count = cursor.fetchone()[0]
        self.page = count / self.pageSize
        cursor.execute(f"SELECT * FROM nko_table {self.orderBy}  LIMIT {self.pageSize} OFFSET {self.pageSize*(self.page-1)}")
        self.fillTable(cursor)

    def nkoFind(self):
        print(self.inputNko.text())
        cursor.execute(f"SELECT * FROM nko_table WHERE nko_name = '{self.inputNko.text()}'")
        self.fillFindTable(cursor)
    def accNameFind(self):
        cursor.execute(f"SELECT * FROM nko_table WHERE acc_name = '{self.inputAccName.text()}'")
        self.fillFindTable(cursor)
    def msrnFind(self):
        cursor.execute(f"SELECT * FROM nko_table WHERE msrn = '{self.inputMSRN.text()}'")
        self.fillFindTable(cursor)
    def formFind(self):
        cursor.execute(f"SELECT * FROM nko_table WHERE form = '{self.inputForm.text()}'")
        self.fillFindTable(cursor)
    def typeReportFind(self):
        cursor.execute(f"SELECT * FROM nko_table WHERE type_of_report = '{self.inputTypeReport.text()}'")
        self.fillFindTable(cursor)
    def periodFind(self):
        cursor.execute(f"SELECT * FROM nko_table WHERE period = '{self.inputPeriod.text()}'")
        self.fillFindTable(cursor)


def application():
    app = QApplication(sys.argv)
    window  = Window()


    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    application()