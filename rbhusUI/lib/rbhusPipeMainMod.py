# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rbhusPipeMainMod.ui'
#
# Created: Tue Nov 11 23:46:42 2014
#      by: PyQt4 UI code generator 4.11.2
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
    MainWindow.setWindowModality(QtCore.Qt.WindowModal)
    MainWindow.resize(931, 612)
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
    self.line = QtGui.QFrame(self.centralwidget)
    self.line.setEnabled(True)
    self.line.setFrameShadow(QtGui.QFrame.Sunken)
    self.line.setLineWidth(1)
    self.line.setMidLineWidth(3)
    self.line.setFrameShape(QtGui.QFrame.HLine)
    self.line.setFrameShadow(QtGui.QFrame.Sunken)
    self.line.setObjectName(_fromUtf8("line"))
    self.gridLayout.addWidget(self.line, 12, 0, 1, 5)
    self.assRefresh = QtGui.QPushButton(self.centralwidget)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.assRefresh.sizePolicy().hasHeightForWidth())
    self.assRefresh.setSizePolicy(sizePolicy)
    self.assRefresh.setText(_fromUtf8(""))
    self.assRefresh.setObjectName(_fromUtf8("assRefresh"))
    self.gridLayout.addWidget(self.assRefresh, 13, 4, 1, 1)
    self.tableWidget = QtGui.QTableWidget(self.centralwidget)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
    self.tableWidget.setSizePolicy(sizePolicy)
    palette = QtGui.QPalette()
    brush = QtGui.QBrush(QtGui.QColor(176, 176, 176))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
    brush = QtGui.QBrush(QtGui.QColor(176, 176, 176))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
    brush = QtGui.QBrush(QtGui.QColor(244, 244, 244))
    brush.setStyle(QtCore.Qt.SolidPattern)
    palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
    self.tableWidget.setPalette(palette)
    self.tableWidget.setAutoFillBackground(False)
    self.tableWidget.setFrameShape(QtGui.QFrame.StyledPanel)
    self.tableWidget.setFrameShadow(QtGui.QFrame.Raised)
    self.tableWidget.setMidLineWidth(1)
    self.tableWidget.setDragDropMode(QtGui.QAbstractItemView.NoDragDrop)
    self.tableWidget.setAlternatingRowColors(False)
    self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
    self.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
    self.tableWidget.setWordWrap(False)
    self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
    self.tableWidget.setColumnCount(0)
    self.tableWidget.setRowCount(0)
    self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
    self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
    self.tableWidget.horizontalHeader().setStretchLastSection(True)
    self.tableWidget.verticalHeader().setVisible(False)
    self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
    self.tableWidget.verticalHeader().setDefaultSectionSize(32)
    self.tableWidget.verticalHeader().setHighlightSections(True)
    self.tableWidget.verticalHeader().setSortIndicatorShown(True)
    self.gridLayout.addWidget(self.tableWidget, 10, 0, 1, 5)
    self.checkBoxFilter = QtGui.QCheckBox(self.centralwidget)
    self.checkBoxFilter.setObjectName(_fromUtf8("checkBoxFilter"))
    self.gridLayout.addWidget(self.checkBoxFilter, 1, 0, 1, 1)
    self.groupBoxFilter = QtGui.QGroupBox(self.centralwidget)
    self.groupBoxFilter.setEnabled(True)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.groupBoxFilter.sizePolicy().hasHeightForWidth())
    self.groupBoxFilter.setSizePolicy(sizePolicy)
    self.groupBoxFilter.setTitle(_fromUtf8(""))
    self.groupBoxFilter.setAlignment(QtCore.Qt.AlignCenter)
    self.groupBoxFilter.setFlat(False)
    self.groupBoxFilter.setCheckable(False)
    self.groupBoxFilter.setChecked(False)
    self.groupBoxFilter.setObjectName(_fromUtf8("groupBoxFilter"))
    self.gridLayout_2 = QtGui.QGridLayout(self.groupBoxFilter)
    self.gridLayout_2.setMargin(1)
    self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
    self.comboNodeType = QtGui.QComboBox(self.groupBoxFilter)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.comboNodeType.sizePolicy().hasHeightForWidth())
    self.comboNodeType.setSizePolicy(sizePolicy)
    self.comboNodeType.setEditable(True)
    self.comboNodeType.setInsertPolicy(QtGui.QComboBox.InsertAlphabetically)
    self.comboNodeType.setObjectName(_fromUtf8("comboNodeType"))
    self.gridLayout_2.addWidget(self.comboNodeType, 6, 3, 1, 1)
    self.comboScene = QtGui.QComboBox(self.groupBoxFilter)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.comboScene.sizePolicy().hasHeightForWidth())
    self.comboScene.setSizePolicy(sizePolicy)
    self.comboScene.setEditable(True)
    self.comboScene.setInsertPolicy(QtGui.QComboBox.InsertAlphabetically)
    self.comboScene.setObjectName(_fromUtf8("comboScene"))
    self.gridLayout_2.addWidget(self.comboScene, 4, 3, 1, 1)
    self.label_2 = QtGui.QLabel(self.groupBoxFilter)
    self.label_2.setObjectName(_fromUtf8("label_2"))
    self.gridLayout_2.addWidget(self.label_2, 5, 3, 1, 1)
    self.labelAssType = QtGui.QLabel(self.groupBoxFilter)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.labelAssType.sizePolicy().hasHeightForWidth())
    self.labelAssType.setSizePolicy(sizePolicy)
    self.labelAssType.setObjectName(_fromUtf8("labelAssType"))
    self.gridLayout_2.addWidget(self.labelAssType, 1, 1, 1, 1)
    self.comboStageType = QtGui.QComboBox(self.groupBoxFilter)
    self.comboStageType.setEnabled(True)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.comboStageType.sizePolicy().hasHeightForWidth())
    self.comboStageType.setSizePolicy(sizePolicy)
    self.comboStageType.setEditable(True)
    self.comboStageType.setInsertPolicy(QtGui.QComboBox.InsertAlphabetically)
    self.comboStageType.setFrame(True)
    self.comboStageType.setObjectName(_fromUtf8("comboStageType"))
    self.gridLayout_2.addWidget(self.comboStageType, 6, 1, 1, 1)
    self.label = QtGui.QLabel(self.groupBoxFilter)
    self.label.setObjectName(_fromUtf8("label"))
    self.gridLayout_2.addWidget(self.label, 5, 1, 1, 1)
    self.comboFileType = QtGui.QComboBox(self.groupBoxFilter)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.comboFileType.sizePolicy().hasHeightForWidth())
    self.comboFileType.setSizePolicy(sizePolicy)
    self.comboFileType.setEditable(True)
    self.comboFileType.setInsertPolicy(QtGui.QComboBox.InsertAlphabetically)
    self.comboFileType.setDuplicatesEnabled(False)
    self.comboFileType.setFrame(True)
    self.comboFileType.setObjectName(_fromUtf8("comboFileType"))
    self.gridLayout_2.addWidget(self.comboFileType, 6, 5, 1, 1)
    self.labelSce = QtGui.QLabel(self.groupBoxFilter)
    self.labelSce.setObjectName(_fromUtf8("labelSce"))
    self.gridLayout_2.addWidget(self.labelSce, 3, 3, 1, 1)
    self.comboSequence = QtGui.QComboBox(self.groupBoxFilter)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.comboSequence.sizePolicy().hasHeightForWidth())
    self.comboSequence.setSizePolicy(sizePolicy)
    self.comboSequence.setEditable(True)
    self.comboSequence.setInsertPolicy(QtGui.QComboBox.InsertAlphabetically)
    self.comboSequence.setObjectName(_fromUtf8("comboSequence"))
    self.gridLayout_2.addWidget(self.comboSequence, 4, 1, 1, 1)
    self.labelSeq = QtGui.QLabel(self.groupBoxFilter)
    self.labelSeq.setObjectName(_fromUtf8("labelSeq"))
    self.gridLayout_2.addWidget(self.labelSeq, 3, 1, 1, 1)
    self.labelFileType = QtGui.QLabel(self.groupBoxFilter)
    self.labelFileType.setObjectName(_fromUtf8("labelFileType"))
    self.gridLayout_2.addWidget(self.labelFileType, 5, 5, 1, 1)
    self.pushResetScene = QtGui.QPushButton(self.groupBoxFilter)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.pushResetScene.sizePolicy().hasHeightForWidth())
    self.pushResetScene.setSizePolicy(sizePolicy)
    self.pushResetScene.setText(_fromUtf8(""))
    self.pushResetScene.setFlat(True)
    self.pushResetScene.setObjectName(_fromUtf8("pushResetScene"))
    self.gridLayout_2.addWidget(self.pushResetScene, 4, 4, 1, 1)
    self.comboAssType = QtGui.QComboBox(self.groupBoxFilter)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.comboAssType.sizePolicy().hasHeightForWidth())
    self.comboAssType.setSizePolicy(sizePolicy)
    self.comboAssType.setEditable(True)
    self.comboAssType.setInsertPolicy(QtGui.QComboBox.InsertAlphabetically)
    self.comboAssType.setObjectName(_fromUtf8("comboAssType"))
    self.gridLayout_2.addWidget(self.comboAssType, 2, 1, 1, 1)
    self.pushResetSeq = QtGui.QPushButton(self.groupBoxFilter)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.pushResetSeq.sizePolicy().hasHeightForWidth())
    self.pushResetSeq.setSizePolicy(sizePolicy)
    self.pushResetSeq.setText(_fromUtf8(""))
    self.pushResetSeq.setFlat(True)
    self.pushResetSeq.setObjectName(_fromUtf8("pushResetSeq"))
    self.gridLayout_2.addWidget(self.pushResetSeq, 4, 2, 1, 1)
    self.pushResetAsset = QtGui.QPushButton(self.groupBoxFilter)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.pushResetAsset.sizePolicy().hasHeightForWidth())
    self.pushResetAsset.setSizePolicy(sizePolicy)
    self.pushResetAsset.setFlat(True)
    self.pushResetAsset.setObjectName(_fromUtf8("pushResetAsset"))
    self.gridLayout_2.addWidget(self.pushResetAsset, 2, 2, 1, 1)
    self.pushResetStage = QtGui.QPushButton(self.groupBoxFilter)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.pushResetStage.sizePolicy().hasHeightForWidth())
    self.pushResetStage.setSizePolicy(sizePolicy)
    self.pushResetStage.setText(_fromUtf8(""))
    self.pushResetStage.setFlat(True)
    self.pushResetStage.setObjectName(_fromUtf8("pushResetStage"))
    self.gridLayout_2.addWidget(self.pushResetStage, 6, 2, 1, 1)
    self.pushResetNode = QtGui.QPushButton(self.groupBoxFilter)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.pushResetNode.sizePolicy().hasHeightForWidth())
    self.pushResetNode.setSizePolicy(sizePolicy)
    self.pushResetNode.setText(_fromUtf8(""))
    self.pushResetNode.setFlat(True)
    self.pushResetNode.setObjectName(_fromUtf8("pushResetNode"))
    self.gridLayout_2.addWidget(self.pushResetNode, 6, 4, 1, 1)
    self.pushResetFile = QtGui.QPushButton(self.groupBoxFilter)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.pushResetFile.sizePolicy().hasHeightForWidth())
    self.pushResetFile.setSizePolicy(sizePolicy)
    self.pushResetFile.setText(_fromUtf8(""))
    self.pushResetFile.setFlat(True)
    self.pushResetFile.setObjectName(_fromUtf8("pushResetFile"))
    self.gridLayout_2.addWidget(self.pushResetFile, 6, 6, 1, 1)
    self.horizontalLayout_2 = QtGui.QHBoxLayout()
    self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
    self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
    spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
    self.horizontalLayout_2.addItem(spacerItem)
    self.filterRefresh = QtGui.QPushButton(self.groupBoxFilter)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.filterRefresh.sizePolicy().hasHeightForWidth())
    self.filterRefresh.setSizePolicy(sizePolicy)
    self.filterRefresh.setText(_fromUtf8(""))
    self.filterRefresh.setObjectName(_fromUtf8("filterRefresh"))
    self.horizontalLayout_2.addWidget(self.filterRefresh)
    self.gridLayout_2.addLayout(self.horizontalLayout_2, 7, 5, 1, 2)
    self.gridLayout.addWidget(self.groupBoxFilter, 1, 1, 1, 4)
    self.horizontalLayout = QtGui.QHBoxLayout()
    self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
    self.pushNewAsset = QtGui.QPushButton(self.centralwidget)
    self.pushNewAsset.setObjectName(_fromUtf8("pushNewAsset"))
    self.horizontalLayout.addWidget(self.pushNewAsset)
    self.radioMineAss = QtGui.QRadioButton(self.centralwidget)
    self.radioMineAss.setChecked(True)
    self.radioMineAss.setObjectName(_fromUtf8("radioMineAss"))
    self.horizontalLayout.addWidget(self.radioMineAss)
    self.radioAllAss = QtGui.QRadioButton(self.centralwidget)
    self.radioAllAss.setObjectName(_fromUtf8("radioAllAss"))
    self.horizontalLayout.addWidget(self.radioAllAss)
    spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.horizontalLayout.addItem(spacerItem1)
    self.groupBox = QtGui.QGroupBox(self.centralwidget)
    self.groupBox.setTitle(_fromUtf8(""))
    self.groupBox.setObjectName(_fromUtf8("groupBox"))
    self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
    self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
    self.lineEditSearch = QtGui.QLineEdit(self.groupBox)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.lineEditSearch.sizePolicy().hasHeightForWidth())
    self.lineEditSearch.setSizePolicy(sizePolicy)
    self.lineEditSearch.setObjectName(_fromUtf8("lineEditSearch"))
    self.verticalLayout.addWidget(self.lineEditSearch)
    self.horizontalLayout_3 = QtGui.QHBoxLayout()
    self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
    self.checkCase = QtGui.QCheckBox(self.groupBox)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.checkCase.sizePolicy().hasHeightForWidth())
    self.checkCase.setSizePolicy(sizePolicy)
    self.checkCase.setChecked(True)
    self.checkCase.setTristate(False)
    self.checkCase.setObjectName(_fromUtf8("checkCase"))
    self.horizontalLayout_3.addWidget(self.checkCase)
    self.line_2 = QtGui.QFrame(self.groupBox)
    self.line_2.setFrameShape(QtGui.QFrame.VLine)
    self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
    self.line_2.setObjectName(_fromUtf8("line_2"))
    self.horizontalLayout_3.addWidget(self.line_2)
    self.checkWords = QtGui.QCheckBox(self.groupBox)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.checkWords.sizePolicy().hasHeightForWidth())
    self.checkWords.setSizePolicy(sizePolicy)
    self.checkWords.setObjectName(_fromUtf8("checkWords"))
    self.horizontalLayout_3.addWidget(self.checkWords)
    self.checkTags = QtGui.QCheckBox(self.groupBox)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.checkTags.sizePolicy().hasHeightForWidth())
    self.checkTags.setSizePolicy(sizePolicy)
    self.checkTags.setObjectName(_fromUtf8("checkTags"))
    self.horizontalLayout_3.addWidget(self.checkTags)
    self.verticalLayout.addLayout(self.horizontalLayout_3)
    self.horizontalLayout.addWidget(self.groupBox)
    self.gridLayout.addLayout(self.horizontalLayout, 9, 0, 1, 5)
    spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.gridLayout.addItem(spacerItem2, 13, 1, 1, 2)
    self.pushLogout = QtGui.QPushButton(self.centralwidget)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.pushLogout.sizePolicy().hasHeightForWidth())
    self.pushLogout.setSizePolicy(sizePolicy)
    self.pushLogout.setObjectName(_fromUtf8("pushLogout"))
    self.gridLayout.addWidget(self.pushLogout, 13, 0, 1, 1)
    self.checkRefresh = QtGui.QCheckBox(self.centralwidget)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.checkRefresh.sizePolicy().hasHeightForWidth())
    self.checkRefresh.setSizePolicy(sizePolicy)
    self.checkRefresh.setText(_fromUtf8(""))
    self.checkRefresh.setIconSize(QtCore.QSize(20, 20))
    self.checkRefresh.setObjectName(_fromUtf8("checkRefresh"))
    self.gridLayout.addWidget(self.checkRefresh, 13, 3, 1, 1)
    MainWindow.setCentralWidget(self.centralwidget)
    self.menuBar = QtGui.QMenuBar(MainWindow)
    self.menuBar.setGeometry(QtCore.QRect(0, 0, 931, 21))
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
    self.actionEdit_project = QtGui.QAction(MainWindow)
    self.actionEdit_project.setObjectName(_fromUtf8("actionEdit_project"))
    self.menuAdmin.addAction(self.actionTask_trak)
    self.menuAdmin.addAction(self.actionNew_seq_scn)
    self.menuProject.addAction(self.actionSet_project)
    self.menuProject.addAction(self.actionNew_project)
    self.menuProject.addAction(self.actionEdit_project)
    self.menuDebug.addAction(self.actionList_env)
    self.menuBar.addAction(self.menuProject.menuAction())
    self.menuBar.addAction(self.menuAdmin.menuAction())
    self.menuBar.addAction(self.menuDebug.menuAction())

    self.retranslateUi(MainWindow)
    QtCore.QMetaObject.connectSlotsByName(MainWindow)

  def retranslateUi(self, MainWindow):
    MainWindow.setWindowTitle(_translate("MainWindow", "Rbhus Production Management", None))
    self.tableWidget.setSortingEnabled(True)
    self.checkBoxFilter.setText(_translate("MainWindow", "filters", None))
    self.label_2.setText(_translate("MainWindow", "nodeType", None))
    self.labelAssType.setText(_translate("MainWindow", "assetType", None))
    self.label.setText(_translate("MainWindow", "stageType", None))
    self.labelSce.setText(_translate("MainWindow", "scene", None))
    self.labelSeq.setText(_translate("MainWindow", "sequence", None))
    self.labelFileType.setText(_translate("MainWindow", "fileType", None))
    self.pushNewAsset.setText(_translate("MainWindow", "new", None))
    self.radioMineAss.setText(_translate("MainWindow", "mine", None))
    self.radioAllAss.setText(_translate("MainWindow", "all", None))
    self.lineEditSearch.setPlaceholderText(_translate("MainWindow", "search", None))
    self.checkCase.setText(_translate("MainWindow", "ignore case", None))
    self.checkWords.setText(_translate("MainWindow", "whole words", None))
    self.checkTags.setText(_translate("MainWindow", "tags", None))
    self.pushLogout.setText(_translate("MainWindow", "logout", None))
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
    self.actionEdit_project.setText(_translate("MainWindow", "edit project", None))

