import os
os.environ['ICONIFY_QTLIB'] = 'PySide6'


import sys

from ui_SSIS import *

from Custom_Widgets.Widgets import *

settings = QSettings()

from Functions import appFunctions



class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

       
        loadJsonStyle(self, self.ui) 

        
        self.show() 

        dbFolder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Database/ssis_v2.db'))
        appFunctions.main (dbFolder)

        appFunctions.displayCourse(self, appFunctions.getAllCourse(dbFolder))

        appFunctions.displayCourse1(self, appFunctions.getAllCourse(dbFolder))

        self.ui.inputCourse.clicked.connect(lambda: appFunctions.inputCourse(self, dbFolder))

        appFunctions.displayStudents(self, appFunctions.getAllStudents(dbFolder))

        appFunctions.displayStudents1(self, appFunctions.getAllStudents(dbFolder))

        self.ui.addInfo.clicked.connect(lambda: appFunctions.inputStudent(self, dbFolder))

        self.ui.csearchBtn.clicked.connect(lambda: appFunctions.searchData(self, dbFolder))
        
        self.ui.ssearchBtn.clicked.connect(lambda: appFunctions.searchData1(self, dbFolder))
        
        self.ui.deleteStudentButton.clicked.connect(lambda: appFunctions.deleteStudent(self))

        self.ui.deleteCourseButton.clicked.connect(lambda: appFunctions.deleteCourse(self))

        self.ui.tableWidget_4.itemSelectionChanged.connect(lambda: appFunctions.whenClickedCode(self))

        self.ui.tableWidget_3.itemSelectionChanged.connect(lambda: appFunctions.whenClickedId(self))

        self.ui.editStudentButton.clicked.connect(lambda: appFunctions.updateStudent(self))

        self.ui.updateStudentButton.clicked.connect(lambda: appFunctions.updateStudentData(self))

        self.ui.editCourseButton.clicked.connect(lambda: appFunctions.updateCourses(self))

        self.ui.updateCourseButton.clicked.connect(lambda: appFunctions.updateCourseData(self))

     

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
