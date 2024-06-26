# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form2.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(465, 226)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 471, 271))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.crypt_password_le = QtWidgets.QLineEdit(self.layoutWidget)
        self.crypt_password_le.setObjectName("crypt_password_le")
        self.horizontalLayout.addWidget(self.crypt_password_le)
        self.GO_pb = QtWidgets.QPushButton(self.layoutWidget)
        self.GO_pb.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.GO_pb.setObjectName("GO_pb")
        self.horizontalLayout.addWidget(self.GO_pb)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabWidget = QtWidgets.QTabWidget(self.layoutWidget)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setToolTipDuration(-5)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.add_password_1_tab = QtWidgets.QWidget()
        self.add_password_1_tab.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.add_password_1_tab.setObjectName("add_password_1_tab")
        self.label = QtWidgets.QLabel(self.add_password_1_tab)
        self.label.setGeometry(QtCore.QRect(0, 24, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.add_password_1_tab)
        self.label_2.setGeometry(QtCore.QRect(0, 56, 47, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.add_password_1_tab)
        self.label_3.setGeometry(QtCore.QRect(0, 88, 99, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.add_password_1_tab)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 120, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.layoutWidget1 = QtWidgets.QWidget(self.add_password_1_tab)
        self.layoutWidget1.setGeometry(QtCore.QRect(114, 9, 341, 111))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Soc_set_le = QtWidgets.QLineEdit(self.layoutWidget1)
        self.Soc_set_le.setObjectName("Soc_set_le")
        self.verticalLayout_2.addWidget(self.Soc_set_le)
        self.password_le = QtWidgets.QLineEdit(self.layoutWidget1)
        self.password_le.setObjectName("password_le")
        self.verticalLayout_2.addWidget(self.password_le)
        self.dop_le = QtWidgets.QLineEdit(self.layoutWidget1)
        self.dop_le.setObjectName("dop_le")
        self.verticalLayout_2.addWidget(self.dop_le)
        self.tabWidget.addTab(self.add_password_1_tab, "")
        self.read_2_tab = QtWidgets.QWidget()
        self.read_2_tab.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.read_2_tab.setObjectName("read_2_tab")
        self.tableWidget = QtWidgets.QTableWidget(self.read_2_tab)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 461, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tabWidget.addTab(self.read_2_tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 465, 24))
        self.menuBar.setObjectName("menuBar")
        self.menuGo_to = QtWidgets.QMenu(self.menuBar)
        self.menuGo_to.setObjectName("menuGo_to")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuHow_it_works = QtWidgets.QMenu(self.menuHelp)
        self.menuHow_it_works.setObjectName("menuHow_it_works")
        MainWindow.setMenuBar(self.menuBar)
        self.actionRead = QtWidgets.QAction(MainWindow)
        self.actionRead.setObjectName("actionRead")
        self.actionAdd_new_note = QtWidgets.QAction(MainWindow)
        self.actionAdd_new_note.setObjectName("actionAdd_new_note")
        self.actionEnglish = QtWidgets.QAction(MainWindow)
        self.actionEnglish.setObjectName("actionEnglish")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.menuGo_to.addAction(self.actionRead)
        self.menuGo_to.addSeparator()
        self.menuGo_to.addAction(self.actionAdd_new_note)
        self.menuHow_it_works.addAction(self.actionEnglish)
        self.menuHow_it_works.addAction(self.action_3)
        self.menuHelp.addAction(self.menuHow_it_works.menuAction())
        self.menuBar.addAction(self.menuGo_to.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password crypter"))
        self.GO_pb.setText(_translate("MainWindow", "Go"))
        self.label.setText(_translate("MainWindow", "Соц. сеть"))
        self.label_2.setText(_translate("MainWindow", "Пароль"))
        self.label_3.setText(_translate("MainWindow", "Дополнительно"))
        self.pushButton_2.setText(_translate("MainWindow", "Добавить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.add_password_1_tab), _translate("MainWindow", "Добавить пароль"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Соц. сеть"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Пароль"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Дополнительно"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.read_2_tab), _translate("MainWindow", "Прочитать"))
        self.menuGo_to.setTitle(_translate("MainWindow", "Go to..."))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuHow_it_works.setTitle(_translate("MainWindow", "How it works?"))
        self.actionRead.setText(_translate("MainWindow", "Read"))
        self.actionAdd_new_note.setText(_translate("MainWindow", "Add new password"))
        self.actionEnglish.setText(_translate("MainWindow", "English"))
        self.action_3.setText(_translate("MainWindow", "Русский"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

# from PyQt5 import QtCore, QtGui, QtWidgets


