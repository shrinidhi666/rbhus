# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rbhusListMod.ui'
#
# Created: Wed Oct 16 13:37:27 2013
#      by: PyQt4 UI code generator 4.10.2
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

class Ui_mainRbhusList(object):
  def setupUi(self, mainRbhusList):
    mainRbhusList.setObjectName(_fromUtf8("mainRbhusList"))
    mainRbhusList.setWindowModality(QtCore.Qt.WindowModal)
    mainRbhusList.resize(1084, 707)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(mainRbhusList.sizePolicy().hasHeightForWidth())
    mainRbhusList.setSizePolicy(sizePolicy)
    mainRbhusList.setLayoutDirection(QtCore.Qt.LeftToRight)
    mainRbhusList.setAutoFillBackground(False)
    mainRbhusList.setDocumentMode(True)
    mainRbhusList.setDockNestingEnabled(True)
    self.centralwidget = QtGui.QWidget(mainRbhusList)
    self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
    self.verticalLayout_5 = QtGui.QVBoxLayout(self.centralwidget)
    self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
    self.dockWidgetTasks = QtGui.QDockWidget(self.centralwidget)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.dockWidgetTasks.sizePolicy().hasHeightForWidth())
    self.dockWidgetTasks.setSizePolicy(sizePolicy)
    self.dockWidgetTasks.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)
    self.dockWidgetTasks.setObjectName(_fromUtf8("dockWidgetTasks"))
    self.dockWidgetContents_2 = QtGui.QWidget()
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.dockWidgetContents_2.sizePolicy().hasHeightForWidth())
    self.dockWidgetContents_2.setSizePolicy(sizePolicy)
    self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
    self.verticalLayout_3 = QtGui.QVBoxLayout(self.dockWidgetContents_2)
    self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
    self.horizontalLayout_12 = QtGui.QHBoxLayout()
    self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
    self.label = QtGui.QLabel(self.dockWidgetContents_2)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
    self.label.setSizePolicy(sizePolicy)
    font = QtGui.QFont()
    font.setBold(True)
    font.setWeight(75)
    self.label.setFont(font)
    self.label.setObjectName(_fromUtf8("label"))
    self.horizontalLayout_12.addWidget(self.label)
    self.labelUser = QtGui.QLabel(self.dockWidgetContents_2)
    font = QtGui.QFont()
    font.setPointSize(10)
    font.setBold(True)
    font.setUnderline(False)
    font.setWeight(75)
    self.labelUser.setFont(font)
    self.labelUser.setObjectName(_fromUtf8("labelUser"))
    self.horizontalLayout_12.addWidget(self.labelUser)
    self.verticalLayout_3.addLayout(self.horizontalLayout_12)
    self.horizontalLayout_3 = QtGui.QHBoxLayout()
    self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
    self.labelTask = QtGui.QLabel(self.dockWidgetContents_2)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.labelTask.sizePolicy().hasHeightForWidth())
    self.labelTask.setSizePolicy(sizePolicy)
    font = QtGui.QFont()
    font.setBold(True)
    font.setWeight(75)
    font.setStyleStrategy(QtGui.QFont.PreferAntialias)
    self.labelTask.setFont(font)
    self.labelTask.setObjectName(_fromUtf8("labelTask"))
    self.horizontalLayout_3.addWidget(self.labelTask)
    self.groupBox_3 = QtGui.QGroupBox(self.dockWidgetContents_2)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
    self.groupBox_3.setSizePolicy(sizePolicy)
    self.groupBox_3.setTitle(_fromUtf8(""))
    self.groupBox_3.setFlat(False)
    self.groupBox_3.setCheckable(False)
    self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
    self.gridLayout_9 = QtGui.QGridLayout(self.groupBox_3)
    self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
    self.checkTHold = QtGui.QCheckBox(self.groupBox_3)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.checkTHold.sizePolicy().hasHeightForWidth())
    self.checkTHold.setSizePolicy(sizePolicy)
    self.checkTHold.setObjectName(_fromUtf8("checkTHold"))
    self.gridLayout_9.addWidget(self.checkTHold, 0, 3, 1, 1)
    self.checkTDone = QtGui.QCheckBox(self.groupBox_3)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.checkTDone.sizePolicy().hasHeightForWidth())
    self.checkTDone.setSizePolicy(sizePolicy)
    self.checkTDone.setObjectName(_fromUtf8("checkTDone"))
    self.gridLayout_9.addWidget(self.checkTDone, 0, 1, 1, 1)
    self.checkTActive = QtGui.QCheckBox(self.groupBox_3)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.checkTActive.sizePolicy().hasHeightForWidth())
    self.checkTActive.setSizePolicy(sizePolicy)
    self.checkTActive.setObjectName(_fromUtf8("checkTActive"))
    self.gridLayout_9.addWidget(self.checkTActive, 0, 0, 1, 1)
    self.checkTAutohold = QtGui.QCheckBox(self.groupBox_3)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.checkTAutohold.sizePolicy().hasHeightForWidth())
    self.checkTAutohold.setSizePolicy(sizePolicy)
    self.checkTAutohold.setObjectName(_fromUtf8("checkTAutohold"))
    self.gridLayout_9.addWidget(self.checkTAutohold, 0, 2, 1, 1)
    self.checkTAll = QtGui.QCheckBox(self.groupBox_3)
    font = QtGui.QFont()
    font.setBold(True)
    font.setWeight(75)
    self.checkTAll.setFont(font)
    self.checkTAll.setObjectName(_fromUtf8("checkTAll"))
    self.gridLayout_9.addWidget(self.checkTAll, 0, 4, 1, 1)
    self.horizontalLayout_3.addWidget(self.groupBox_3)
    spacerItem = QtGui.QSpacerItem(630, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.horizontalLayout_3.addItem(spacerItem)
    self.groupBox = QtGui.QGroupBox(self.dockWidgetContents_2)
    self.groupBox.setTitle(_fromUtf8(""))
    self.groupBox.setObjectName(_fromUtf8("groupBox"))
    self.horizontalLayout_10 = QtGui.QHBoxLayout(self.groupBox)
    self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
    self.checkTMine = QtGui.QCheckBox(self.groupBox)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.checkTMine.sizePolicy().hasHeightForWidth())
    self.checkTMine.setSizePolicy(sizePolicy)
    self.checkTMine.setObjectName(_fromUtf8("checkTMine"))
    self.horizontalLayout_10.addWidget(self.checkTMine)
    self.horizontalLayout_3.addWidget(self.groupBox)
    self.verticalLayout_3.addLayout(self.horizontalLayout_3)
    self.frame_6 = QtGui.QFrame(self.dockWidgetContents_2)
    self.frame_6.setObjectName(_fromUtf8("frame_6"))
    self.horizontalLayout_9 = QtGui.QHBoxLayout(self.frame_6)
    self.horizontalLayout_9.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
    self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
    self.verticalLayout_12 = QtGui.QVBoxLayout()
    self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
    self.horizontalLayout_11 = QtGui.QHBoxLayout()
    self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
    self.labelSearch = QtGui.QLabel(self.frame_6)
    self.labelSearch.setObjectName(_fromUtf8("labelSearch"))
    self.horizontalLayout_11.addWidget(self.labelSearch)
    self.lineEditSearch = QtGui.QLineEdit(self.frame_6)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.lineEditSearch.sizePolicy().hasHeightForWidth())
    self.lineEditSearch.setSizePolicy(sizePolicy)
    self.lineEditSearch.setObjectName(_fromUtf8("lineEditSearch"))
    self.horizontalLayout_11.addWidget(self.lineEditSearch)
    spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
    self.horizontalLayout_11.addItem(spacerItem1)
    self.label_2 = QtGui.QLabel(self.frame_6)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
    self.label_2.setSizePolicy(sizePolicy)
    self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.label_2.setObjectName(_fromUtf8("label_2"))
    self.horizontalLayout_11.addWidget(self.label_2)
    self.labelTaskTotal = QtGui.QLabel(self.frame_6)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.labelTaskTotal.sizePolicy().hasHeightForWidth())
    self.labelTaskTotal.setSizePolicy(sizePolicy)
    self.labelTaskTotal.setLayoutDirection(QtCore.Qt.LeftToRight)
    self.labelTaskTotal.setAutoFillBackground(True)
    self.labelTaskTotal.setFrameShape(QtGui.QFrame.WinPanel)
    self.labelTaskTotal.setFrameShadow(QtGui.QFrame.Sunken)
    self.labelTaskTotal.setTextFormat(QtCore.Qt.PlainText)
    self.labelTaskTotal.setScaledContents(False)
    self.labelTaskTotal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.labelTaskTotal.setMargin(2)
    self.labelTaskTotal.setObjectName(_fromUtf8("labelTaskTotal"))
    self.horizontalLayout_11.addWidget(self.labelTaskTotal)
    self.verticalLayout_12.addLayout(self.horizontalLayout_11)
    self.tableList = QtGui.QTableWidget(self.frame_6)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.tableList.sizePolicy().hasHeightForWidth())
    self.tableList.setSizePolicy(sizePolicy)
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
    self.tableList.setPalette(palette)
    self.tableList.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    self.tableList.setFrameShadow(QtGui.QFrame.Raised)
    self.tableList.setEditTriggers(QtGui.QAbstractItemView.DoubleClicked)
    self.tableList.setAlternatingRowColors(False)
    self.tableList.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
    self.tableList.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
    self.tableList.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
    self.tableList.setGridStyle(QtCore.Qt.SolidLine)
    self.tableList.setWordWrap(False)
    self.tableList.setObjectName(_fromUtf8("tableList"))
    self.tableList.setColumnCount(0)
    self.tableList.setRowCount(0)
    self.tableList.horizontalHeader().setCascadingSectionResizes(True)
    self.tableList.horizontalHeader().setStretchLastSection(True)
    self.tableList.verticalHeader().setVisible(False)
    self.tableList.verticalHeader().setCascadingSectionResizes(True)
    self.verticalLayout_12.addWidget(self.tableList)
    self.horizontalLayout_5 = QtGui.QHBoxLayout()
    self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
    spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.horizontalLayout_5.addItem(spacerItem2)
    self.taskRefresh = QtGui.QPushButton(self.frame_6)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.taskRefresh.sizePolicy().hasHeightForWidth())
    self.taskRefresh.setSizePolicy(sizePolicy)
    self.taskRefresh.setFlat(False)
    self.taskRefresh.setObjectName(_fromUtf8("taskRefresh"))
    self.horizontalLayout_5.addWidget(self.taskRefresh)
    self.verticalLayout_12.addLayout(self.horizontalLayout_5)
    self.horizontalLayout_9.addLayout(self.verticalLayout_12)
    self.verticalLayout_3.addWidget(self.frame_6)
    self.dockWidgetTasks.setWidget(self.dockWidgetContents_2)
    self.verticalLayout_5.addWidget(self.dockWidgetTasks)
    mainRbhusList.setCentralWidget(self.centralwidget)
    self.dockWidgetFrames = QtGui.QDockWidget(mainRbhusList)
    self.dockWidgetFrames.setEnabled(True)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.dockWidgetFrames.sizePolicy().hasHeightForWidth())
    self.dockWidgetFrames.setSizePolicy(sizePolicy)
    self.dockWidgetFrames.setMouseTracking(True)
    self.dockWidgetFrames.setFocusPolicy(QtCore.Qt.ClickFocus)
    self.dockWidgetFrames.setAcceptDrops(False)
    self.dockWidgetFrames.setStatusTip(_fromUtf8(""))
    self.dockWidgetFrames.setLayoutDirection(QtCore.Qt.LeftToRight)
    self.dockWidgetFrames.setAutoFillBackground(False)
    self.dockWidgetFrames.setFloating(False)
    self.dockWidgetFrames.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
    self.dockWidgetFrames.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
    self.dockWidgetFrames.setObjectName(_fromUtf8("dockWidgetFrames"))
    self.dockWidgetContents_3 = QtGui.QWidget()
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.dockWidgetContents_3.sizePolicy().hasHeightForWidth())
    self.dockWidgetContents_3.setSizePolicy(sizePolicy)
    self.dockWidgetContents_3.setObjectName(_fromUtf8("dockWidgetContents_3"))
    self.horizontalLayout_2 = QtGui.QHBoxLayout(self.dockWidgetContents_3)
    self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
    self.verticalLayout_8 = QtGui.QVBoxLayout()
    self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
    self.horizontalLayout_4 = QtGui.QHBoxLayout()
    self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
    self.label_5 = QtGui.QLabel(self.dockWidgetContents_3)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
    self.label_5.setSizePolicy(sizePolicy)
    font = QtGui.QFont()
    font.setBold(True)
    font.setWeight(75)
    font.setStyleStrategy(QtGui.QFont.PreferAntialias)
    self.label_5.setFont(font)
    self.label_5.setObjectName(_fromUtf8("label_5"))
    self.horizontalLayout_4.addWidget(self.label_5)
    self.groupBox_2 = QtGui.QGroupBox(self.dockWidgetContents_3)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
    self.groupBox_2.setSizePolicy(sizePolicy)
    self.groupBox_2.setTitle(_fromUtf8(""))
    self.groupBox_2.setFlat(False)
    self.groupBox_2.setCheckable(False)
    self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
    self.gridLayout_6 = QtGui.QGridLayout(self.groupBox_2)
    self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
    self.checkAutohold = QtGui.QCheckBox(self.groupBox_2)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.checkAutohold.sizePolicy().hasHeightForWidth())
    self.checkAutohold.setSizePolicy(sizePolicy)
    self.checkAutohold.setObjectName(_fromUtf8("checkAutohold"))
    self.gridLayout_6.addWidget(self.checkAutohold, 1, 6, 1, 1)
    self.checkFailed = QtGui.QCheckBox(self.groupBox_2)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.checkFailed.sizePolicy().hasHeightForWidth())
    self.checkFailed.setSizePolicy(sizePolicy)
    self.checkFailed.setObjectName(_fromUtf8("checkFailed"))
    self.gridLayout_6.addWidget(self.checkFailed, 1, 5, 1, 1)
    self.checkKilled = QtGui.QCheckBox(self.groupBox_2)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.checkKilled.sizePolicy().hasHeightForWidth())
    self.checkKilled.setSizePolicy(sizePolicy)
    self.checkKilled.setObjectName(_fromUtf8("checkKilled"))
    self.gridLayout_6.addWidget(self.checkKilled, 1, 8, 1, 1)
    self.checkHold = QtGui.QCheckBox(self.groupBox_2)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.checkHold.sizePolicy().hasHeightForWidth())
    self.checkHold.setSizePolicy(sizePolicy)
    self.checkHold.setObjectName(_fromUtf8("checkHold"))
    self.gridLayout_6.addWidget(self.checkHold, 1, 7, 1, 1)
    self.checkDone = QtGui.QCheckBox(self.groupBox_2)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.checkDone.sizePolicy().hasHeightForWidth())
    self.checkDone.setSizePolicy(sizePolicy)
    self.checkDone.setObjectName(_fromUtf8("checkDone"))
    self.gridLayout_6.addWidget(self.checkDone, 1, 3, 1, 1)
    self.checkRunning = QtGui.QCheckBox(self.groupBox_2)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.checkRunning.sizePolicy().hasHeightForWidth())
    self.checkRunning.setSizePolicy(sizePolicy)
    self.checkRunning.setObjectName(_fromUtf8("checkRunning"))
    self.gridLayout_6.addWidget(self.checkRunning, 1, 2, 1, 1)
    self.checkAssigned = QtGui.QCheckBox(self.groupBox_2)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.checkAssigned.sizePolicy().hasHeightForWidth())
    self.checkAssigned.setSizePolicy(sizePolicy)
    self.checkAssigned.setObjectName(_fromUtf8("checkAssigned"))
    self.gridLayout_6.addWidget(self.checkAssigned, 1, 1, 1, 1)
    self.checkAll = QtGui.QCheckBox(self.groupBox_2)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.checkAll.sizePolicy().hasHeightForWidth())
    self.checkAll.setSizePolicy(sizePolicy)
    font = QtGui.QFont()
    font.setBold(True)
    font.setWeight(75)
    self.checkAll.setFont(font)
    self.checkAll.setObjectName(_fromUtf8("checkAll"))
    self.gridLayout_6.addWidget(self.checkAll, 1, 9, 1, 1)
    self.checkUnassigned = QtGui.QCheckBox(self.groupBox_2)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.checkUnassigned.sizePolicy().hasHeightForWidth())
    self.checkUnassigned.setSizePolicy(sizePolicy)
    self.checkUnassigned.setObjectName(_fromUtf8("checkUnassigned"))
    self.gridLayout_6.addWidget(self.checkUnassigned, 1, 0, 1, 1)
    self.checkHung = QtGui.QCheckBox(self.groupBox_2)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.checkHung.sizePolicy().hasHeightForWidth())
    self.checkHung.setSizePolicy(sizePolicy)
    self.checkHung.setObjectName(_fromUtf8("checkHung"))
    self.gridLayout_6.addWidget(self.checkHung, 1, 4, 1, 1)
    self.horizontalLayout_4.addWidget(self.groupBox_2)
    spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.horizontalLayout_4.addItem(spacerItem3)
    self.verticalLayout_8.addLayout(self.horizontalLayout_4)
    self.horizontalLayout_8 = QtGui.QHBoxLayout()
    self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
    self.verticalLayout_8.addLayout(self.horizontalLayout_8)
    self.horizontalLayout_6 = QtGui.QHBoxLayout()
    self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
    self.labelSearchFrames = QtGui.QLabel(self.dockWidgetContents_3)
    self.labelSearchFrames.setObjectName(_fromUtf8("labelSearchFrames"))
    self.horizontalLayout_6.addWidget(self.labelSearchFrames)
    self.lineEditSearchFrames = QtGui.QLineEdit(self.dockWidgetContents_3)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.lineEditSearchFrames.sizePolicy().hasHeightForWidth())
    self.lineEditSearchFrames.setSizePolicy(sizePolicy)
    self.lineEditSearchFrames.setObjectName(_fromUtf8("lineEditSearchFrames"))
    self.horizontalLayout_6.addWidget(self.lineEditSearchFrames)
    spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
    self.horizontalLayout_6.addItem(spacerItem4)
    self.label_6 = QtGui.QLabel(self.dockWidgetContents_3)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
    self.label_6.setSizePolicy(sizePolicy)
    self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.label_6.setObjectName(_fromUtf8("label_6"))
    self.horizontalLayout_6.addWidget(self.label_6)
    self.labelTotal = QtGui.QLabel(self.dockWidgetContents_3)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.labelTotal.sizePolicy().hasHeightForWidth())
    self.labelTotal.setSizePolicy(sizePolicy)
    self.labelTotal.setLayoutDirection(QtCore.Qt.LeftToRight)
    self.labelTotal.setAutoFillBackground(True)
    self.labelTotal.setFrameShape(QtGui.QFrame.WinPanel)
    self.labelTotal.setFrameShadow(QtGui.QFrame.Sunken)
    self.labelTotal.setTextFormat(QtCore.Qt.PlainText)
    self.labelTotal.setScaledContents(False)
    self.labelTotal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.labelTotal.setMargin(2)
    self.labelTotal.setObjectName(_fromUtf8("labelTotal"))
    self.horizontalLayout_6.addWidget(self.labelTotal)
    self.verticalLayout_8.addLayout(self.horizontalLayout_6)
    self.tableFrames = QtGui.QTableWidget(self.dockWidgetContents_3)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
    sizePolicy.setHorizontalStretch(1)
    sizePolicy.setVerticalStretch(1)
    sizePolicy.setHeightForWidth(self.tableFrames.sizePolicy().hasHeightForWidth())
    self.tableFrames.setSizePolicy(sizePolicy)
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
    self.tableFrames.setPalette(palette)
    self.tableFrames.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
    self.tableFrames.setEditTriggers(QtGui.QAbstractItemView.DoubleClicked)
    self.tableFrames.setAlternatingRowColors(False)
    self.tableFrames.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
    self.tableFrames.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
    self.tableFrames.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
    self.tableFrames.setWordWrap(False)
    self.tableFrames.setObjectName(_fromUtf8("tableFrames"))
    self.tableFrames.setColumnCount(0)
    self.tableFrames.setRowCount(0)
    self.tableFrames.horizontalHeader().setCascadingSectionResizes(True)
    self.tableFrames.horizontalHeader().setStretchLastSection(True)
    self.tableFrames.verticalHeader().setVisible(False)
    self.verticalLayout_8.addWidget(self.tableFrames)
    self.horizontalLayout_7 = QtGui.QHBoxLayout()
    self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
    self.checkRefresh = QtGui.QCheckBox(self.dockWidgetContents_3)
    self.checkRefresh.setObjectName(_fromUtf8("checkRefresh"))
    self.horizontalLayout_7.addWidget(self.checkRefresh)
    spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.horizontalLayout_7.addItem(spacerItem5)
    self.framesRefresh = QtGui.QPushButton(self.dockWidgetContents_3)
    self.framesRefresh.setObjectName(_fromUtf8("framesRefresh"))
    self.horizontalLayout_7.addWidget(self.framesRefresh)
    self.verticalLayout_8.addLayout(self.horizontalLayout_7)
    self.horizontalLayout_2.addLayout(self.verticalLayout_8)
    self.dockWidgetFrames.setWidget(self.dockWidgetContents_3)
    mainRbhusList.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockWidgetFrames)

    self.retranslateUi(mainRbhusList)
    QtCore.QMetaObject.connectSlotsByName(mainRbhusList)

  def retranslateUi(self, mainRbhusList):
    mainRbhusList.setWindowTitle(_translate("mainRbhusList", "rbhusList", None))
    self.label.setText(_translate("mainRbhusList", "USER :", None))
    self.labelUser.setText(_translate("mainRbhusList", "TextLabel", None))
    self.labelTask.setText(_translate("mainRbhusList", "TASKS", None))
    self.checkTHold.setText(_translate("mainRbhusList", "hold", None))
    self.checkTDone.setText(_translate("mainRbhusList", "done", None))
    self.checkTActive.setText(_translate("mainRbhusList", "active", None))
    self.checkTAutohold.setText(_translate("mainRbhusList", "autohold", None))
    self.checkTAll.setText(_translate("mainRbhusList", "ALL", None))
    self.checkTMine.setText(_translate("mainRbhusList", "mine", None))
    self.labelSearch.setText(_translate("mainRbhusList", "search", None))
    self.label_2.setText(_translate("mainRbhusList", "total", None))
    self.labelTaskTotal.setText(_translate("mainRbhusList", "0", None))
    self.tableList.setSortingEnabled(True)
    self.taskRefresh.setToolTip(_translate("mainRbhusList", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline; color:#ff0000;\">CHECK MORE THAN 100 TIMES IF POSSIBLE BEFORE DELETING !!</span></p></body></html>", None))
    self.taskRefresh.setStatusTip(_translate("mainRbhusList", "CHECK MORE THAN 100 TIMES IF POSSIBLE BEFORE DELETING !!", None))
    self.taskRefresh.setText(_translate("mainRbhusList", "refresh", None))
    self.label_5.setText(_translate("mainRbhusList", "FRAMES", None))
    self.checkAutohold.setText(_translate("mainRbhusList", "autohold", None))
    self.checkFailed.setText(_translate("mainRbhusList", "failed", None))
    self.checkKilled.setText(_translate("mainRbhusList", "killed", None))
    self.checkHold.setText(_translate("mainRbhusList", "hold", None))
    self.checkDone.setText(_translate("mainRbhusList", "done", None))
    self.checkRunning.setText(_translate("mainRbhusList", "running", None))
    self.checkAssigned.setText(_translate("mainRbhusList", "assigned", None))
    self.checkAll.setText(_translate("mainRbhusList", "ALL", None))
    self.checkUnassigned.setText(_translate("mainRbhusList", "unassigned", None))
    self.checkHung.setText(_translate("mainRbhusList", "hung", None))
    self.labelSearchFrames.setText(_translate("mainRbhusList", "search", None))
    self.label_6.setText(_translate("mainRbhusList", "total", None))
    self.labelTotal.setText(_translate("mainRbhusList", "0", None))
    self.tableFrames.setSortingEnabled(True)
    self.checkRefresh.setText(_translate("mainRbhusList", "autoRefresh", None))
    self.framesRefresh.setText(_translate("mainRbhusList", "refresh", None))

