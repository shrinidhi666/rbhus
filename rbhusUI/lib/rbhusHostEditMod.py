# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rbhusHostEditMod.ui'
#
# Created: Tue Oct  8 12:18:14 2013
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

class Ui_rbhusHostEdit(object):
  def setupUi(self, rbhusHostEdit):
    rbhusHostEdit.setObjectName(_fromUtf8("rbhusHostEdit"))
    rbhusHostEdit.resize(503, 97)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(rbhusHostEdit.sizePolicy().hasHeightForWidth())
    rbhusHostEdit.setSizePolicy(sizePolicy)
    self.centralwidget = QtGui.QWidget(rbhusHostEdit)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
    self.centralwidget.setSizePolicy(sizePolicy)
    self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
    self.gridLayout = QtGui.QGridLayout(self.centralwidget)
    self.gridLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
    self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
    self.labelImageName = QtGui.QLabel(self.centralwidget)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.labelImageName.sizePolicy().hasHeightForWidth())
    self.labelImageName.setSizePolicy(sizePolicy)
    self.labelImageName.setObjectName(_fromUtf8("labelImageName"))
    self.gridLayout.addWidget(self.labelImageName, 0, 0, 1, 1)
    self.horizontalLayout = QtGui.QHBoxLayout()
    self.horizontalLayout.setContentsMargins(-1, 10, -1, -1)
    self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
    spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    self.horizontalLayout.addItem(spacerItem)
    self.pushApply = QtGui.QPushButton(self.centralwidget)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.pushApply.sizePolicy().hasHeightForWidth())
    self.pushApply.setSizePolicy(sizePolicy)
    self.pushApply.setObjectName(_fromUtf8("pushApply"))
    self.horizontalLayout.addWidget(self.pushApply)
    self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 2)
    self.spinCpu = QtGui.QSpinBox(self.centralwidget)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.spinCpu.sizePolicy().hasHeightForWidth())
    self.spinCpu.setSizePolicy(sizePolicy)
    self.spinCpu.setObjectName(_fromUtf8("spinCpu"))
    self.gridLayout.addWidget(self.spinCpu, 0, 1, 1, 1)
    self.label = QtGui.QLabel(self.centralwidget)
    self.label.setObjectName(_fromUtf8("label"))
    self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
    self.lineEditGroups = QtGui.QLineEdit(self.centralwidget)
    self.lineEditGroups.setObjectName(_fromUtf8("lineEditGroups"))
    self.gridLayout.addWidget(self.lineEditGroups, 1, 1, 1, 1)
    self.pushReset = QtGui.QPushButton(self.centralwidget)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.pushReset.sizePolicy().hasHeightForWidth())
    self.pushReset.setSizePolicy(sizePolicy)
    self.pushReset.setObjectName(_fromUtf8("pushReset"))
    self.gridLayout.addWidget(self.pushReset, 2, 0, 1, 1)
    self.pushSelect = QtGui.QPushButton(self.centralwidget)
    self.pushSelect.setObjectName(_fromUtf8("pushSelect"))
    self.gridLayout.addWidget(self.pushSelect, 1, 2, 1, 1)
    rbhusHostEdit.setCentralWidget(self.centralwidget)

    self.retranslateUi(rbhusHostEdit)
    QtCore.QMetaObject.connectSlotsByName(rbhusHostEdit)

  def retranslateUi(self, rbhusHostEdit):
    rbhusHostEdit.setWindowTitle(_translate("rbhusHostEdit", "rbhusHostEdit", None))
    self.labelImageName.setToolTip(_translate("rbhusHostEdit", "Effective Number of Cores to use for render", None))
    self.labelImageName.setText(_translate("rbhusHostEdit", "eCpus", None))
    self.pushApply.setText(_translate("rbhusHostEdit", "apply", None))
    self.label.setText(_translate("rbhusHostEdit", "groups", None))
    self.pushReset.setText(_translate("rbhusHostEdit", "reset", None))
    self.pushSelect.setText(_translate("rbhusHostEdit", "select", None))

