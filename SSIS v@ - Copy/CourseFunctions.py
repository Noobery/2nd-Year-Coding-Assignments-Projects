import sqlite3
from sqlite3 import Error
from PySide6.QtWidgets import QTableWidgetItem, QComboBox

class appFunctions1():
    def __init__(self, arg):
        super(appFunctions1, self).__init__()
        self.arg = arg

    @staticmethod
    def createConnection(db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)
        return conn

    @staticmethod
    def createTable(conn, createTableSql):
        try:
            c = conn.cursor()
            c.execute(createTableSql)
        except Error as e:
            print(e)

    @staticmethod
    def main1(dbFolder):
        createUserTable = """CREATE TABLE IF NOT EXISTS Students1 (
                                ID TEXT PRIMARY KEY,
                                FULL_NAME TEXT,
                                GENDER TEXT,
                                YEAR_LEVEL TEXT,
                                COURSE_CODE TEXT
                            );"""
        conn = appFunctions1.createConnection(dbFolder)
        if conn is not None:
            appFunctions1.createTable(conn, createUserTable)
        else:
            print("Cannot Establish DB Connection")

    @staticmethod
    def getAllUsers1(dbFolder):
        conn = appFunctions1.createConnection(dbFolder)
        _getAllUsers = """SELECT * FROM Students1;"""
        try:
            c = conn.cursor()
            c.execute(_getAllUsers)
            return c.fetchall()  # fetch all rows
        except Error as e:
            print(e)

    import sqlite3
from sqlite3 import Error
from PySide6.QtWidgets import QTableWidgetItem, QComboBox

class appFunctions1():
    def __init__(self, arg):
        super(appFunctions1, self).__init__()
        self.arg = arg

    @staticmethod
    def createConnection(db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)
        return conn

    @staticmethod
    def createTable(conn, createTableSql):
        try:
            c = conn.cursor()
            c.execute(createTableSql)
        except Error as e:
            print(e)

    @staticmethod
    def main1(dbFolder):
        createUserTable = """CREATE TABLE IF NOT EXISTS Students1 (
                                ID TEXT PRIMARY KEY,
                                FULL_NAME TEXT,
                                GENDER TEXT,
                                YEAR_LEVEL TEXT,
                                COURSE_CODE TEXT
                            );"""
        conn = appFunctions1.createConnection(dbFolder)
        if conn is not None:
            appFunctions1.createTable(conn, createUserTable)
        else:
            print("Cannot Establish DB Connection")

    @staticmethod
    def getAllUsers1(dbFolder):
        conn = appFunctions1.createConnection(dbFolder)
        _getAllUsers = """SELECT * FROM Students1;"""
        try:
            c = conn.cursor()
            c.execute(_getAllUsers)
            return c.fetchall()  # fetch all rows
        except Error as e:
            print(e)

    def inputCourse1(self, dbFolder):
        conn = appFunctions1.createConnection(dbFolder)

        idNum = self.ui.idNum.text()
        fullName = self.ui.fullName.text()
        gender = self.ui.gender.currentText()
        yearLevel = self.ui.yearLevel.text()
        courseCode = self.ui.courseCode.currentText()

        insert_course_data_sql = "INSERT INTO Students1 (ID, FULL_NAME, GENDER, YEAR_LEVEL, COURSE_CODE) VALUES (?, ?, ?, ?, ?)"

        try:
            c = conn.cursor()

            # Check if the ID already exists
            select_id_sql = "SELECT * FROM Students1 WHERE ID = ?"
            c.execute(select_id_sql, (idNum,))
            existing_id = c.fetchone()

            if existing_id:
                print("ID already exists")
            else:
                # Insert the new course data
                c.execute(insert_course_data_sql, (idNum, fullName, gender, yearLevel, courseCode))
                conn.commit()
                print("Course inserted successfully")
                self.ui.idNum.setText("")
                self.ui.fullName.setText("")
                self.ui.yearLevel.setText("")
                appFunctions1.displayCourse1(self, appFunctions1.getAllUsers1(dbFolder))
        except Error as e:
            print(e)



    def displayCourse1(self, rows):
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(0)

        for row in rows:
            rowPos = self.ui.tableWidget_2.rowCount()
            self.ui.tableWidget.insertRow(rowPos)
            self.ui.tableWidget.setItem(rowPos, 0, QTableWidgetItem(row[0]))
            self.ui.tableWidget.setItem(rowPos, 1, QTableWidgetItem(row[1]))
            self.ui.tableWidget.setItem(rowPos, 2, QTableWidgetItem(row[2]))
            self.ui.tableWidget.setItem(rowPos, 3, QTableWidgetItem(row[3]))
            self.ui.tableWidget.setItem(rowPos, 4, QTableWidgetItem(row[4]))

        # Add gender options to the combo box
        gender_options = ["woman", "man", "transgender", "non-binary"]
        self.ui.gender.addItems(gender_options)


    def displayCourse1(self, rows):
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(0)

        for row in rows:
            rowPos = self.ui.tableWidget_2.rowCount()
            self.ui.tableWidget.insertRow(rowPos)
            self.ui.tableWidget.setItem(rowPos, 0, QTableWidgetItem(row[0]))
            self.ui.tableWidget.setItem(rowPos, 1, QTableWidgetItem(row[1]))
            self.ui.tableWidget.setItem(rowPos, 2, QTableWidgetItem(row[2]))
            self.ui.tableWidget.setItem(rowPos, 3, QTableWidgetItem(row[3]))
            self.ui.tableWidget.setItem(rowPos, 4, QTableWidgetItem(row[4]))

        # Add gender options to the combo box
        gender_options = ["woman", "man", "transgender", "non-binary"]
        self.ui.gender.addItems(gender_options)
