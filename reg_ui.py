from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Reg_Window(object):
    def setupUi(self, Reg_Window):
        Reg_Window.setObjectName("Reg_Window")
        Reg_Window.resize(585, 462)
        Reg_Window.setMaximumSize(QtCore.QSize(585, 462))
        Reg_Window.setStyleSheet("background-color: rgb(0, 244, 179);")
        Reg_Window.setWindowTitle("Новый пользователь")
        Reg_Window.setWindowIcon(QtGui.QIcon("icons/logo/chart-user.png"))
        self.centralwidget = QtWidgets.QWidget(Reg_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setStyleSheet("\n"
"font: 57 12pt \"Source Code Pro Black\";")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 57 12pt \"Source Code Pro Medium\";")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setStyleSheet("\n"
"font: 57 12pt \"Source Code Pro Black\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 57 12pt \"Source Code Pro Medium\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.frame_1 = QtWidgets.QFrame(self.frame)
        self.frame_1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_1.setObjectName("frame_1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.frame_1)
        self.label_3.setStyleSheet("\n"
"\n"
"font: 57 12pt \"Source Code Pro Black\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_1)
        self.lineEdit_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 57 12pt \"Source Code Pro Medium\";")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_4.addWidget(self.lineEdit_3)
        self.verticalLayout_2.addWidget(self.frame_1)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pushButton.setStyleSheet("\n"
"background-color: rgb(255, 255, 127);\n"
"font: 57 12pt \"Source Code Pro Black\";")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.frame_2)
        Reg_Window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Reg_Window)
        self.statusbar.setObjectName("statusbar")
        Reg_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Reg_Window)
        QtCore.QMetaObject.connectSlotsByName(Reg_Window)

    def retranslateUi(self, Reg_Window):
        _translate = QtCore.QCoreApplication.translate
        Reg_Window.setWindowTitle(_translate("Reg_Window", "MainWindow"))
        self.label.setText(_translate("Reg_Window", "Имя"))
        self.label_2.setText(_translate("Reg_Window", "Возраст"))
        self.label_3.setText(_translate("Reg_Window", "Пароль"))
        self.pushButton.setText(_translate("Reg_Window", "отправить данные"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Reg_Window = QtWidgets.QMainWindow()
    ui = Ui_Reg_Window()
    ui.setupUi(Reg_Window)
    Reg_Window.show()
    sys.exit(app.exec())
