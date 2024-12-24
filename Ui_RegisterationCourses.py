from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StudentRegisterationCourses(object):
    def setupUi(self, StudentRegisterationCourses):
        StudentRegisterationCourses.setObjectName("StudentRegisterationCourses")
        StudentRegisterationCourses.resize(689, 490)
        self.centralwidget = QtWidgets.QWidget(StudentRegisterationCourses)
        self.centralwidget.setObjectName("centralwidget")
        self.LoginPage = QtWidgets.QWidget(self.centralwidget)
        self.LoginPage.setEnabled(True)
        self.LoginPage.setGeometry(QtCore.QRect(0, 0, 691, 471))
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
        self.label_2.setGeometry(QtCore.QRect(270, 30, 181, 31))
        self.label_2.setStyleSheet("font: 63 14pt \"Sitka Display Semibold\";\n"
                                    "background-color: rgb(66, 167, 255);\n"
                                    "")
        self.label_2.setObjectName("label_2")
        self.scrollArea = QtWidgets.QScrollArea(self.LoginPage)
        self.scrollArea.setGeometry(QtCore.QRect(290, 120, 361, 271))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.Content = QtWidgets.QWidget()
        self.Content.setGeometry(QtCore.QRect(0, 0, 359, 269))
        self.Content.setObjectName("Content")

        # Setting layout for the Content widget
        self.contentLayout = QtWidgets.QVBoxLayout(self.Content)
        self.contentLayout.setObjectName("contentLayout")

        # Content data that will be scrollable
        self.Content_Data = QtWidgets.QLabel(self.Content)
        self.Content_Data.setText("Sample text to demonstrate scrolling. " * 50)  # Sufficient text for scrolling
        self.Content_Data.setWordWrap(True)
        self.Content_Data.setObjectName("Content_Data")

        self.contentLayout.addWidget(self.Content_Data)
        self.scrollArea.setWidget(self.Content)

        self.pushButton = QtWidgets.QPushButton(self.LoginPage)
        self.pushButton.setGeometry(QtCore.QRect(10, 422, 61, 31))
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.LoginPage)
        self.label_3.setGeometry(QtCore.QRect(30, 130, 221, 251))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("C:/Users/dell/Downloads/Umt_logo.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")

        self.widget_3.raise_()
        self.LoginDetailLabel.raise_()
        self.scrollArea.raise_()
        self.pushButton.raise_()
        self.label_3.raise_()
        StudentRegisterationCourses.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(StudentRegisterationCourses)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 689, 21))
        self.menubar.setObjectName("menubar")
        StudentRegisterationCourses.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(StudentRegisterationCourses)
        self.statusbar.setObjectName("statusbar")
        StudentRegisterationCourses.setStatusBar(self.statusbar)

        self.retranslateUi(StudentRegisterationCourses)
        QtCore.QMetaObject.connectSlotsByName(StudentRegisterationCourses)

    def retranslateUi(self, StudentRegisterationCourses):
        _translate = QtCore.QCoreApplication.translate
        StudentRegisterationCourses.setWindowTitle(_translate("StudentRegisterationCourses", "MainWindow"))
        self.label_2.setText(_translate("StudentRegisterationCourses", "Registered Courses"))
        self.pushButton.setText(_translate("StudentRegisterationCourses", "<<Back"))


# Main script to run the application
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StudentRegisterationCourses = QtWidgets.QMainWindow()
    ui = Ui_StudentRegisterationCourses()
    ui.setupUi(StudentRegisterationCourses)
    StudentRegisterationCourses.show()
    sys.exit(app.exec_())
