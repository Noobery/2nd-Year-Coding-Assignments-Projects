import os
import sqlite3
from sqlite3 import Error
from PySide6.QtWidgets import QTableWidgetItem, QTableWidget, QLineEdit, QDialog, QVBoxLayout, QMessageBox, QInputDialog
from PySide6.QtCore import Qt
class appFunctions():
    def __init__(self, arg):
        super(appFunctions, self).__init__()
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
    def main(dbFolder):
        createUserTable = """CREATE TABLE IF NOT EXISTS Course (
                                COURSE_CODE TEXT PRIMARY KEY,
                                COURSE TEXT
                            );"""
        createUserTable1 = """CREATE TABLE IF NOT EXISTS Students (
                                ID TEXT PRIMARY KEY,
                                FULL_NAME TEXT,
                                GENDER TEXT,
                                YEAR_LEVEL TEXT,
                                COURSE_CODE TEXT,
                                FOREIGN KEY (COURSE_CODE) REFERENCES Course(COURSE_CODE)
                            );"""
        conn = appFunctions.createConnection(dbFolder)
        if conn is not None:
            appFunctions.createTable(conn, createUserTable)
            appFunctions.createTable(conn, createUserTable1)
        else:
            print("Cannot Establish DB Connection")

    @staticmethod
    def getAllCourse(dbFolder):
        conn = appFunctions.createConnection(dbFolder)
        _getAllCourse = """SELECT * FROM Course;"""
        try:
            c = conn.cursor()
            c.execute(_getAllCourse)
            return c.fetchall()  # fetch all rows
        except Error as e:
            print(e)

    @staticmethod
    def getAllStudents(dbFolder):
        conn = appFunctions.createConnection(dbFolder)
        _getAllUsers = """SELECT * FROM Students;"""
        try:
            c = conn.cursor()
            c.execute(_getAllUsers)
            return c.fetchall()  # fetch all rows
        except Error as e:
            print(e)

    def inputCourse(self, dbFolder):
        conn = appFunctions.createConnection(dbFolder)

        course_Code = self.ui.course_Code.text()
        course = self.ui.course.text()
        

        # Check if any required field is empty
        if not course or not course_Code:
            QMessageBox.warning(self, "Missing Fields", "Please fill in all required fields.")
            return

        insert_course_data_sql = "INSERT INTO Course (COURSE_CODE, COURSE) VALUES (?, ?)"

        try:
            c = conn.cursor()

            # Check if the course code already exists
            select_course_sql = "SELECT * FROM Course WHERE COURSE_CODE = ?"
            c.execute(select_course_sql, (course_Code,))
            existing_course = c.fetchone()

            if existing_course:
                QMessageBox.warning(self, "Duplicate Course Code", "Course code already exists.")
            else:
                # Insert the new course data
                c.execute(insert_course_data_sql, (course_Code, course))
                conn.commit()
                QMessageBox.information(self, "Success", "Course inserted successfully.")
                self.ui.course_Code.setText("")
                self.ui.course.setText("")
                
                appFunctions.displayCourse(self, appFunctions.getAllCourse(dbFolder))
                appFunctions.displayCourse1(self, appFunctions.getAllCourse(dbFolder))
        except Error as e:
            print(e)

    

    def inputStudent(self, dbFolder):
        conn = appFunctions.createConnection(dbFolder)

        idNum = self.ui.idNum.text()
        fullName = self.ui.fullName.text()
        gender = self.ui.gender.currentText()
        yearLevel = self.ui.yearLevel.text()
        courseCode = self.ui.courseCode.currentText()

        # Check if any required field is empty
        if not idNum or not fullName or not yearLevel or not courseCode or not gender:
            QMessageBox.warning(self, "Missing Fields", "Please fill in all required fields.")
            return

        insert_students_data_sql = "INSERT INTO Students (ID, FULL_NAME, GENDER, YEAR_LEVEL, COURSE_CODE) VALUES (?, ?, ?, ?, ?)"

        try:
            c = conn.cursor()

            # Check if the ID already exists
            select_id_sql = "SELECT * FROM Students WHERE ID = ?"
            c.execute(select_id_sql, (idNum,))
            existing_id = c.fetchone()

            if existing_id:
                QMessageBox.warning(self, "Duplicate ID", "ID already exists.")
            else:
                # Insert the new course data
                c.execute(insert_students_data_sql, (idNum, fullName, gender, yearLevel, courseCode))
                conn.commit()
                QMessageBox.information(self, "Success", "Student info inserted successfully.")
                self.ui.idNum.setText("")
                self.ui.fullName.setText("")
                self.ui.yearLevel.setText("")
                appFunctions.displayStudents(self, appFunctions.getAllStudents(dbFolder))
                appFunctions.displayStudents1(self, appFunctions.getAllStudents(dbFolder))
        except Error as e:
            print(e)


    def displayCourse(self, rows):
        self.ui.tableWidget_2.clearContents()
        self.ui.tableWidget_2.setRowCount(0)

        for row in rows:
            rowPos = self.ui.tableWidget_2.rowCount()
            self.ui.tableWidget_2.insertRow(rowPos)
            self.ui.tableWidget_2.setItem(rowPos, 0, QTableWidgetItem(row[0]))
            self.ui.tableWidget_2.setItem(rowPos, 1, QTableWidgetItem(row[1]))
            
            # Set item flags to make cells non-editable
            for col in range(self.ui.tableWidget_2.columnCount()):
                item = self.ui.tableWidget_2.item(rowPos, col)
                if item:
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)

        # Update courseCode combo box with course codes
        course_codes = [row[0] for row in rows]  # Fetch COURSE_CODE data
        self.ui.courseCode.clear()
        self.ui.courseCode.addItems(course_codes)

    def displayStudents(self, rows):
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(0)

        for row in rows:
            rowPos = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(rowPos)
            self.ui.tableWidget.setItem(rowPos, 0, QTableWidgetItem(row[0]))
            self.ui.tableWidget.setItem(rowPos, 1, QTableWidgetItem(row[1]))
            self.ui.tableWidget.setItem(rowPos, 2, QTableWidgetItem(row[2]))
            self.ui.tableWidget.setItem(rowPos, 3, QTableWidgetItem(row[3]))
            self.ui.tableWidget.setItem(rowPos, 4, QTableWidgetItem(row[4]))
            
            # Set item flags to make cells non-editable
            for col in range(self.ui.tableWidget.columnCount()):
                item = self.ui.tableWidget.item(rowPos, col)
                if item:
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)

        # Add gender options to the combo box
        gender_options = ["Female", "Male", "Transgender", "Non-binary"]
        self.ui.gender.clear()  # Clear existing items in the combo box
        self.ui.gender.addItems(gender_options)
    
    def displayStudents1(self, rows):
        self.ui.tableWidget_3.clearContents()
        self.ui.tableWidget_3.setRowCount(0)

        for row in rows:
            rowPos = self.ui.tableWidget_3.rowCount()
            self.ui.tableWidget_3.insertRow(rowPos)
            self.ui.tableWidget_3.setItem(rowPos, 0, QTableWidgetItem(row[0]))
            self.ui.tableWidget_3.setItem(rowPos, 1, QTableWidgetItem(row[1]))
            self.ui.tableWidget_3.setItem(rowPos, 2, QTableWidgetItem(row[2]))
            self.ui.tableWidget_3.setItem(rowPos, 3, QTableWidgetItem(row[3]))
            self.ui.tableWidget_3.setItem(rowPos, 4, QTableWidgetItem(row[4]))
            
            # Set item flags to make cells non-editable
            for col in range(self.ui.tableWidget_3.columnCount()):
                item = self.ui.tableWidget_3.item(rowPos, col)
                if item:
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)

    def displayCourse1(self, rows):
        self.ui.tableWidget_4.clearContents()
        self.ui.tableWidget_4.setRowCount(0)

        for row in rows:
            rowPos = self.ui.tableWidget_4.rowCount()
            self.ui.tableWidget_4.insertRow(rowPos)
            self.ui.tableWidget_4.setItem(rowPos, 0, QTableWidgetItem(row[0]))
            self.ui.tableWidget_4.setItem(rowPos, 1, QTableWidgetItem(row[1]))
            
            # Set item flags to make cells non-editable
            for col in range(self.ui.tableWidget_4.columnCount()):
                item = self.ui.tableWidget_4.item(rowPos, col)
                if item:
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)

        # Update courseCode combo box with course codes
        course_codes = [row[0] for row in rows]  # Fetch COURSE_CODE data
        self.ui.courseCode.clear()
        self.ui.courseCode.addItems(course_codes)

    def searchData1(self, dbFolder):
        dialog = QDialog()
        layout = QVBoxLayout()
        search_input = QLineEdit()
        search_input.setPlaceholderText("Enter search keyword(s)")

        table_widget = QTableWidget()
        table_widget.setColumnCount(5)
        table_widget.setHorizontalHeaderLabels(["ID", "Full Name", "Gender", "Year Level", "Course Code"])

        def perform_search():
            search_terms = search_input.text().split()
            rows = appFunctions.searchStudents(dbFolder, search_terms)
            appFunctions.displaySearchResults1(table_widget, rows)

        search_input.textChanged.connect(perform_search)

        layout.addWidget(search_input)
        layout.addWidget(table_widget)
        dialog.setLayout(layout)
        dialog.exec_()

    @staticmethod
    def searchStudents(dbFolder, search_terms):
        conn = appFunctions.createConnection(dbFolder)
        _searchStudents = "SELECT * FROM Students WHERE ID LIKE ? OR FULL_NAME LIKE ? OR GENDER LIKE ? OR YEAR_LEVEL LIKE ? OR COURSE_CODE LIKE ?"
        try:
            c = conn.cursor()
            params = ['%{}%'.format(term) for term in search_terms]

            # Adjust the parameter binding based on the number of search terms
            if len(search_terms) == 0:
                c.execute(_searchStudents, ('%', '%', '%', '%', '%'))
            elif len(search_terms) == 1:
                c.execute(_searchStudents, (params[0], params[0], params[0], params[0], params[0]))
            elif len(search_terms) == 2:
                c.execute(_searchStudents, (params[0], params[1], params[0], params[1], params[1]))
            elif len(search_terms) == 3:
                c.execute(_searchStudents, (params[0], params[1], params[2], params[0], params[2]))
            elif len(search_terms) == 4:
                c.execute(_searchStudents, (params[0], params[1], params[2], params[3], params[3]))
            else:
                c.execute(_searchStudents, tuple(params + params[:5]))  # Use the first 5 search terms

            rows = c.fetchall()
            return rows
        except Error as e:
            print(e)

    @staticmethod
    def displaySearchResults(table_widget, rows):
        table_widget.clearContents()
        table_widget.setRowCount(0)

        if rows is None:
            return

        for row in rows:
            rowPos = table_widget.rowCount()
            table_widget.insertRow(rowPos)
            table_widget.setItem(rowPos, 0, QTableWidgetItem(row[0]))
            table_widget.setItem(rowPos, 1, QTableWidgetItem(row[1]))

    def searchData(self, dbFolder):
        dialog = QDialog()
        layout = QVBoxLayout()
        search_input = QLineEdit()
        search_input.setPlaceholderText("Enter search keyword(s)")

        table_widget = QTableWidget()
        table_widget.setColumnCount(2)
        table_widget.setHorizontalHeaderLabels(["COURSE CODE", "COURSE"])

        def perform_search():
            search_terms = search_input.text().split()
            rows = appFunctions.searchCourses(dbFolder, search_terms)
            appFunctions.displaySearchResults(table_widget, rows)

        search_input.textChanged.connect(perform_search)

        layout.addWidget(search_input)
        layout.addWidget(table_widget)
        dialog.setLayout(layout)
        dialog.exec_()

    @staticmethod
    def searchCourses(dbFolder, search_terms):
        conn = appFunctions.createConnection(dbFolder)
        _searchCourses = "SELECT * FROM Course WHERE COURSE_CODE LIKE ? OR COURSE LIKE ?"
        try:
            c = conn.cursor()
            params = ['%{}%'.format(term) for term in search_terms]

            # Adjust the parameter binding based on the number of search terms
            if len(search_terms) == 0:
                c.execute(_searchCourses, ('%', '%'))
            elif len(search_terms) == 1:
                c.execute(_searchCourses, (params[0], params[0]))
            elif len(search_terms) == 2:
                c.execute(_searchCourses, tuple(params))
            else:
                c.execute(_searchCourses, tuple(params[:2]))  # Use the first 2 search terms

            rows = c.fetchall()
            return rows
        except Error as e:
            print(e)

    @staticmethod
    def displaySearchResults(table_widget, rows):
        table_widget.clearContents()
        table_widget.setRowCount(0)

        if rows is None:
            return

        for row in rows:
            rowPos = table_widget.rowCount()
            table_widget.insertRow(rowPos)
            table_widget.setItem(rowPos, 0, QTableWidgetItem(row[0]))
            table_widget.setItem(rowPos, 1, QTableWidgetItem(row[1]))
    
    def displaySearchResults1(table_widget, rows):
        table_widget.clearContents()
        table_widget.setRowCount(0)

        if rows is None:
            return

        for row in rows:
            rowPos = table_widget.rowCount()
            table_widget.insertRow(rowPos)
            table_widget.setItem(rowPos, 0, QTableWidgetItem(row[0]))
            table_widget.setItem(rowPos, 1, QTableWidgetItem(row[1]))
            table_widget.setItem(rowPos, 2, QTableWidgetItem(row[2]))
            table_widget.setItem(rowPos, 3, QTableWidgetItem(row[3]))
            table_widget.setItem(rowPos, 4, QTableWidgetItem(row[4]))

    def deleteStudent(self):
        # Get the student ID from the line edit widget
        student_id = self.ui.idNum_3.text()
        
        print("Student ID:", student_id)
        # Specify the path to the database folder
        dbFolder = "Database/ssis_v2.db"
        
        conn = appFunctions.createConnection(dbFolder)

        delete_student_sql = "DELETE FROM Students WHERE ID = ?"

        try:
            c = conn.cursor()

            # Check if the student ID exists
            select_id_sql = "SELECT * FROM Students WHERE ID = ?"
            c.execute(select_id_sql, (student_id,))
            existing_id = c.fetchone()

            if existing_id:
                # Delete the student data
                c.execute(delete_student_sql, (student_id,))
                conn.commit()
                QMessageBox.information(None, "Success", "Student data deleted successfully.")
                appFunctions.displayStudents(self, appFunctions.getAllStudents(dbFolder))
                appFunctions.displayStudents1(self, appFunctions.getAllStudents(dbFolder))
            else:
                QMessageBox.warning(None, "Invalid ID", "Student ID does not exist.")
        except Error as e:
            print(e)

    def deleteCourse(self):
        # Get the course code from the line edit widget
        course_code = self.ui.courseCodeLine.text()

        # Print the course code for debugging
        print("Course Code:", course_code)

        # Specify the path to the database folder
        dbFolder = "Database/ssis_v2.db"

        conn = appFunctions.createConnection(dbFolder)

        delete_course_sql = "DELETE FROM Course WHERE COURSE = ?"
        delete_student_sql = "DELETE FROM Students WHERE COURSE_CODE = ?"

        try:
            c = conn.cursor()

            # Check if the course exists
            select_course_sql = "SELECT * FROM Course WHERE COURSE = ?"
            c.execute(select_course_sql, (course_code,))
            existing_course = c.fetchone()

            if existing_course:
                # Delete the student data for the course
                c.execute(delete_student_sql, (course_code,))
                conn.commit()

                # Delete the course data
                c.execute(delete_course_sql, (course_code,))
                conn.commit()

                QMessageBox.information(None, "Success", "Course and associated student data deleted successfully.")
                appFunctions.displayCourse(self, appFunctions.getAllCourse(dbFolder))
                appFunctions.displayStudents(self, appFunctions.getAllStudents(dbFolder))
                appFunctions.displayStudents1(self, appFunctions.getAllStudents(dbFolder))
                appFunctions.displayCourse1(self, appFunctions.getAllCourse(dbFolder))
            else:
                QMessageBox.warning(None, "Invalid Course Code", "Course Code does not exist.")
        except Error as e:
            print(e)
    
    def whenClickedCode(self):
        selected_indexes = self.ui.tableWidget_4.selectedIndexes()
        
        if selected_indexes:
            selected_index = selected_indexes[0]
            row = selected_index.row()
            column = selected_index.column()
            
            # Retrieve the data from the selected cell
            item = self.ui.tableWidget_4.item(row, column)
            if item:
                value = item.text()
                # Set the value to the courseCodeLine line edit
                self.ui.courseCodeLine.setText(value)

    def whenClickedId(self):
        selected_indexes = self.ui.tableWidget_3.selectedIndexes()
        
        if selected_indexes:
            selected_index = selected_indexes[0]
            row = selected_index.row()
            column = selected_index.column()
            
            # Retrieve the data from the selected cell
            item = self.ui.tableWidget_3.item(row, column)
            if item:
                value = item.text()
                # Set the value to the courseCodeLine line edit
                self.ui.idNum_3.setText(value)
 
    def updateStudent(self):
        # Prompt the user to enter the ID number of the student to edit
        id_number, ok = QInputDialog.getText(self, "Update Student", "Enter ID Number:")
        
        if ok:
            # Check if the ID number exists in the database
            dbFolder = "Database/ssis_v2.db"
            conn = appFunctions.createConnection(dbFolder)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Students WHERE ID=?", (id_number,))
            student = cursor.fetchone()
            
            if student:
                # The ID number exists, transfer the student information to the corresponding fields
                self.ui.idNum_2.setText(student[0])
                self.ui.idNum_2.setReadOnly(True)  # Disable editing
                
                self.ui.fullName_2.setText(student[1])
                
                gender_options = ["Female", "Male", "Transgender", "Non-binary"]
                self.ui.gender_2.clear()  # Clear existing items in the combo box
                self.ui.gender_2.addItems(gender_options)
                
                # Set the selected gender in the combo box
                gender_index = self.ui.gender_2.findText(student[2])
                if gender_index != -1:
                    self.ui.gender_2.setCurrentIndex(gender_index)
                
                self.ui.yearLevel_2.setText(student[3])
                
                # Get the course codes from the Course table
                course_codes = appFunctions.getAllCourse(dbFolder)
                
                # Clear existing items in the course code combo box
                self.ui.courseCode_2.clear()
                
                for code in course_codes:
                    self.ui.courseCode_2.addItem(code[1])  # Use COURSE_CODE instead of COURSE
                
                # Set the selected course code in the combo box
                course_code_index = self.ui.courseCode_2.findText(student[4])
                if course_code_index != -1:
                    self.ui.courseCode_2.setCurrentIndex(course_code_index)
                
                # Update the student information when the Update Student button is clicked
                
                QMessageBox.information(self, "Success", "Student information loaded successfully.")
            else:
                QMessageBox.warning(self, "Error", "Student with ID Number {} not found.".format(id_number))

    def updateStudentData(self):
        # Retrieve the updated student information from the line edits and combo boxes
        id_number = self.ui.idNum_2.text()
        full_name = self.ui.fullName_2.text()
        gender = self.ui.gender_2.currentText()
        year_level = self.ui.yearLevel_2.text()
        course_code = self.ui.courseCode_2.currentText()
        
        # Update the student information in the database
        dbFolder = "Database/ssis_v2.db"
        conn = appFunctions.createConnection(dbFolder)
        cursor = conn.cursor()
        cursor.execute("UPDATE Students SET FULL_NAME=?, GENDER=?, YEAR_LEVEL=?, COURSE_CODE=? WHERE ID=?",
                    (full_name, gender, year_level, course_code, id_number))
        conn.commit()
        
        QMessageBox.information(self, "Success", "Student information updated successfully.")

        appFunctions.displayStudents(self, appFunctions.getAllStudents(dbFolder))
        appFunctions.displayStudents1(self, appFunctions.getAllStudents(dbFolder))


    def updateCourses(self):
        # Prompt the user to enter the course code of the course to edit
        course_code, ok = QInputDialog.getText(self, "Update Course", "Enter Course Code:")
        
        if ok:
            # Check if the course code exists in the database
            dbFolder = "Database/ssis_v2.db"
            conn = appFunctions.createConnection(dbFolder)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Course WHERE COURSE=?", (course_code,))
            course = cursor.fetchone()
            
            if course:
                # The course code exists, transfer the course information to the corresponding fields
                self.ui.course_Code_2.setText(course[1])
                self.ui.course_Code_2.setReadOnly(True)  # Disable editing
                
                self.ui.course_2.setText(course[0])
                
                # Get the course codes from the Courses table
                course_codes = appFunctions.getAllCourse(dbFolder)
                
                # Clear existing items in the course code combo box
                
                
                # Update the course information when the Edit Course button is clicked
                
                QMessageBox.information(self, "Success", "Course information loaded successfully.")
            else:
                QMessageBox.warning(self, "Error", "Course with Course Code {} not found.".format(course_code))
    
    def updateCourseData(self):
        # Retrieve the updated student information from the line edits and combo boxes
        course = self.ui.course_2.text()
        course_code = self.ui.course_Code_2.text()
        
        # Update the student information in the database
        dbFolder = "Database/ssis_v2.db"
        conn = appFunctions.createConnection(dbFolder)
        cursor = conn.cursor()
        cursor.execute("UPDATE Course SET COURSE_CODE =? WHERE COURSE = ?",
                    (course, course_code))
        conn.commit()
        
        QMessageBox.information(self, "Success", "Student information updated successfully.")

        appFunctions.displayCourse(self, appFunctions.getAllCourse(dbFolder))
        appFunctions.displayCourse1(self, appFunctions.getAllCourse(dbFolder))
    




