# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Dump\heads_up\qtgui\ui\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(520, 313)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(520, 313))
        MainWindow.setMaximumSize(QtCore.QSize(520, 313))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_today_title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_today_title.setFont(font)
        self.label_today_title.setObjectName("label_today_title")
        self.verticalLayout_6.addWidget(self.label_today_title)
        self.plainTextEdit_today = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit_today.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_today.setSizePolicy(sizePolicy)
        self.plainTextEdit_today.setMinimumSize(QtCore.QSize(0, 50))
        self.plainTextEdit_today.setMaximumSize(QtCore.QSize(16777215, 45))
        self.plainTextEdit_today.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.plainTextEdit_today.setFrameShadow(QtWidgets.QFrame.Plain)
        self.plainTextEdit_today.setLineWidth(1)
        self.plainTextEdit_today.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_today.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.plainTextEdit_today.setReadOnly(True)
        self.plainTextEdit_today.setObjectName("plainTextEdit_today")
        self.verticalLayout_6.addWidget(self.plainTextEdit_today)
        self.label_tomorrow_title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_tomorrow_title.setFont(font)
        self.label_tomorrow_title.setObjectName("label_tomorrow_title")
        self.verticalLayout_6.addWidget(self.label_tomorrow_title)
        self.plainTextEdit_tomorrow = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit_tomorrow.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_tomorrow.setSizePolicy(sizePolicy)
        self.plainTextEdit_tomorrow.setMinimumSize(QtCore.QSize(0, 50))
        self.plainTextEdit_tomorrow.setMaximumSize(QtCore.QSize(16777215, 45))
        self.plainTextEdit_tomorrow.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.plainTextEdit_tomorrow.setFrameShadow(QtWidgets.QFrame.Plain)
        self.plainTextEdit_tomorrow.setLineWidth(1)
        self.plainTextEdit_tomorrow.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_tomorrow.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.plainTextEdit_tomorrow.setReadOnly(True)
        self.plainTextEdit_tomorrow.setObjectName("plainTextEdit_tomorrow")
        self.verticalLayout_6.addWidget(self.plainTextEdit_tomorrow)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.tableWidget_calendar = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_calendar.setMinimumSize(QtCore.QSize(400, 120))
        self.tableWidget_calendar.setMaximumSize(QtCore.QSize(400, 120))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tableWidget_calendar.setFont(font)
        self.tableWidget_calendar.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_calendar.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_calendar.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget_calendar.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_calendar.setTabKeyNavigation(False)
        self.tableWidget_calendar.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget_calendar.setRowCount(5)
        self.tableWidget_calendar.setColumnCount(8)
        self.tableWidget_calendar.setObjectName("tableWidget_calendar")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_calendar.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_calendar.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_calendar.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_calendar.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_calendar.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_calendar.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_calendar.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_calendar.setItem(0, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_calendar.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_calendar.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_calendar.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_calendar.setItem(4, 0, item)
        self.tableWidget_calendar.horizontalHeader().setVisible(False)
        self.tableWidget_calendar.horizontalHeader().setDefaultSectionSize(50)
        self.tableWidget_calendar.horizontalHeader().setMinimumSectionSize(13)
        self.tableWidget_calendar.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_calendar.verticalHeader().setVisible(False)
        self.tableWidget_calendar.verticalHeader().setDefaultSectionSize(23)
        self.tableWidget_calendar.verticalHeader().setHighlightSections(False)
        self.tableWidget_calendar.verticalHeader().setMinimumSectionSize(14)
        self.tableWidget_calendar.verticalHeader().setStretchLastSection(True)
        self.horizontalLayout_3.addWidget(self.tableWidget_calendar)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_shortcut1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_shortcut1.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_shortcut1.sizePolicy().hasHeightForWidth())
        self.pushButton_shortcut1.setSizePolicy(sizePolicy)
        self.pushButton_shortcut1.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_shortcut1.setObjectName("pushButton_shortcut1")
        self.verticalLayout_4.addWidget(self.pushButton_shortcut1)
        self.pushButton_shortcut2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_shortcut2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_shortcut2.sizePolicy().hasHeightForWidth())
        self.pushButton_shortcut2.setSizePolicy(sizePolicy)
        self.pushButton_shortcut2.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_shortcut2.setText("")
        self.pushButton_shortcut2.setObjectName("pushButton_shortcut2")
        self.verticalLayout_4.addWidget(self.pushButton_shortcut2)
        self.pushButton_shortcut3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_shortcut3.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_shortcut3.sizePolicy().hasHeightForWidth())
        self.pushButton_shortcut3.setSizePolicy(sizePolicy)
        self.pushButton_shortcut3.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_shortcut3.setText("")
        self.pushButton_shortcut3.setObjectName("pushButton_shortcut3")
        self.verticalLayout_4.addWidget(self.pushButton_shortcut3)
        self.pushButton_shortcut4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_shortcut4.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_shortcut4.sizePolicy().hasHeightForWidth())
        self.pushButton_shortcut4.setSizePolicy(sizePolicy)
        self.pushButton_shortcut4.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_shortcut4.setText("")
        self.pushButton_shortcut4.setObjectName("pushButton_shortcut4")
        self.verticalLayout_4.addWidget(self.pushButton_shortcut4)
        self.pushButton_shortcut5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_shortcut5.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_shortcut5.sizePolicy().hasHeightForWidth())
        self.pushButton_shortcut5.setSizePolicy(sizePolicy)
        self.pushButton_shortcut5.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_shortcut5.setText("")
        self.pushButton_shortcut5.setObjectName("pushButton_shortcut5")
        self.verticalLayout_4.addWidget(self.pushButton_shortcut5)
        self.pushButton_shortcut6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_shortcut6.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_shortcut6.sizePolicy().hasHeightForWidth())
        self.pushButton_shortcut6.setSizePolicy(sizePolicy)
        self.pushButton_shortcut6.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_shortcut6.setText("")
        self.pushButton_shortcut6.setObjectName("pushButton_shortcut6")
        self.verticalLayout_4.addWidget(self.pushButton_shortcut6)
        self.pushButton_shortcut8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_shortcut8.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_shortcut8.sizePolicy().hasHeightForWidth())
        self.pushButton_shortcut8.setSizePolicy(sizePolicy)
        self.pushButton_shortcut8.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_shortcut8.setText("")
        self.pushButton_shortcut8.setObjectName("pushButton_shortcut8")
        self.verticalLayout_4.addWidget(self.pushButton_shortcut8)
        self.pushButton_shortcut8_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_shortcut8_2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_shortcut8_2.sizePolicy().hasHeightForWidth())
        self.pushButton_shortcut8_2.setSizePolicy(sizePolicy)
        self.pushButton_shortcut8_2.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_shortcut8_2.setText("")
        self.pushButton_shortcut8_2.setObjectName("pushButton_shortcut8_2")
        self.verticalLayout_4.addWidget(self.pushButton_shortcut8_2)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 520, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuDeveloper = QtWidgets.QMenu(self.menuBar)
        self.menuDeveloper.setObjectName("menuDeveloper")
        self.menuLog_Level = QtWidgets.QMenu(self.menuDeveloper)
        self.menuLog_Level.setObjectName("menuLog_Level")
        self.menuSettings = QtWidgets.QMenu(self.menuBar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.actionDISABLE = QtWidgets.QAction(MainWindow)
        self.actionDISABLE.setCheckable(True)
        self.actionDISABLE.setObjectName("actionDISABLE")
        self.actionWARNING = QtWidgets.QAction(MainWindow)
        self.actionWARNING.setCheckable(True)
        self.actionWARNING.setObjectName("actionWARNING")
        self.actionINFO = QtWidgets.QAction(MainWindow)
        self.actionINFO.setCheckable(True)
        self.actionINFO.setObjectName("actionINFO")
        self.actionDEBUG = QtWidgets.QAction(MainWindow)
        self.actionDEBUG.setCheckable(True)
        self.actionDEBUG.setObjectName("actionDEBUG")
        self.actionVERBOSE = QtWidgets.QAction(MainWindow)
        self.actionVERBOSE.setCheckable(True)
        self.actionVERBOSE.setObjectName("actionVERBOSE")
        self.actionShow_developer_console = QtWidgets.QAction(MainWindow)
        self.actionShow_developer_console.setObjectName("actionShow_developer_console")
        self.actionCalendar_Notification_Manager = QtWidgets.QAction(MainWindow)
        self.actionCalendar_Notification_Manager.setObjectName("actionCalendar_Notification_Manager")
        self.actionEdit_shortcuts = QtWidgets.QAction(MainWindow)
        self.actionEdit_shortcuts.setObjectName("actionEdit_shortcuts")
        self.actionClear_shotcuts = QtWidgets.QAction(MainWindow)
        self.actionClear_shotcuts.setObjectName("actionClear_shotcuts")
        self.action_manage_shortcuts = QtWidgets.QAction(MainWindow)
        self.action_manage_shortcuts.setObjectName("action_manage_shortcuts")
        self.actionRemove_all_shortcuts = QtWidgets.QAction(MainWindow)
        self.actionRemove_all_shortcuts.setObjectName("actionRemove_all_shortcuts")
        self.action_manually_change_login = QtWidgets.QAction(MainWindow)
        self.action_manually_change_login.setObjectName("action_manually_change_login")
        self.actionChange_hours_per_day = QtWidgets.QAction(MainWindow)
        self.actionChange_hours_per_day.setObjectName("actionChange_hours_per_day")
        self.action_refresh_calendars = QtWidgets.QAction(MainWindow)
        self.action_refresh_calendars.setObjectName("action_refresh_calendars")
        self.actionUsing_the_calendar = QtWidgets.QAction(MainWindow)
        self.actionUsing_the_calendar.setObjectName("actionUsing_the_calendar")
        self.actionCreating_shortcuts = QtWidgets.QAction(MainWindow)
        self.actionCreating_shortcuts.setObjectName("actionCreating_shortcuts")
        self.menuLog_Level.addAction(self.actionDISABLE)
        self.menuLog_Level.addAction(self.actionWARNING)
        self.menuLog_Level.addAction(self.actionINFO)
        self.menuLog_Level.addAction(self.actionDEBUG)
        self.menuLog_Level.addAction(self.actionVERBOSE)
        self.menuDeveloper.addAction(self.menuLog_Level.menuAction())
        self.menuSettings.addAction(self.action_manage_shortcuts)
        self.menuSettings.addAction(self.actionRemove_all_shortcuts)
        self.menuHelp.addAction(self.actionUsing_the_calendar)
        self.menuHelp.addAction(self.actionCreating_shortcuts)
        self.menuBar.addAction(self.menuSettings.menuAction())
        self.menuBar.addAction(self.menuDeveloper.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HeadsUp"))
        self.label_today_title.setText(_translate("MainWindow", "Tuesday 29th June"))
        self.plainTextEdit_today.setPlainText(_translate("MainWindow", "15:00 - 15:30    Placeholder Text\n"
"15:00 - 15:30    J/C Monthly Something Meeting Pineapple\n"
"15:00 - 15:30    Placeholder Text"))
        self.label_tomorrow_title.setText(_translate("MainWindow", "Wednesday 30th June"))
        self.plainTextEdit_tomorrow.setPlainText(_translate("MainWindow", "15:00 - 15:30    Placeholder Text\n"
"15:00 - 15:30    J/C Monthly Something Meeting Pineapple\n"
"15:00 - 15:30    Placeholder Text"))
        __sortingEnabled = self.tableWidget_calendar.isSortingEnabled()
        self.tableWidget_calendar.setSortingEnabled(False)
        item = self.tableWidget_calendar.item(0, 1)
        item.setText(_translate("MainWindow", "Mon"))
        item = self.tableWidget_calendar.item(0, 2)
        item.setText(_translate("MainWindow", "Tue"))
        item = self.tableWidget_calendar.item(0, 3)
        item.setText(_translate("MainWindow", "Wed"))
        item = self.tableWidget_calendar.item(0, 4)
        item.setText(_translate("MainWindow", "Thu"))
        item = self.tableWidget_calendar.item(0, 5)
        item.setText(_translate("MainWindow", "Fri"))
        item = self.tableWidget_calendar.item(0, 6)
        item.setText(_translate("MainWindow", "Sat"))
        item = self.tableWidget_calendar.item(0, 7)
        item.setText(_translate("MainWindow", "Sun"))
        item = self.tableWidget_calendar.item(1, 0)
        item.setText(_translate("MainWindow", "01/08"))
        item = self.tableWidget_calendar.item(2, 0)
        item.setText(_translate("MainWindow", "01/08"))
        item = self.tableWidget_calendar.item(3, 0)
        item.setText(_translate("MainWindow", "01/08"))
        item = self.tableWidget_calendar.item(4, 0)
        item.setText(_translate("MainWindow", "01/08"))
        self.tableWidget_calendar.setSortingEnabled(__sortingEnabled)
        self.pushButton_shortcut1.setText(_translate("MainWindow", "<This is a sample>"))
        self.menuDeveloper.setTitle(_translate("MainWindow", "Developer"))
        self.menuLog_Level.setTitle(_translate("MainWindow", "Log Level"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionDISABLE.setText(_translate("MainWindow", "DISABLE"))
        self.actionWARNING.setText(_translate("MainWindow", "WARNING"))
        self.actionINFO.setText(_translate("MainWindow", "INFO"))
        self.actionDEBUG.setText(_translate("MainWindow", "DEBUG"))
        self.actionVERBOSE.setText(_translate("MainWindow", "VERBOSE"))
        self.actionShow_developer_console.setText(_translate("MainWindow", "Show developer console"))
        self.actionCalendar_Notification_Manager.setText(_translate("MainWindow", "Calendar Notification Manager"))
        self.actionEdit_shortcuts.setText(_translate("MainWindow", "Edit shortcuts..."))
        self.actionClear_shotcuts.setText(_translate("MainWindow", "Clear shotcuts..."))
        self.action_manage_shortcuts.setText(_translate("MainWindow", "Manage shortcuts"))
        self.actionRemove_all_shortcuts.setText(_translate("MainWindow", "Remove all shortcuts"))
        self.action_manually_change_login.setText(_translate("MainWindow", "Change login time..."))
        self.actionChange_hours_per_day.setText(_translate("MainWindow", "Change hours per day..."))
        self.action_refresh_calendars.setText(_translate("MainWindow", "Refresh calendars"))
        self.actionUsing_the_calendar.setText(_translate("MainWindow", "Calendar abbriviations..."))
        self.actionCreating_shortcuts.setText(_translate("MainWindow", "Creating shortcuts..."))
