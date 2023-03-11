# Form implementation generated from reading ui file 'assistant.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1237, 800)
        MainWindow.setMinimumSize(QtCore.QSize(652, 612))
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1080))
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        MainWindow.setIconSize(QtCore.QSize(34, 34))

        # sizes
        self.sidebarClosedSize = QtCore.QSize(0, 16777215)
        self.sidebarOpenedSize = QtCore.QSize(200, 1677215)
        self.frameMessagesSize = QtCore.QSize(16777215, 120)
        #

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sidebar = QtWidgets.QFrame(self.centralwidget)
        self.sidebar.setMaximumSize(self.sidebarClosedSize)
        font = QtGui.QFont()
        font.setFamily("Terminal")
        font.setPointSize(14)
        self.sidebar.setFont(font)
        self.sidebar.setStyleSheet("background-color: rgb(95, 190, 0);")
        self.sidebar.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.sidebar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.sidebar.setObjectName("sidebar")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.sidebar)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.titlemenu = QtWidgets.QFrame(self.sidebar)
        self.titlemenu.setMaximumSize(QtCore.QSize(16777215, 80))
        self.titlemenu.setAutoFillBackground(False)
        self.titlemenu.setStyleSheet("font: 87 12pt \"Source Serif Pro Black\";")
        self.titlemenu.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.titlemenu.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.titlemenu.setObjectName("titlemenu")
        self.logo = QtWidgets.QPushButton(self.titlemenu)
        self.logo.setGeometry(QtCore.QRect(0, 0, 71, 71))
        self.logo.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/logo/microphone.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.logo.setIcon(icon)
        self.logo.setIconSize(QtCore.QSize(50, 50))
        self.logo.setObjectName("logo")
        self.label_assissntat = QtWidgets.QLabel(self.titlemenu)
        self.label_assissntat.setGeometry(QtCore.QRect(80, 10, 101, 41))
        self.label_assissntat.setStyleSheet("font: 57 12pt \"Source Code Pro Black\";\n"
"")
        self.label_assissntat.setObjectName("label_assissntat")
        self.verticalLayout_2.addWidget(self.titlemenu)
        self.frame_2 = QtWidgets.QFrame(self.sidebar)
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.toolBox = QtWidgets.QToolBox(self.frame_2)
        self.toolBox.setGeometry(QtCore.QRect(10, 110, 181, 321))
        self.toolBox.setMaximumSize(QtCore.QSize(16777215, 160234))
        self.toolBox.setAutoFillBackground(False)
        self.toolBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 57 12pt \"Source Code Pro Black\";")
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_myaccount = QtWidgets.QLabel(self.page)
        self.label_myaccount.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_myaccount.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 57 12pt \"Source Code Pro Medium\";")
        self.label_myaccount.setObjectName("label_myaccount")
        self.verticalLayout_5.addWidget(self.label_myaccount)
        self.my_account = QtWidgets.QPushButton(self.page)
        self.my_account.setMaximumSize(QtCore.QSize(60, 60))
        self.my_account.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/logo/circle-user.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.my_account.setIcon(icon1)
        self.my_account.setIconSize(QtCore.QSize(50, 50))
        self.my_account.setObjectName("my_account")
        self.verticalLayout_5.addWidget(self.my_account)
        self.label_changeaccount = QtWidgets.QLabel(self.page)
        self.label_changeaccount.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label_changeaccount.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 57 12pt \"Source Code Pro Medium\";")
        self.label_changeaccount.setObjectName("label_changeaccount")
        self.verticalLayout_5.addWidget(self.label_changeaccount)
        self.change_account = QtWidgets.QPushButton(self.page)
        self.change_account.setMaximumSize(QtCore.QSize(60, 60))
        self.change_account.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/logo/chart-user.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.change_account.setIcon(icon2)
        self.change_account.setIconSize(QtCore.QSize(50, 50))
        self.change_account.setObjectName("change_account")
        self.verticalLayout_5.addWidget(self.change_account)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/logo/portrait.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolBox.addItem(self.page, icon3, "")
        self.Settings = QtWidgets.QWidget()
        self.Settings.setGeometry(QtCore.QRect(0, 0, 181, 265))
        self.Settings.setObjectName("Settings")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Settings)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_volume = QtWidgets.QLabel(self.Settings)
        self.label_volume.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 57 12pt \"Source Code Pro Medium\";")
        self.label_volume.setObjectName("label_volume")
        self.verticalLayout_4.addWidget(self.label_volume)
        self.volume = QtWidgets.QSlider(self.Settings)
        self.volume.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.volume.setObjectName("volume")
        self.verticalLayout_4.addWidget(self.volume)
        self.label_speed = QtWidgets.QLabel(self.Settings)
        self.label_speed.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 57 12pt \"Source Code Pro Medium\";")
        self.label_speed.setObjectName("label_speed")
        self.verticalLayout_4.addWidget(self.label_speed)
        self.speed = QtWidgets.QSlider(self.Settings)
        self.speed.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.speed.setObjectName("speed")
        self.verticalLayout_4.addWidget(self.speed)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/logo/volume.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolBox.addItem(self.Settings, icon4, "")
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_4 = QtWidgets.QFrame(self.sidebar)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.button_exit = QtWidgets.QPushButton(self.frame_4)
        self.button_exit.setGeometry(QtCore.QRect(10, 10, 171, 61))
        self.button_exit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 57 12pt \"Source Code Pro Black\";")
        self.button_exit.setObjectName("button_exit")
        self.verticalLayout_2.addWidget(self.frame_4)
        self.horizontalLayout.addWidget(self.sidebar)
        self.mainframe = QtWidgets.QFrame(self.centralwidget)
        self.mainframe.setStyleSheet("font: 87 14pt \"Source Serif Pro Black\";")
        self.mainframe.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.mainframe.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.mainframe.setObjectName("mainframe")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainframe)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.mainframe)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button_open_sidebar = QtWidgets.QPushButton(self.frame_3)
        self.button_open_sidebar.setMaximumSize(QtCore.QSize(60, 60))
        self.button_open_sidebar.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/logo/3917762.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.button_open_sidebar.setIcon(icon5)
        self.button_open_sidebar.setIconSize(QtCore.QSize(50, 50))
        self.button_open_sidebar.setShortcut("")
        self.button_open_sidebar.setObjectName("button_open_sidebar")
        self.horizontalLayout_2.addWidget(self.button_open_sidebar)
        self.label_title = QtWidgets.QLabel(self.frame_3)
        self.label_title.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Source Code Pro Black")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_title.setFont(font)
        self.label_title.setMouseTracking(True)
        self.label_title.setTabletTracking(False)
        self.label_title.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 57 18pt \"Source Code Pro Black\";")
        self.label_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.horizontalLayout_2.addWidget(self.label_title)
        self.button_clear_messages = QtWidgets.QPushButton(self.frame_3)
        self.button_clear_messages.setMaximumSize(QtCore.QSize(60, 60))
        self.button_clear_messages.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/logo/trash.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.button_clear_messages.setIcon(icon6)
        self.button_clear_messages.setIconSize(QtCore.QSize(50, 50))
        self.button_clear_messages.setObjectName("clear_messages")
        self.horizontalLayout_2.addWidget(self.button_clear_messages)
        self.verticalLayout.addWidget(self.frame_3)
        self.messages = QtWidgets.QFrame(self.mainframe)
        self.messages.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.messages.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.messages.setObjectName("messages")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.messages)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frameMessages4 = QtWidgets.QFrame(self.messages)
        self.frameMessages4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameMessages4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameMessages4.setObjectName("frameMessages4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frameMessages4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.fromwho4 = QtWidgets.QLabel(self.frameMessages4)
        self.fromwho4.setMaximumSize(QtCore.QSize(100, 16777215))
        self.fromwho4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 87 12pt \"Source Serif Pro Black\";")
        self.fromwho4.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.fromwho4.setObjectName("fromwho4")
        self.horizontalLayout_3.addWidget(self.fromwho4)
        self.message4 = QtWidgets.QLabel(self.frameMessages4)
        self.message4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 57 12pt \"Source Code Pro Medium\";")
        self.message4.setObjectName("message4")
        self.horizontalLayout_3.addWidget(self.message4)
        self.verticalLayout_3.addWidget(self.frameMessages4)
        self.frameMessages3 = QtWidgets.QFrame(self.messages)
        self.frameMessages3.setMaximumSize(QtCore.QSize(16777215, 120))
        self.frameMessages3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameMessages3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameMessages3.setObjectName("frameMessages3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frameMessages3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.fromwho3 = QtWidgets.QLabel(self.frameMessages3)
        self.fromwho3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.fromwho3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 87 12pt \"Source Serif Pro Black\";")
        self.fromwho3.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.fromwho3.setObjectName("fromwho3")
        self.horizontalLayout_4.addWidget(self.fromwho3)
        self.message3 = QtWidgets.QLabel(self.frameMessages3)
        self.message3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 57 12pt \"Source Code Pro Medium\";")
        self.message3.setObjectName("message3")
        self.horizontalLayout_4.addWidget(self.message3)
        self.verticalLayout_3.addWidget(self.frameMessages3)
        self.frameMessages2 = QtWidgets.QFrame(self.messages)
        self.frameMessages2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameMessages2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameMessages2.setObjectName("frameMessages2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frameMessages2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.fromwho2 = QtWidgets.QLabel(self.frameMessages2)
        self.fromwho2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.fromwho2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 87 12pt \"Source Serif Pro Black\";")
        self.fromwho2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.fromwho2.setObjectName("fromwho2")
        self.horizontalLayout_6.addWidget(self.fromwho2)
        self.message2 = QtWidgets.QLabel(self.frameMessages2)
        self.message2.setMaximumSize(QtCore.QSize(16777215, 120))
        self.message2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 57 12pt \"Source Code Pro Medium\";")
        self.message2.setObjectName("message2")
        self.horizontalLayout_6.addWidget(self.message2)
        self.verticalLayout_3.addWidget(self.frameMessages2)
        self.frameMessages1 = QtWidgets.QFrame(self.messages)
        self.frameMessages1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameMessages1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameMessages1.setObjectName("frameMessages1")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frameMessages1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.fromwho1 = QtWidgets.QLabel(self.frameMessages1)
        self.fromwho1.setMaximumSize(QtCore.QSize(100, 16777215))
        self.fromwho1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 87 12pt \"Source Serif Pro Black\";")
        self.fromwho1.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.fromwho1.setObjectName("fromwho1")
        self.horizontalLayout_5.addWidget(self.fromwho1)
        self.message1 = QtWidgets.QLabel(self.frameMessages1)
        self.message1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 57 12pt \"Source Code Pro Medium\";")
        self.message1.setObjectName("message1")
        self.horizontalLayout_5.addWidget(self.message1)
        self.verticalLayout_3.addWidget(self.frameMessages1)
        self.verticalLayout.addWidget(self.messages)
        self.buttonstart = QtWidgets.QFrame(self.mainframe)
        self.buttonstart.setMaximumSize(QtCore.QSize(16777215, 100))
        self.buttonstart.setStyleSheet("")
        self.buttonstart.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.buttonstart.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.buttonstart.setObjectName("buttonstart")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.buttonstart)
        self.horizontalLayout_7.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_7.setSpacing(1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_8 = QtWidgets.QFrame(self.buttonstart)
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_8.setSpacing(1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_10 = QtWidgets.QFrame(self.frame_8)
        self.frame_10.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.button_commands = QtWidgets.QPushButton(self.frame_10)
        self.button_commands.setMaximumSize(QtCore.QSize(60, 60))
        self.button_commands.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/logo/3917698.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.button_commands.setIcon(icon7)
        self.button_commands.setIconSize(QtCore.QSize(50, 50))
        self.button_commands.setObjectName("button_commands")
        self.horizontalLayout_9.addWidget(self.button_commands)
        self.button_news = QtWidgets.QPushButton(self.frame_10)
        self.button_news.setMaximumSize(QtCore.QSize(60, 60))
        self.button_news.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/logo/chart-line-up.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.button_news.setIcon(icon8)
        self.button_news.setIconSize(QtCore.QSize(50, 50))
        self.button_news.setObjectName("button_news")
        self.horizontalLayout_9.addWidget(self.button_news)
        self.button_ask = QtWidgets.QPushButton(self.frame_10)
        self.button_ask.setMaximumSize(QtCore.QSize(60, 60))
        self.button_ask.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/logo/interrogation.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.button_ask.setIcon(icon9)
        self.button_ask.setIconSize(QtCore.QSize(50, 50))
        self.button_ask.setObjectName("button_ask")
        self.horizontalLayout_9.addWidget(self.button_ask)
        self.button_search = QtWidgets.QPushButton(self.frame_10)
        self.button_search.setMaximumSize(QtCore.QSize(60, 60))
        self.button_search.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icons/logo/world.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.button_search.setIcon(icon10)
        self.button_search.setIconSize(QtCore.QSize(50, 50))
        self.button_search.setObjectName("button_search")
        self.horizontalLayout_9.addWidget(self.button_search)
        self.button_mathmode = QtWidgets.QPushButton(self.frame_10)
        self.button_mathmode.setMaximumSize(QtCore.QSize(60, 60))
        self.button_mathmode.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icons/logo/3914110.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.button_mathmode.setIcon(icon11)
        self.button_mathmode.setIconSize(QtCore.QSize(50, 50))
        self.button_mathmode.setObjectName("button_mathmode")
        self.horizontalLayout_9.addWidget(self.button_mathmode)
        self.horizontalLayout_8.addWidget(self.frame_10)
        self.frame_9 = QtWidgets.QFrame(self.frame_8)
        self.frame_9.setMaximumSize(QtCore.QSize(100, 100))
        self.frame_9.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.button_start = QtWidgets.QPushButton(self.frame_9)
        self.button_start.setMaximumSize(QtCore.QSize(60, 60))
        self.button_start.setStyleSheet("font: 14pt \"Terminal\";\n"
"\n"
"\n"
"")
        self.button_start.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("icons/logo/megaphone.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.button_start.setIcon(icon12)
        self.button_start.setIconSize(QtCore.QSize(50, 50))
        self.button_start.setObjectName("button_start")
        self.horizontalLayout_10.addWidget(self.button_start)
        self.horizontalLayout_8.addWidget(self.frame_9)
        self.horizontalLayout_7.addWidget(self.frame_8)
        self.verticalLayout.addWidget(self.buttonstart)
        self.horizontalLayout.addWidget(self.mainframe)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.action = QtGui.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_3 = QtGui.QAction(MainWindow)
        self.action_3.setObjectName("action_3")

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(1)
        self.toolBox.layout().setSpacing(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.clear_messages()

    def clear_messages(self):
        """Убрать все рамки сообщений при запуске"""
        self.frameMessages1.hide()
        self.frameMessages2.hide()
        self.frameMessages3.hide()
        self.frameMessages4.hide()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_assissntat.setText(_translate("MainWindow", "Assistant"))
        self.label_myaccount.setText(_translate("MainWindow", "Мой аккаунт"))
        self.label_changeaccount.setText(_translate("MainWindow", "Сменить аккаунт"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Аккаунт"))
        self.label_volume.setText(_translate("MainWindow", "Volume"))
        self.label_speed.setText(_translate("MainWindow", "Speed"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Settings), _translate("MainWindow", "Звук"))
        self.button_exit.setText(_translate("MainWindow", "Exit"))
        self.label_title.setText(_translate("MainWindow", "Диалог"))
        self.fromwho4.setText(_translate("MainWindow", "ME:"))
        self.message4.setText(_translate("MainWindow", "Привет"))
        self.fromwho3.setText(_translate("MainWindow", "ME:"))
        self.message3.setText(_translate("MainWindow", "Привет"))
        self.fromwho2.setText(_translate("MainWindow", "ME:"))
        self.message2.setText(_translate("MainWindow", "Привет"))
        self.fromwho1.setText(_translate("MainWindow", "ME:"))
        self.message1.setText(_translate("MainWindow", "Привет"))
        self.action.setText(_translate("MainWindow", "Окно"))
        self.action_3.setText(_translate("MainWindow", "Конфигурация ассистента"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
