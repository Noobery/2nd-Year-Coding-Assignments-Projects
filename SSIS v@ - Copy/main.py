import os
os.environ['ICONIFY_QTLIB'] = 'PySide6'


import sys
########################################################################
# IMPORT GUI FILE
from ui_SSIS import *
########################################################################

########################################################################
# IMPORT Custom widgets
from Custom_Widgets.Widgets import *
# INITIALIZE APP SETTINGS
settings = QSettings()
########################################################################

from Functions import appFunctions

#from CourseFunctions import appFunctions1

########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        #Use this if you only have one json file named "style.json" inside the root directory, "json" directory or "jsonstyles" folder.
        loadJsonStyle(self, self.ui) 

        # Use this to specify your json file(s) path/name
        # loadJsonStyle(self, self.ui, jsonFiles = {
        #     "mystyle.json", "style.json"
        #     }) 

        ########################################################################

        #######################################################################
        # SHOW WINDOW
        #####set ICONIFY_QTLIB=PySide6##################################################################
        self.show() 

        dbFolder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Database/ssis_v2.db'))
        appFunctions.main (dbFolder)

        appFunctions.displayCourse(self, appFunctions.getAllUsers(dbFolder))

        appFunctions.displayCourse3(self, appFunctions.getAllUsers(dbFolder))

        self.ui.inputCourse.clicked.connect(lambda: appFunctions.inputCourse(self, dbFolder))

        appFunctions.displayCourse1(self, appFunctions.getAllUsers1(dbFolder))

        appFunctions.displayCourse2(self, appFunctions.getAllUsers1(dbFolder))

        self.ui.addInfo.clicked.connect(lambda: appFunctions.inputCourse1(self, dbFolder))

        self.ui.csearchBtn.clicked.connect(lambda: appFunctions.searchData(self, dbFolder))
        
        self.ui.ssearchBtn.clicked.connect(lambda: appFunctions.searchData1(self, dbFolder))
        
        self.ui.deleteStudentButton.clicked.connect(lambda: appFunctions.deleteStudent(self))

        self.ui.deleteCourseButton.clicked.connect(lambda: appFunctions.deleteCourse(self))

        self.ui.tableWidget_4.itemSelectionChanged.connect(lambda: appFunctions.whenClickedCode(self))

        self.ui.tableWidget_3.itemSelectionChanged.connect(lambda: appFunctions.whenClickedId(self))

      
      

        



     
    

        

########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ########################################################################
    ## 
    ########################################################################
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  