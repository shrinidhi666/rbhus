# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rbhusPipeMainMod.ui'
#
# Created: Mon May 26 21:51:35 2014
#      by: PyQt4 UI code generator 4.10.3
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
    MainWindow.resize(667, 386)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Maximum)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
    MainWindow.setSizePolicy(sizePolicy)
    MainWindow.setDocumentMode(False)
    MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
    self.centralwidget = QtGui.QWidget(MainWindow)
    self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
    self.gridLayout = QtGui.QGridLayout(self.centralwidget)
    self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
    spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.gridLayout.addItem(spacerItem, 8, 1, 1, 2)
    self.assRefresh = QtGui.QPushButton(self.centralwidget)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.assRefresh.sizePolicy().hasHeightForWidth())
    self.assRefresh.setSizePolicy(sizePolicy)
    self.assRefresh.setText(_fromUtf8(""))
    self.assRefresh.setObjectName(_fromUtf8("assRefresh"))
    self.gridLayout.addWidget(self.assRefresh, 8, 4, 1, 1)
    self.line = QtGui.QFrame(self.centralwidget)
    self.line.setEnabled(True)
    self.line.setFrameShadow(QtGui.QFrame.Sunken)
    self.line.setLineWidth(1)
    self.line.setMidLineWidth(3)
    self.line.setFrameShape(QtGui.QFrame.HLine)
    self.line.setFrameShadow(QtGui.QFrame.Sunken)
    self.line.setObjectName(_fromUtf8("line"))
    self.gridLayout.addWidget(self.line, 7, 0, 1, 5)
    self.groupBox = QtGui.QGroupBox(self.centralwidget)
    self.groupBox.setTitle(_fromUtf8(""))
    self.groupBox.setObjectName(_fromUtf8("groupBox"))
    self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
    self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
    self.comboSequence = QtGui.QComboBox(self.groupBox)
    self.comboSequence.setObjectName(_fromUtf8("comboSequence"))
    self.gridLayout_2.addWidget(self.comboSequence, 3, 2, 1, 1)
    self.labelSeq = QtGui.QLabel(self.groupBox)
    self.labelSeq.setObjectName(_fromUtf8("labelSeq"))
    self.gridLayout_2.addWidget(self.labelSeq, 2, 2, 1, 1)
    self.label = QtGui.QLabel(self.groupBox)
    self.label.setObjectName(_fromUtf8("label"))
    self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
    self.comboStageType = QtGui.QComboBox(self.groupBox)
    self.comboStageType.setObjectName(_fromUtf8("comboStageType"))
    self.gridLayout_2.addWidget(self.comboStageType, 3, 0, 1, 1)
    self.comboScene = QtGui.QComboBox(self.groupBox)
    self.comboScene.setObjectName(_fromUtf8("comboScene"))
    self.gridLayout_2.addWidget(self.comboScene, 3, 3, 1, 1)
    self.labelFileType = QtGui.QLabel(self.groupBox)
    self.labelFileType.setObjectName(_fromUtf8("labelFileType"))
    self.gridLayout_2.addWidget(self.labelFileType, 2, 4, 1, 1)
    self.comboFileType = QtGui.QComboBox(self.groupBox)
    self.comboFileType.setObjectName(_fromUtf8("comboFileType"))
    self.gridLayout_2.addWidget(self.comboFileType, 3, 4, 1, 1)
    self.label_2 = QtGui.QLabel(self.groupBox)
    self.label_2.setObjectName(_fromUtf8("label_2"))
    self.gridLayout_2.addWidget(self.label_2, 2, 1, 1, 1)
    self.comboNodeType = QtGui.QComboBox(self.groupBox)
    self.comboNodeType.setObjectName(_fromUtf8("comboNodeType"))
    self.gridLayout_2.addWidget(self.comboNodeType, 3, 1, 1, 1)
    self.labelSce = QtGui.QLabel(self.groupBox)
    self.labelSce.setObjectName(_fromUtf8("labelSce"))
    self.gridLayout_2.addWidget(self.labelSce, 2, 3, 1, 1)
    self.comboAssType = QtGui.QComboBox(self.groupBox)
    self.comboAssType.setObjectName(_fromUtf8("comboAssType"))
    self.gridLayout_2.addWidget(self.comboAssType, 3, 5, 1, 1)
    self.labelAssType = QtGui.QLabel(self.groupBox)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.labelAssType.sizePolicy().hasHeightForWidth())
    self.labelAssType.setSizePolicy(sizePolicy)
    self.labelAssType.setObjectName(_fromUtf8("labelAssType"))
    self.gridLayout_2.addWidget(self.labelAssType, 2, 5, 1, 1)
    self.gridLayout.addWidget(self.groupBox, 2, 0, 1, 5)
    self.horizontalLayout = QtGui.QHBoxLayout()
    self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
    self.pushNewAsset = QtGui.QPushButton(self.centralwidget)
    self.pushNewAsset.setObjectName(_fromUtf8("pushNewAsset"))
    self.horizontalLayout.addWidget(self.pushNewAsset)
    self.radioButton_2 = QtGui.QRadioButton(self.centralwidget)
    self.radioButton_2.setChecked(True)
    self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
    self.horizontalLayout.addWidget(self.radioButton_2)
    self.radioButton = QtGui.QRadioButton(self.centralwidget)
    self.radioButton.setObjectName(_fromUtf8("radioButton"))
    self.horizontalLayout.addWidget(self.radioButton)
    spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.horizontalLayout.addItem(spacerItem1)
    self.lineEdit = QtGui.QLineEdit(self.centralwidget)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
    self.lineEdit.setSizePolicy(sizePolicy)
    self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
    self.horizontalLayout.addWidget(self.lineEdit)
    self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 5)
    self.checkRefresh = QtGui.QCheckBox(self.centralwidget)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.checkRefresh.sizePolicy().hasHeightForWidth())
    self.checkRefresh.setSizePolicy(sizePolicy)
    self.checkRefresh.setText(_fromUtf8(""))
    self.checkRefresh.setIconSize(QtCore.QSize(20, 20))
    self.checkRefresh.setObjectName(_fromUtf8("checkRefresh"))
    self.gridLayout.addWidget(self.checkRefresh, 8, 3, 1, 1)
    self.pushLogout = QtGui.QPushButton(self.centralwidget)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.pushLogout.sizePolicy().hasHeightForWidth())
    self.pushLogout.setSizePolicy(sizePolicy)
    self.pushLogout.setObjectName(_fromUtf8("pushLogout"))
    self.gridLayout.addWidget(self.pushLogout, 8, 0, 1, 1)
    self.listWidget = QtGui.QListWidget(self.centralwidget)
    self.listWidget.setAlternatingRowColors(True)
    self.listWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
    self.listWidget.setObjectName(_fromUtf8("listWidget"))
    self.gridLayout.addWidget(self.listWidget, 5, 0, 1, 5)
    MainWindow.setCentralWidget(self.centralwidget)
    self.menuBar = QtGui.QMenuBar(MainWindow)
    self.menuBar.setGeometry(QtCore.QRect(0, 0, 667, 21))
    self.menuBar.setObjectName(_fromUtf8("menuBar"))
    self.menuAdmin = QtGui.QMenu(self.menuBar)
    self.menuAdmin.setObjectName(_fromUtf8("menuAdmin"))
    self.menuProject = QtGui.QMenu(self.menuBar)
    self.menuProject.setObjectName(_fromUtf8("menuProject"))
    self.menuDebug = QtGui.QMenu(self.menuBar)
    self.menuDebug.setObjectName(_fromUtf8("menuDebug"))
    MainWindow.setMenuBar(self.menuBar)
    self.actionMine = QtGui.QAction(MainWindow)
    self.actionMine.setObjectName(_fromUtf8("actionMine"))
    self.actionAll = QtGui.QAction(MainWindow)
    self.actionAll.setObjectName(_fromUtf8("actionAll"))
    self.actionSet_project = QtGui.QAction(MainWindow)
    self.actionSet_project.setObjectName(_fromUtf8("actionSet_project"))
    self.actionTask_trak = QtGui.QAction(MainWindow)
    self.actionTask_trak.setObjectName(_fromUtf8("actionTask_trak"))
    self.actionNew_project = QtGui.QAction(MainWindow)
    self.actionNew_project.setObjectName(_fromUtf8("actionNew_project"))
    self.actionList_env = QtGui.QAction(MainWindow)
    self.actionList_env.setObjectName(_fromUtf8("actionList_env"))
    self.actionNew_seq_scn = QtGui.QAction(MainWindow)
    self.actionNew_seq_scn.setObjectName(_fromUtf8("actionNew_seq_scn"))
    self.menuAdmin.addAction(self.actionTask_trak)
    self.menuAdmin.addAction(self.actionNew_seq_scn)
    self.menuProject.addAction(self.actionSet_project)
    self.menuProject.addAction(self.actionNew_project)
    self.menuDebug.addAction(self.actionList_env)
    self.menuBar.addAction(self.menuProject.menuAction())
    self.menuBar.addAction(self.menuAdmin.menuAction())
    self.menuBar.addAction(self.menuDebug.menuAction())

    self.retranslateUi(MainWindow)
    QtCore.QMetaObject.connectSlotsByName(MainWindow)

  def retranslateUi(self, MainWindow):
    MainWindow.setWindowTitle(_translate("MainWindow", "Rbhus Production Management", None))
    self.labelSeq.setText(_translate("MainWindow", "sequence", None))
    self.label.setText(_translate("MainWindow", "stageType", None))
    self.labelFileType.setText(_translate("MainWindow", "fileType", None))
    self.label_2.setText(_translate("MainWindow", "nodeType", None))
    self.labelSce.setText(_translate("MainWindow", "scene", None))
    self.labelAssType.setText(_translate("MainWindow", "assetType", None))
    self.pushNewAsset.setText(_translate("MainWindow", "new", None))
    self.radioButton_2.setText(_translate("MainWindow", "mine", None))
    self.radioButton.setText(_translate("MainWindow", "all", None))
    self.lineEdit.setPlaceholderText(_translate("MainWindow", "search", None))
    self.pushLogout.setText(_translate("MainWindow", "logout", None))
    self.listWidget.setSortingEnabled(True)
    self.menuAdmin.setTitle(_translate("MainWindow", "admin", None))
    self.menuProject.setTitle(_translate("MainWindow", "project", None))
    self.menuDebug.setTitle(_translate("MainWindow", "debug", None))
    self.actionMine.setText(_translate("MainWindow", "mine", None))
    self.actionAll.setText(_translate("MainWindow", "all", None))
    self.actionSet_project.setText(_translate("MainWindow", "set project", None))
    self.actionTask_trak.setText(_translate("MainWindow", "trak", None))
    self.actionNew_project.setText(_translate("MainWindow", "new project", None))
    self.actionList_env.setText(_translate("MainWindow", "list env", None))
    self.actionNew_seq_scn.setText(_translate("MainWindow", "new seq/scn", None))

