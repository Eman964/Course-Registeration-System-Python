from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RegisteredCoursesbyStudent(object):
    def setupUi(self, RegisteredCoursesbyStudent):
        RegisteredCoursesbyStudent.setObjectName("RegisteredCoursesbyStudent")
        RegisteredCoursesbyStudent.resize(694, 494)
        self.centralwidget = QtWidgets.QWidget(RegisteredCoursesbyStudent)
        self.centralwidget.setObjectName("centralwidget")
        self.LoginPage = QtWidgets.QWidget(self.centralwidget)
        self.LoginPage.setEnabled(True)
        self.LoginPage.setGeometry(QtCore.QRect(0, 0, 701, 471))
        self.LoginPage.setAutoFillBackground(False)
        self.LoginPage.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.LoginPage.setInputMethodHints(QtCore.Qt.ImhNone)
        self.LoginPage.setObjectName("LoginPage")
        self.LoginDetailLabel = QtWidgets.QLabel(self.LoginPage)
        self.LoginDetailLabel.setGeometry(QtCore.QRect(50, 310, 361, 20))
        self.LoginDetailLabel.setText("")
        self.LoginDetailLabel.setObjectName("LoginDetailLabel")
        self.widget_3 = QtWidgets.QWidget(self.LoginPage)
        self.widget_3.setGeometry(QtCore.QRect(0, 0, 701, 81))
        self.widget_3.setStyleSheet("background-color: rgb(66, 167, 255);")
        self.widget_3.setObjectName("widget_3")
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        self.label_2.setGeometry(QtCore.QRect(230, 30, 231, 31))
        self.label_2.setStyleSheet("font: 63 14pt \"Sitka Display Semibold\";\n"
                                   "background-color: rgb(66, 167, 255);\n"
                                   "")
        self.label_2.setObjectName("label_2")

        # Scroll Area setup
        self.scrollArea = QtWidgets.QScrollArea(self.LoginPage)
        self.scrollArea.setGeometry(QtCore.QRect(280, 120, 371, 321))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        # Scroll Area Content setup
        self.Content = QtWidgets.QWidget()
        self.Content.setGeometry(QtCore.QRect(0, 0, 350, 1000))  # Ensuring height is enough for scrolling
        self.Content.setObjectName("Content")

        # Setting layout for the Content widget
        self.contentLayout = QtWidgets.QVBoxLayout(self.Content)
        self.contentLayout.setObjectName("contentLayout")

        # Content data that will be scrollable
        self.ContentData = QtWidgets.QLabel(self.Content)
        self.ContentData.setText("Sample text to demonstrate scrolling. " * 50)  # Sufficient text for scrolling
        self.ContentData.setWordWrap(True)
        self.ContentData.setObjectName("ContentData")

        self.contentLayout.addWidget(self.ContentData)
        self.scrollArea.setWidget(self.Content)

        self.pushButton = QtWidgets.QPushButton(self.LoginPage)
        self.pushButton.setGeometry(QtCore.QRect(30, 420, 61, 31))
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")

        self.label_5 = QtWidgets.QLabel(self.LoginPage)
        self.label_5.setGeometry(QtCore.QRect(30, 130, 221, 251))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("C:/Users/dell/Downloads/Umt_logo.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")

        self.widget_3.raise_()
        self.LoginDetailLabel.raise_()
        self.scrollArea.raise_()
        self.pushButton.raise_()
        self.label_5.raise_()

        RegisteredCoursesbyStudent.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RegisteredCoursesbyStudent)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 694, 21))
        self.menubar.setObjectName("menubar")
        RegisteredCoursesbyStudent.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RegisteredCoursesbyStudent)
        self.statusbar.setObjectName("statusbar")
        RegisteredCoursesbyStudent.setStatusBar(self.statusbar)

        self.retranslateUi(RegisteredCoursesbyStudent)
        QtCore.QMetaObject.connectSlotsByName(RegisteredCoursesbyStudent)

    def retranslateUi(self, RegisteredCoursesbyStudent):
        _translate = QtCore.QCoreApplication.translate
        RegisteredCoursesbyStudent.setWindowTitle(_translate("RegisteredCoursesbyStudent", "MainWindow"))
        self.label_2.setText(_translate("RegisteredCoursesbyStudent", "Student Registered Courses"))
        self.pushButton.setText(_translate("RegisteredCoursesbyStudent", "<<Back"))

# Main script to run the application
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RegisteredCoursesbyStudent = QtWidgets.QMainWindow()
    ui = Ui_RegisteredCoursesbyStudent()
    ui.setupUi(RegisteredCoursesbyStudent)
    RegisteredCoursesbyStudent.show()
    sys.exit(app.exec_())
