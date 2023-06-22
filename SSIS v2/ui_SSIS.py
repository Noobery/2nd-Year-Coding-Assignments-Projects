# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SSIS_BACKUP_UIEfkJZV.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

from Custom_Widgets.Widgets import (QCustomSlideMenu, QCustomStackedWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(830, 583)
        MainWindow.setStyleSheet(u"*{	\n"
"	border none;\n"
"	background-color: transparent;\n"
"	padding 0;\n"
"	margin 0;\n"
"	color: #fff;\n"
"}\n"
"#mainMenu1, QLineEdit{\n"
"	background-color: #1b1b27\n"
"}\n"
"#centralwidget{\n"
"	background-color: #1b1b27\n"
"}\n"
"#addStudent{\n"
"	background-color: #1b1b27\n"
"}\n"
"\n"
"\n"
"#Header, #mainBody {\n"
"	background-color: #112D4E\n"
"}\n"
"\n"
"QPushButton{\n"
"	text-align:left;\n"
"	padding: 5px 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"\n"
"}\n"
"\n"
"#addStudent{\n"
"	border-left: 3px solid #F9F7F7\n"
"}\n"
"\n"
"QLineEdit{\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QComboBox {\n"
"	background-color: #1b1b27\n"
"}\n"
"\n"
"#addInfo {\n"
"	background-color: #3F72AF;\n"
"	border-radius: 10px\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"	background-color: #112D4E\n"
"}\n"
"\n"
"#tableWidget {\n"
"	background-color: #112D4E\n"
"}\n"
"\n"
"#inputCourse {\n"
"	background-color: #3F72AF;\n"
"	border-radius: 10px\n"
"}\n"
"#tableWidget"
                        "_2 {\n"
"	background-color: #112D4E\n"
"}\n"
"\n"
"#tableWidget_3 {\n"
"	background-color: #112D4E\n"
"}\n"
"\n"
"#tableWidget_4 {\n"
"	background-color: #112D4E\n"
"}\n"
"\n"
"#deleteStudentButton{\n"
"	background-color: #C70000;\n"
"	border-radius: 10px\n"
"}\n"
"\n"
"#deleteCourseButton{\n"
"	background-color: #C70000;\n"
"	border-radius: 10px\n"
"}\n"
"\n"
"#updateCourseButton{\n"
"	background-color: #3F72AF;\n"
"	border-radius: 10px\n"
"}\n"
"\n"
"#updateStudentButton{\n"
"	background-color: #3F72AF;\n"
"	border-radius: 10px\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Header = QWidget(self.centralwidget)
        self.Header.setObjectName(u"Header")
        self.horizontalLayout = QHBoxLayout(self.Header)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.Header)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.menuButton = QPushButton(self.frame_2)
        self.menuButton.setObjectName(u"menuButton")
        self.menuButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"../SSIS v@/Resource/whiteMenu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menuButton.setIcon(icon)
        self.menuButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.menuButton, 0, Qt.AlignLeft)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout_4.addWidget(self.label)


        self.horizontalLayout.addWidget(self.frame_2, 0, Qt.AlignLeft)

        self.frame = QFrame(self.Header)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.horizontalLayout.addWidget(self.frame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.Header)

        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBody.sizePolicy().hasHeightForWidth())
        self.mainBody.setSizePolicy(sizePolicy)
        self.mainBody.setMinimumSize(QSize(825, 496))
        self.horizontalLayout_2 = QHBoxLayout(self.mainBody)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 9, 9, 9)
        self.leftMenu = QCustomSlideMenu(self.mainBody)
        self.leftMenu.setObjectName(u"leftMenu")
        self.leftMenu.setMinimumSize(QSize(200, 0))
        self.leftMenu.setMaximumSize(QSize(0, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.leftMenu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 20)
        self.widget = QWidget(self.leftMenu)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(200, 458))
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 0, 0, 0)
        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 0, 0, 9)
        self.addStudent = QPushButton(self.frame_3)
        self.addStudent.setObjectName(u"addStudent")
        font1 = QFont()
        font1.setBold(False)
        self.addStudent.setFont(font1)
        self.addStudent.setCursor(QCursor(Qt.PointingHandCursor))
        self.addStudent.setIconSize(QSize(16, 16))

        self.verticalLayout_5.addWidget(self.addStudent)

        self.addCourse = QPushButton(self.frame_3)
        self.addCourse.setObjectName(u"addCourse")

        self.verticalLayout_5.addWidget(self.addCourse)

        self.deleteStudentBtn = QPushButton(self.frame_3)
        self.deleteStudentBtn.setObjectName(u"deleteStudentBtn")
        self.deleteStudentBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.deleteStudentBtn)

        self.deleteCourseBtn = QPushButton(self.frame_3)
        self.deleteCourseBtn.setObjectName(u"deleteCourseBtn")
        self.deleteCourseBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.deleteCourseBtn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.verticalLayout_4.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.widget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, -1, -1, 15)
        self.aboutButton = QPushButton(self.frame_4)
        self.aboutButton.setObjectName(u"aboutButton")
        self.aboutButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_6.addWidget(self.aboutButton)


        self.verticalLayout_4.addWidget(self.frame_4)


        self.verticalLayout_3.addWidget(self.widget)


        self.horizontalLayout_2.addWidget(self.leftMenu)

        self.mainMenu1 = QWidget(self.mainBody)
        self.mainMenu1.setObjectName(u"mainMenu1")
        self.mainMenu1.setEnabled(True)
        sizePolicy.setHeightForWidth(self.mainMenu1.sizePolicy().hasHeightForWidth())
        self.mainMenu1.setSizePolicy(sizePolicy)
        self.mainMenu1.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.mainMenu1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 9, 6, 0)
        self.mainPages = QCustomStackedWidget(self.mainMenu1)
        self.mainPages.setObjectName(u"mainPages")
        self.AstudentPage = QWidget()
        self.AstudentPage.setObjectName(u"AstudentPage")
        self.verticalLayout_10 = QVBoxLayout(self.AstudentPage)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_3 = QWidget(self.AstudentPage)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_11 = QVBoxLayout(self.widget_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_6 = QFrame(self.widget_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.label_3 = QLabel(self.frame_8)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.label_3.setFont(font2)

        self.horizontalLayout_8.addWidget(self.label_3, 0, Qt.AlignLeft)

        self.ssearchBtn = QPushButton(self.frame_8)
        self.ssearchBtn.setObjectName(u"ssearchBtn")
        self.ssearchBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u"../SSIS v@/Resource/whiteSearch.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ssearchBtn.setIcon(icon1)
        self.ssearchBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.ssearchBtn, 0, Qt.AlignLeft)


        self.horizontalLayout_5.addWidget(self.frame_8, 0, Qt.AlignLeft)

        self.showAdd = QPushButton(self.frame_6)
        self.showAdd.setObjectName(u"showAdd")
        font3 = QFont()
        font3.setBold(True)
        self.showAdd.setFont(font3)
        self.showAdd.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"../SSIS v@/Resource/addUser.png", QSize(), QIcon.Normal, QIcon.Off)
        self.showAdd.setIcon(icon2)
        self.showAdd.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.showAdd, 0, Qt.AlignRight)


        self.verticalLayout_11.addWidget(self.frame_6)

        self.tableWidget = QTableWidget(self.widget_3)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setBackground(QColor(0, 0, 0));
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_11.addWidget(self.tableWidget)


        self.verticalLayout_10.addWidget(self.widget_3)

        self.mainPages.addWidget(self.AstudentPage)
        self.deleteCoursePage = QWidget()
        self.deleteCoursePage.setObjectName(u"deleteCoursePage")
        self.verticalLayout_15 = QVBoxLayout(self.deleteCoursePage)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.widget_5 = QWidget(self.deleteCoursePage)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_14 = QVBoxLayout(self.widget_5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_10 = QFrame(self.widget_5)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_15 = QFrame(self.frame_10)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_15)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.horizontalLayout_11.addWidget(self.label_8)

        self.editCourseButton = QPushButton(self.frame_15)
        self.editCourseButton.setObjectName(u"editCourseButton")
        self.editCourseButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u"../SSIS v@/Resource/whiteEdit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.editCourseButton.setIcon(icon3)
        self.editCourseButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_11.addWidget(self.editCourseButton, 0, Qt.AlignLeft)


        self.horizontalLayout_10.addWidget(self.frame_15, 0, Qt.AlignLeft)

        self.deleteCourseBTN = QPushButton(self.frame_10)
        self.deleteCourseBTN.setObjectName(u"deleteCourseBTN")
        self.deleteCourseBTN.setFont(font3)
        self.deleteCourseBTN.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u"../SSIS v@/Resource/whiteDelete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteCourseBTN.setIcon(icon4)
        self.deleteCourseBTN.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.deleteCourseBTN, 0, Qt.AlignRight)


        self.verticalLayout_14.addWidget(self.frame_10)

        self.tableWidget_4 = QTableWidget(self.widget_5)
        if (self.tableWidget_4.columnCount() < 2):
            self.tableWidget_4.setColumnCount(2)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        self.tableWidget_4.setObjectName(u"tableWidget_4")

        self.verticalLayout_14.addWidget(self.tableWidget_4)


        self.verticalLayout_15.addWidget(self.widget_5)

        self.mainPages.addWidget(self.deleteCoursePage)
        self.deleteStudentPage = QWidget()
        self.deleteStudentPage.setObjectName(u"deleteStudentPage")
        self.verticalLayout_12 = QVBoxLayout(self.deleteStudentPage)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.widget_4 = QWidget(self.deleteStudentPage)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_13 = QVBoxLayout(self.widget_4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_9 = QFrame(self.widget_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_16 = QFrame(self.frame_9)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_16)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.horizontalLayout_12.addWidget(self.label_5)

        self.editStudentButton = QPushButton(self.frame_16)
        self.editStudentButton.setObjectName(u"editStudentButton")
        self.editStudentButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.editStudentButton.setIcon(icon3)
        self.editStudentButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_12.addWidget(self.editStudentButton, 0, Qt.AlignLeft)


        self.horizontalLayout_9.addWidget(self.frame_16, 0, Qt.AlignLeft)

        self.deleteButton = QPushButton(self.frame_9)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setFont(font3)
        self.deleteButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteButton.setIcon(icon4)
        self.deleteButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_9.addWidget(self.deleteButton, 0, Qt.AlignRight)


        self.verticalLayout_13.addWidget(self.frame_9)

        self.tableWidget_3 = QTableWidget(self.widget_4)
        if (self.tableWidget_3.columnCount() < 5):
            self.tableWidget_3.setColumnCount(5)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setBackground(QColor(0, 0, 0));
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        self.tableWidget_3.setObjectName(u"tableWidget_3")

        self.verticalLayout_13.addWidget(self.tableWidget_3)


        self.verticalLayout_12.addWidget(self.widget_4)

        self.mainPages.addWidget(self.deleteStudentPage)
        self.coursePage = QWidget()
        self.coursePage.setObjectName(u"coursePage")
        self.coursePage.setCursor(QCursor(Qt.PointingHandCursor))
        self.verticalLayout_25 = QVBoxLayout(self.coursePage)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.widget_7 = QWidget(self.coursePage)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_26 = QVBoxLayout(self.widget_7)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.frame_12 = QFrame(self.widget_7)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.frame_7 = QFrame(self.frame_12)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_7)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)

        self.horizontalLayout_7.addWidget(self.label_6)

        self.csearchBtn = QPushButton(self.frame_7)
        self.csearchBtn.setObjectName(u"csearchBtn")
        self.csearchBtn.setIcon(icon1)
        self.csearchBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_7.addWidget(self.csearchBtn, 0, Qt.AlignLeft)


        self.horizontalLayout_6.addWidget(self.frame_7, 0, Qt.AlignLeft)

        self.addCourseButton = QPushButton(self.frame_12)
        self.addCourseButton.setObjectName(u"addCourseButton")
        self.addCourseButton.setFont(font3)
        icon5 = QIcon()
        icon5.addFile(u"../SSIS v@/Resource/course.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addCourseButton.setIcon(icon5)
        self.addCourseButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.addCourseButton, 0, Qt.AlignRight)


        self.verticalLayout_26.addWidget(self.frame_12)

        self.tableWidget_2 = QTableWidget(self.widget_7)
        if (self.tableWidget_2.columnCount() < 2):
            self.tableWidget_2.setColumnCount(2)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.verticalLayout_26.addWidget(self.tableWidget_2)


        self.verticalLayout_25.addWidget(self.widget_7)

        self.mainPages.addWidget(self.coursePage)
        self.aboutPage = QWidget()
        self.aboutPage.setObjectName(u"aboutPage")
        self.label_7 = QLabel(self.aboutPage)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(330, 180, 121, 61))
        self.label_7.setFont(font2)
        self.mainPages.addWidget(self.aboutPage)

        self.verticalLayout_2.addWidget(self.mainPages)


        self.horizontalLayout_2.addWidget(self.mainMenu1)

        self.rightMenu = QCustomSlideMenu(self.mainBody)
        self.rightMenu.setObjectName(u"rightMenu")
        self.rightMenu.setMinimumSize(QSize(0, 0))
        self.rightMenu.setMaximumSize(QSize(0, 16777215))
        self.verticalLayout_7 = QVBoxLayout(self.rightMenu)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, -1, 0, -1)
        self.iconCloseStudent = QPushButton(self.rightMenu)
        self.iconCloseStudent.setObjectName(u"iconCloseStudent")
        icon6 = QIcon()
        icon6.addFile(u"../SSIS v@/Resource/closeIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.iconCloseStudent.setIcon(icon6)
        self.iconCloseStudent.setIconSize(QSize(24, 24))

        self.verticalLayout_7.addWidget(self.iconCloseStudent, 0, Qt.AlignRight)

        self.widget_2 = QWidget(self.rightMenu)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(200, 312))
        self.verticalLayout_8 = QVBoxLayout(self.widget_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(70, 70))
        self.label_2.setMaximumSize(QSize(70, 70))
        self.label_2.setPixmap(QPixmap(u"../SSIS v@/Resource/addUser.png"))
        self.label_2.setScaledContents(True)

        self.verticalLayout_8.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.frame_5 = QFrame(self.widget_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.idNum = QLineEdit(self.frame_5)
        self.idNum.setObjectName(u"idNum")
        self.idNum.setStyleSheet(u"QLineEdit {\n"
"	background-color: #1b1b27;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_9.addWidget(self.idNum)

        self.fullName = QLineEdit(self.frame_5)
        self.fullName.setObjectName(u"fullName")
        font4 = QFont()
        font4.setKerning(True)
        self.fullName.setFont(font4)
        self.fullName.setStyleSheet(u"QLineEdit {\n"
"	background-color: #1b1b27;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_9.addWidget(self.fullName)

        self.gender = QComboBox(self.frame_5)
        self.gender.setObjectName(u"gender")
        self.gender.setStyleSheet(u"QComboBox {\n"
"	background-color: #1b1b27;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_9.addWidget(self.gender)

        self.yearLevel = QLineEdit(self.frame_5)
        self.yearLevel.setObjectName(u"yearLevel")
        font5 = QFont()
        font5.setKerning(False)
        self.yearLevel.setFont(font5)
        self.yearLevel.setStyleSheet(u"QLineEdit {\n"
"	background-color: #1b1b27;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_9.addWidget(self.yearLevel)

        self.courseCode = QComboBox(self.frame_5)
        self.courseCode.setObjectName(u"courseCode")
        self.courseCode.setStyleSheet(u"QComboBox {\n"
"	background-color: #1b1b27;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_9.addWidget(self.courseCode)


        self.verticalLayout_8.addWidget(self.frame_5)

        self.addInfo = QPushButton(self.widget_2)
        self.addInfo.setObjectName(u"addInfo")
        font6 = QFont()
        font6.setPointSize(10)
        font6.setBold(True)
        font6.setStrikeOut(False)
        self.addInfo.setFont(font6)
        self.addInfo.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_8.addWidget(self.addInfo, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addWidget(self.widget_2, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.rightMenu)

        self.rightMenu_2 = QCustomSlideMenu(self.mainBody)
        self.rightMenu_2.setObjectName(u"rightMenu_2")
        self.rightMenu_2.setMinimumSize(QSize(0, 0))
        self.rightMenu_2.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_36 = QVBoxLayout(self.rightMenu_2)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(-1, -1, 0, -1)
        self.iconCloseCourse = QPushButton(self.rightMenu_2)
        self.iconCloseCourse.setObjectName(u"iconCloseCourse")
        self.iconCloseCourse.setIcon(icon6)
        self.iconCloseCourse.setIconSize(QSize(24, 24))

        self.verticalLayout_36.addWidget(self.iconCloseCourse, 0, Qt.AlignRight)

        self.widget_6 = QWidget(self.rightMenu_2)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(200, 312))
        self.verticalLayout_37 = QVBoxLayout(self.widget_6)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.label_12 = QLabel(self.widget_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(70, 70))
        self.label_12.setMaximumSize(QSize(70, 70))
        self.label_12.setPixmap(QPixmap(u"../SSIS v@/Resource/course.png"))
        self.label_12.setScaledContents(True)

        self.verticalLayout_37.addWidget(self.label_12, 0, Qt.AlignHCenter)

        self.frame_11 = QFrame(self.widget_6)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_11)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.course = QLineEdit(self.frame_11)
        self.course.setObjectName(u"course")
        self.course.setStyleSheet(u"QLineEdit {\n"
"	background-color: #1b1b27;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_38.addWidget(self.course)

        self.course_Code = QLineEdit(self.frame_11)
        self.course_Code.setObjectName(u"course_Code")
        self.course_Code.setFont(font4)
        self.course_Code.setStyleSheet(u"QLineEdit {\n"
"	background-color: #1b1b27;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_38.addWidget(self.course_Code)


        self.verticalLayout_37.addWidget(self.frame_11)

        self.inputCourse = QPushButton(self.widget_6)
        self.inputCourse.setObjectName(u"inputCourse")
        self.inputCourse.setFont(font6)
        self.inputCourse.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_37.addWidget(self.inputCourse, 0, Qt.AlignHCenter)


        self.verticalLayout_36.addWidget(self.widget_6, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.rightMenu_2)

        self.rightMenu_6 = QCustomSlideMenu(self.mainBody)
        self.rightMenu_6.setObjectName(u"rightMenu_6")
        self.rightMenu_6.setMinimumSize(QSize(0, 0))
        self.rightMenu_6.setMaximumSize(QSize(0, 16777215))
        self.verticalLayout_30 = QVBoxLayout(self.rightMenu_6)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(-1, -1, 0, -1)
        self.iconCloseModCourse = QPushButton(self.rightMenu_6)
        self.iconCloseModCourse.setObjectName(u"iconCloseModCourse")
        self.iconCloseModCourse.setIcon(icon6)
        self.iconCloseModCourse.setIconSize(QSize(24, 24))

        self.verticalLayout_30.addWidget(self.iconCloseModCourse, 0, Qt.AlignRight)

        self.widget_11 = QWidget(self.rightMenu_6)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMinimumSize(QSize(200, 312))
        self.verticalLayout_31 = QVBoxLayout(self.widget_11)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_13 = QLabel(self.widget_11)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(70, 70))
        self.label_13.setMaximumSize(QSize(70, 70))
        self.label_13.setPixmap(QPixmap(u"../SSIS v@/Resource/course.png"))
        self.label_13.setScaledContents(True)

        self.verticalLayout_31.addWidget(self.label_13, 0, Qt.AlignHCenter)

        self.frame_18 = QFrame(self.widget_11)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_18)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.course_2 = QLineEdit(self.frame_18)
        self.course_2.setObjectName(u"course_2")
        self.course_2.setStyleSheet(u"QLineEdit {\n"
"	background-color: #1b1b27;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_32.addWidget(self.course_2)

        self.course_Code_2 = QLineEdit(self.frame_18)
        self.course_Code_2.setObjectName(u"course_Code_2")
        self.course_Code_2.setFont(font4)
        self.course_Code_2.setStyleSheet(u"QLineEdit {\n"
"	background-color: #1b1b27;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_32.addWidget(self.course_Code_2)


        self.verticalLayout_31.addWidget(self.frame_18)

        self.updateCourseButton = QPushButton(self.widget_11)
        self.updateCourseButton.setObjectName(u"updateCourseButton")
        self.updateCourseButton.setFont(font6)
        self.updateCourseButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_31.addWidget(self.updateCourseButton, 0, Qt.AlignHCenter)


        self.verticalLayout_30.addWidget(self.widget_11, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.rightMenu_6)

        self.rightMenu_5 = QCustomSlideMenu(self.mainBody)
        self.rightMenu_5.setObjectName(u"rightMenu_5")
        self.rightMenu_5.setMinimumSize(QSize(0, 0))
        self.rightMenu_5.setMaximumSize(QSize(0, 16777215))
        self.verticalLayout_16 = QVBoxLayout(self.rightMenu_5)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(-1, -1, 0, -1)
        self.iconCloseModStudent = QPushButton(self.rightMenu_5)
        self.iconCloseModStudent.setObjectName(u"iconCloseModStudent")
        self.iconCloseModStudent.setIcon(icon6)
        self.iconCloseModStudent.setIconSize(QSize(24, 24))

        self.verticalLayout_16.addWidget(self.iconCloseModStudent, 0, Qt.AlignRight)

        self.widget_10 = QWidget(self.rightMenu_5)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMinimumSize(QSize(200, 312))
        self.verticalLayout_28 = QVBoxLayout(self.widget_10)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_4 = QLabel(self.widget_10)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(70, 70))
        self.label_4.setMaximumSize(QSize(70, 70))
        self.label_4.setPixmap(QPixmap(u"../SSIS v@/Resource/addUser.png"))
        self.label_4.setScaledContents(True)

        self.verticalLayout_28.addWidget(self.label_4, 0, Qt.AlignHCenter)

        self.frame_17 = QFrame(self.widget_10)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_17)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.idNum_2 = QLineEdit(self.frame_17)
        self.idNum_2.setObjectName(u"idNum_2")
        self.idNum_2.setStyleSheet(u"QLineEdit {\n"
"	background-color: #1b1b27;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_29.addWidget(self.idNum_2)

        self.fullName_2 = QLineEdit(self.frame_17)
        self.fullName_2.setObjectName(u"fullName_2")
        self.fullName_2.setFont(font4)
        self.fullName_2.setStyleSheet(u"QLineEdit {\n"
"	background-color: #1b1b27;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_29.addWidget(self.fullName_2)

        self.gender_2 = QComboBox(self.frame_17)
        self.gender_2.setObjectName(u"gender_2")
        self.gender_2.setStyleSheet(u"QComboBox {\n"
"	background-color: #1b1b27;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_29.addWidget(self.gender_2)

        self.yearLevel_2 = QLineEdit(self.frame_17)
        self.yearLevel_2.setObjectName(u"yearLevel_2")
        self.yearLevel_2.setFont(font5)
        self.yearLevel_2.setStyleSheet(u"QLineEdit {\n"
"	background-color: #1b1b27;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_29.addWidget(self.yearLevel_2)

        self.courseCode_2 = QComboBox(self.frame_17)
        self.courseCode_2.setObjectName(u"courseCode_2")
        self.courseCode_2.setStyleSheet(u"QComboBox {\n"
"	background-color: #1b1b27;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_29.addWidget(self.courseCode_2)


        self.verticalLayout_28.addWidget(self.frame_17)

        self.updateStudentButton = QPushButton(self.widget_10)
        self.updateStudentButton.setObjectName(u"updateStudentButton")
        self.updateStudentButton.setFont(font6)
        self.updateStudentButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_28.addWidget(self.updateStudentButton, 0, Qt.AlignHCenter)


        self.verticalLayout_16.addWidget(self.widget_10, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.rightMenu_5)

        self.rightMenu_4 = QCustomSlideMenu(self.mainBody)
        self.rightMenu_4.setObjectName(u"rightMenu_4")
        self.rightMenu_4.setMinimumSize(QSize(0, 0))
        self.rightMenu_4.setMaximumSize(QSize(0, 16777215))
        self.verticalLayout_20 = QVBoxLayout(self.rightMenu_4)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(-1, -1, 0, -1)
        self.iconCloseDelCourse = QPushButton(self.rightMenu_4)
        self.iconCloseDelCourse.setObjectName(u"iconCloseDelCourse")
        self.iconCloseDelCourse.setIcon(icon6)
        self.iconCloseDelCourse.setIconSize(QSize(24, 24))

        self.verticalLayout_20.addWidget(self.iconCloseDelCourse, 0, Qt.AlignRight)

        self.widget_9 = QWidget(self.rightMenu_4)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(200, 312))
        self.verticalLayout_21 = QVBoxLayout(self.widget_9)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_10 = QLabel(self.widget_9)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(70, 70))
        self.label_10.setMaximumSize(QSize(70, 70))
        self.label_10.setPixmap(QPixmap(u"../SSIS v@/Resource/whiteDelete.png"))
        self.label_10.setScaledContents(True)

        self.verticalLayout_21.addWidget(self.label_10, 0, Qt.AlignHCenter)

        self.frame_14 = QFrame(self.widget_9)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_14)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(-1, -1, 9, -1)
        self.courseCodeLine = QLineEdit(self.frame_14)
        self.courseCodeLine.setObjectName(u"courseCodeLine")
        self.courseCodeLine.setStyleSheet(u"QLineEdit {\n"
"	background-color: #1b1b27;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_27.addWidget(self.courseCodeLine)

        self.deleteCourseButton = QPushButton(self.frame_14)
        self.deleteCourseButton.setObjectName(u"deleteCourseButton")
        self.deleteCourseButton.setFont(font6)
        self.deleteCourseButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_27.addWidget(self.deleteCourseButton, 0, Qt.AlignHCenter)


        self.verticalLayout_21.addWidget(self.frame_14)


        self.verticalLayout_20.addWidget(self.widget_9, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.rightMenu_4, 0, Qt.AlignHCenter)

        self.rightMenu_3 = QCustomSlideMenu(self.mainBody)
        self.rightMenu_3.setObjectName(u"rightMenu_3")
        self.rightMenu_3.setMinimumSize(QSize(0, 0))
        self.rightMenu_3.setMaximumSize(QSize(0, 16777215))
        self.verticalLayout_17 = QVBoxLayout(self.rightMenu_3)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(-1, -1, 0, -1)
        self.iconCloseDelStudent = QPushButton(self.rightMenu_3)
        self.iconCloseDelStudent.setObjectName(u"iconCloseDelStudent")
        self.iconCloseDelStudent.setIcon(icon6)
        self.iconCloseDelStudent.setIconSize(QSize(24, 24))

        self.verticalLayout_17.addWidget(self.iconCloseDelStudent, 0, Qt.AlignRight)

        self.widget_8 = QWidget(self.rightMenu_3)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(200, 312))
        self.verticalLayout_18 = QVBoxLayout(self.widget_8)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_9 = QLabel(self.widget_8)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(70, 70))
        self.label_9.setMaximumSize(QSize(70, 70))
        self.label_9.setPixmap(QPixmap(u"../SSIS v@/Resource/whiteDelete.png"))
        self.label_9.setScaledContents(True)

        self.verticalLayout_18.addWidget(self.label_9, 0, Qt.AlignHCenter)

        self.frame_13 = QFrame(self.widget_8)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_13)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(-1, -1, 9, -1)
        self.idNum_3 = QLineEdit(self.frame_13)
        self.idNum_3.setObjectName(u"idNum_3")
        self.idNum_3.setStyleSheet(u"QLineEdit {\n"
"	background-color: #1b1b27;\n"
"	padding: 5px 10px;\n"
"	border-radius: 5px;\n"
"}")

        self.verticalLayout_19.addWidget(self.idNum_3)

        self.deleteStudentButton = QPushButton(self.frame_13)
        self.deleteStudentButton.setObjectName(u"deleteStudentButton")
        self.deleteStudentButton.setFont(font6)
        self.deleteStudentButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_19.addWidget(self.deleteStudentButton, 0, Qt.AlignHCenter)


        self.verticalLayout_18.addWidget(self.frame_13)


        self.verticalLayout_17.addWidget(self.widget_8, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.rightMenu_3)


        self.verticalLayout.addWidget(self.mainBody)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mainPages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"SIMPLE STUDENT INFORMATION SYSTEM", None))
        self.addStudent.setText(QCoreApplication.translate("MainWindow", u"Student Page", None))
        self.addCourse.setText(QCoreApplication.translate("MainWindow", u"Course Page", None))
        self.deleteStudentBtn.setText(QCoreApplication.translate("MainWindow", u"Modify Student Page", None))
        self.deleteCourseBtn.setText(QCoreApplication.translate("MainWindow", u"Modify Course Page", None))
        self.aboutButton.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Student Page", None))
        self.ssearchBtn.setText("")
        self.showAdd.setText(QCoreApplication.translate("MainWindow", u"Add Student", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID Number", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Full Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Gender", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Year Level", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Course Code", None));
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Modify Course Page", None))
        self.editCourseButton.setText("")
        self.deleteCourseBTN.setText(QCoreApplication.translate("MainWindow", u"Delete Course", None))
        ___qtablewidgetitem5 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Course", None));
        ___qtablewidgetitem6 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Course Code", None));
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Modify Student Page", None))
        self.editStudentButton.setText("")
        self.deleteButton.setText(QCoreApplication.translate("MainWindow", u"Delete Student", None))
        ___qtablewidgetitem7 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"ID Number", None));
        ___qtablewidgetitem8 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Full Name", None));
        ___qtablewidgetitem9 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Gender", None));
        ___qtablewidgetitem10 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Year Level", None));
        ___qtablewidgetitem11 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Course Code", None));
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Course Page", None))
        self.csearchBtn.setText("")
        self.addCourseButton.setText(QCoreApplication.translate("MainWindow", u"Add Course", None))
        ___qtablewidgetitem12 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Course", None));
        ___qtablewidgetitem13 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Course Code", None));
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"About Age", None))
        self.iconCloseStudent.setText("")
        self.label_2.setText("")
        self.idNum.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID Number", None))
        self.fullName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Full Name", None))
        self.gender.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.yearLevel.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Year Level", None))
        self.courseCode.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Course Code", None))
        self.addInfo.setText(QCoreApplication.translate("MainWindow", u"Add Student", None))
        self.iconCloseCourse.setText("")
        self.label_12.setText("")
        self.course.setText("")
        self.course.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Course (Eg. BS In Biology)", None))
        self.course_Code.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Course Code (Eg. BSB)", None))
        self.inputCourse.setText(QCoreApplication.translate("MainWindow", u"Add Course", None))
        self.iconCloseModCourse.setText("")
        self.label_13.setText("")
        self.course_2.setText("")
        self.course_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Course (Eg. BS In Biology)", None))
        self.course_Code_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Course Code (Eg. BSB)", None))
        self.updateCourseButton.setText(QCoreApplication.translate("MainWindow", u"Update Course", None))
        self.iconCloseModStudent.setText("")
        self.label_4.setText("")
        self.idNum_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID Number", None))
        self.fullName_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Full Name", None))
        self.gender_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.yearLevel_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Year Level", None))
        self.courseCode_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Course Code", None))
        self.updateStudentButton.setText(QCoreApplication.translate("MainWindow", u"Update Student", None))
        self.iconCloseDelCourse.setText("")
        self.label_10.setText("")
        self.courseCodeLine.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Course Code", None))
        self.deleteCourseButton.setText(QCoreApplication.translate("MainWindow", u"Delete Course", None))
        self.iconCloseDelStudent.setText("")
        self.label_9.setText("")
        self.idNum_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID Number", None))
        self.deleteStudentButton.setText(QCoreApplication.translate("MainWindow", u"Delete Student", None))
    # retranslateUi

