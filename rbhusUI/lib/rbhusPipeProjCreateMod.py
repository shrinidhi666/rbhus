# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rbhusPipeProjCreateMod.ui'
#
# Created by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
  _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
  def _fromUtf8(s):
    return s

try:
  _encoding = QtGui.QApplication.UnicodeUTF8
  def _translate(context, text, disambig):
    return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
  def _translate(context, text, disambig):
    return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
  def setupUi(self, MainWindow):
    MainWindow.setObjectName(_fromUtf8("MainWindow"))
    MainWindow.resize(263, 248)
    self.centralwidget = QtGui.QWidget(MainWindow)
    self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
    self.gridLayout = QtGui.QGridLayout(self.centralwidget)
    self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
    self.labelAclUser = QtGui.QLabel(self.centralwidget)
    self.labelAclUser.setObjectName(_fromUtf8("labelAclUser"))
    self.gridLayout.addWidget(self.labelAclUser, 6, 0, 1, 1)
    self.pushCreate = QtGui.QPushButton(self.centralwidget)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.pushCreate.sizePolicy().hasHeightForWidth())
    self.pushCreate.setSizePolicy(sizePolicy)
    self.pushCreate.setObjectName(_fromUtf8("pushCreate"))
    self.gridLayout.addWidget(self.pushCreate, 12, 0, 1, 2)
    self.labelDue = QtGui.QLabel(self.centralwidget)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.labelDue.sizePolicy().hasHeightForWidth())
    self.labelDue.setSizePolicy(sizePolicy)
    self.labelDue.setObjectName(_fromUtf8("labelDue"))
    self.gridLayout.addWidget(self.labelDue, 4, 0, 1, 1)
    self.labelProj_2 = QtGui.QLabel(self.centralwidget)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.labelProj_2.sizePolicy().hasHeightForWidth())
    self.labelProj_2.setSizePolicy(sizePolicy)
    self.labelProj_2.setObjectName(_fromUtf8("labelProj_2"))
    self.gridLayout.addWidget(self.labelProj_2, 0, 0, 1, 1)
    spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
    self.gridLayout.addItem(spacerItem, 8, 0, 1, 2)
    self.lineEditAclUser = QtGui.QLineEdit(self.centralwidget)
    self.lineEditAclUser.setObjectName(_fromUtf8("lineEditAclUser"))
    self.gridLayout.addWidget(self.lineEditAclUser, 6, 1, 1, 1)
    self.lineEditAdmins = QtGui.QLineEdit(self.centralwidget)
    self.lineEditAdmins.setObjectName(_fromUtf8("lineEditAdmins"))
    self.gridLayout.addWidget(self.lineEditAdmins, 5, 1, 1, 1)
    self.dateEditDue = QtGui.QDateEdit(self.centralwidget)
    self.dateEditDue.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.India))
    self.dateEditDue.setAccelerated(False)
    self.dateEditDue.setCalendarPopup(True)
    self.dateEditDue.setObjectName(_fromUtf8("dateEditDue"))
    self.gridLayout.addWidget(self.dateEditDue, 4, 1, 1, 1)
    self.checkBox = QtGui.QCheckBox(self.centralwidget)
    self.checkBox.setChecked(True)
    self.checkBox.setObjectName(_fromUtf8("checkBox"))
    self.gridLayout.addWidget(self.checkBox, 11, 0, 1, 3)
    self.line = QtGui.QFrame(self.centralwidget)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
    self.line.setSizePolicy(sizePolicy)
    self.line.setFrameShape(QtGui.QFrame.HLine)
    self.line.setFrameShadow(QtGui.QFrame.Sunken)
    self.line.setObjectName(_fromUtf8("line"))
    self.gridLayout.addWidget(self.line, 9, 0, 1, 2)
    self.labelDirectory = QtGui.QLabel(self.centralwidget)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.labelDirectory.sizePolicy().hasHeightForWidth())
    self.labelDirectory.setSizePolicy(sizePolicy)
    self.labelDirectory.setObjectName(_fromUtf8("labelDirectory"))
    self.gridLayout.addWidget(self.labelDirectory, 2, 0, 1, 1)
    self.labelAdmin = QtGui.QLabel(self.centralwidget)
    self.labelAdmin.setObjectName(_fromUtf8("labelAdmin"))
    self.gridLayout.addWidget(self.labelAdmin, 5, 0, 1, 1)
    self.labelName = QtGui.QLabel(self.centralwidget)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.labelName.sizePolicy().hasHeightForWidth())
    self.labelName.setSizePolicy(sizePolicy)
    self.labelName.setObjectName(_fromUtf8("labelName"))
    self.gridLayout.addWidget(self.labelName, 1, 0, 1, 1)
    self.comboProjType = QtGui.QComboBox(self.centralwidget)
    self.comboProjType.setObjectName(_fromUtf8("comboProjType"))
    self.gridLayout.addWidget(self.comboProjType, 0, 1, 1, 1)
    self.comboDirectory = QtGui.QComboBox(self.centralwidget)
    self.comboDirectory.setObjectName(_fromUtf8("comboDirectory"))
    self.gridLayout.addWidget(self.comboDirectory, 2, 1, 1, 1)
    self.lineEditName = QtGui.QLineEdit(self.centralwidget)
    self.lineEditName.setObjectName(_fromUtf8("lineEditName"))
    self.gridLayout.addWidget(self.lineEditName, 1, 1, 1, 1)
    self.labelAclGroup = QtGui.QLabel(self.centralwidget)
    self.labelAclGroup.setObjectName(_fromUtf8("labelAclGroup"))
    self.gridLayout.addWidget(self.labelAclGroup, 7, 0, 1, 1)
    self.lineEditAclGroup = QtGui.QLineEdit(self.centralwidget)
    self.lineEditAclGroup.setObjectName(_fromUtf8("lineEditAclGroup"))
    self.gridLayout.addWidget(self.lineEditAclGroup, 7, 1, 1, 1)
    MainWindow.setCentralWidget(self.centralwidget)

    self.retranslateUi(MainWindow)
    QtCore.QMetaObject.connectSlotsByName(MainWindow)

  def retranslateUi(self, MainWindow):
    MainWindow.setWindowTitle(_translate("MainWindow", "Rbhus Pipe NEW PROJECT", None))
    self.labelAclUser.setText(_translate("MainWindow", "aclUser", None))
    self.pushCreate.setText(_translate("MainWindow", "create", None))
    self.labelDue.setText(_translate("MainWindow", "due date", None))
    self.labelProj_2.setText(_translate("MainWindow", "projType", None))
    self.lineEditAclUser.setText(_translate("MainWindow", "kryptos", None))
    self.checkBox.setText(_translate("MainWindow", "rbhusRender intergration", None))
    self.labelDirectory.setWhatsThis(_translate("MainWindow", "directory to store the output data from file. eg : rendered output of lighting files.", None))
    self.labelDirectory.setText(_translate("MainWindow", "directory", None))
    self.labelAdmin.setText(_translate("MainWindow", "admins", None))
    self.labelName.setText(_translate("MainWindow", "name", None))
    self.labelAclGroup.setText(_translate("MainWindow", "aclGroup", None))
    self.lineEditAclGroup.setText(_translate("MainWindow", "artist", None))

