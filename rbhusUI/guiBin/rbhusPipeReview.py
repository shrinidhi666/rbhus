#!/usr/bin/python
import os
import sys
import datetime
import re
import argparse
import logging
import logging.handlers
import socket
import tempfile
import copy
from PyQt4 import QtCore, QtGui



dirSelf = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dirSelf.rstrip(os.sep).rstrip("guiBin").rstrip(os.sep) + os.sep + "lib")

import rbhusPipeReviewMod

sys.path.append(dirSelf.rstrip(os.sep).rstrip("guiBin").rstrip(os.sep).rstrip("rbhusUI").rstrip(os.sep) + os.sep +"rbhus")

import dbPipe
import constantsPipe
import authPipe
import utilsPipe



parser = argparse.ArgumentParser()

hostname = socket.gethostname()
tempDir = os.path.abspath(tempfile.gettempdir())

if(sys.platform.find("win") >= 0):
  try:
    username = os.environ['rbhusPipe_acl_user']
  except:
    username = "nobody"
if(sys.platform.find("linux") >= 0):
  try:
    username = os.environ['rbhusPipe_acl_user']
  except:
    username = "nobody"
    

try:
  _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
  _fromUtf8 = lambda s: s
  

try:
  _encoding = QtGui.QApplication.UnicodeUTF8
  def _translate(context, text, disambig):
    return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
  def _translate(context, text, disambig):
    return QtGui.QApplication.translate(context, text, disambig)
  
  
parser = argparse.ArgumentParser()
parser.add_argument("-p","--assetpath",dest='assetpath',help='asset path (pipePath)')
parser.add_argument("-i","--assetid",dest='assetid',help='asset id')
args = parser.parse_args()




  
class Ui_Form(rbhusPipeReviewMod.Ui_MainWindow):
  def setupUi(self, Form):
    rbhusPipeReviewMod.Ui_MainWindow.setupUi(self,Form)
    self.spacerForMsgBox = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
    self.splitter.setStretchFactor(0, 10)
    self.assdets = {}
    if(args.assetpath):
      self.assdets = utilsPipe.getAssDetails(assPath=args.assetpath)
    elif(args.assetid):
      self.assdets = utilsPipe.getAssDetails(assId=args.assetid)
    if(self.assdets):
      Form.setWindowTitle(self.assdets['path'])
    else:
      sys.exit(0)
    self.assReviewDets = utilsPipe.reviewDetails(assId=self.assdets['assetId'])
    self.reviewVersion.setText("review for version : "+ str(self.assdets['reviewVersion']))
    self.reviewCountNow = 0
    if(self.assReviewDets):
      for x in self.assReviewDets:
        self.addMsgBox(x['message'],x['username'],x['datetime'],x['reviewVersion'],x['reviewCount'])
        self.reviewCountNow = x['reviewCount'] + 1
    else:
      self.reviewCountNow = 1
    print("REVIEW COUNT : "+ str(self.reviewCountNow))
    self.pushOpenReferenceReview.clicked.connect(lambda item,ver=str(self.assdets['reviewVersion']),revCount=str(self.reviewCountNow) : self.openReferenceFolder(item,ver,revCount))
    self.pushSend.clicked.connect(self.sendReview)
    self.scrollArea.verticalScrollBar().rangeChanged.connect(self.updateScroll)


  
  def updateScroll(self,min,max):
    self.scrollArea.verticalScrollBar().setValue(max)
    print(max)



  def update(self):
    x = utilsPipe.reviewDetails(assId=self.assdets['assetId'],)
    self.addMsgBox(x['message'],x['username'],x['datetime'],x['reviewVersion'],x['reviewCount'])
    self.reviewCountNow = x['reviewCount'] + 1


  def openReferenceFolder(self,*args):
    abspath  = utilsPipe.getAbsPath(self.assdets['path'])
    refFolder = abspath +"/review_"+ str(args[1]) +"/"+ str(args[2])
    print(refFolder)

  def sendReview(self,args):
    revdets = {}
    revdets['assetId'] = str(self.assdets['assetId'])
    revdets['reviewVersion'] = str(self.assdets['reviewVersion'])
    revdets['message'] = self.plainTextEdit.document().toPlainText()
    revdets['username'] = username
    utilsPipe.reviewAdd(revdets)



    
  def addMsgBox(self,msg,user1,date1,ver,revCount):
    try:
      self.verticalLayout_2.removeItem(self.spacerForMsgBox)
    except:
      pass
    widgetMsgQueue = QtGui.QWidget(self.scrollAreaWidgetContents)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(widgetMsgQueue.sizePolicy().hasHeightForWidth())
    widgetMsgQueue.setSizePolicy(sizePolicy)
    widgetMsgQueue.setObjectName(_fromUtf8("widgetMsgQueue"))
    verticalLayout_3 = QtGui.QVBoxLayout(widgetMsgQueue)
    verticalLayout_3.setMargin(0)
    verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
    groupBox = QtGui.QGroupBox(widgetMsgQueue)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(groupBox.sizePolicy().hasHeightForWidth())
    groupBox.setSizePolicy(sizePolicy)
    groupBox.setTitle(_fromUtf8(""))
    groupBox.setObjectName(_fromUtf8("groupBox"))
    horizontalLayout = QtGui.QHBoxLayout(groupBox)
    horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
    user = QtGui.QLabel(groupBox)
    user.setObjectName(_fromUtf8("user"))
    horizontalLayout.addWidget(user)
    date = QtGui.QLabel(groupBox)
    date.setObjectName(_fromUtf8("date"))
    horizontalLayout.addWidget(date)
    version = QtGui.QLabel(groupBox)
    version.setObjectName(_fromUtf8("version"))
    horizontalLayout.addWidget(version)
    verticalLayout_3.addWidget(groupBox)
    msgBox = QtGui.QPlainTextEdit(widgetMsgQueue)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(msgBox.sizePolicy().hasHeightForWidth())
    msgBox.setSizePolicy(sizePolicy)
    msgBox.setObjectName(_fromUtf8("msgBox"))
    verticalLayout_3.addWidget(msgBox)
    horizontalLayout_4 = QtGui.QHBoxLayout()
    horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
    pushOpenReferenceReviewed = QtGui.QPushButton(widgetMsgQueue)
    pushOpenReferenceReviewed.setObjectName(_fromUtf8("pushOpenReferenceReviewed"))
    horizontalLayout_4.addWidget(pushOpenReferenceReviewed)
    spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
    horizontalLayout_4.addItem(spacerItem)
    verticalLayout_3.addLayout(horizontalLayout_4)
    msgBox.setPlainText(msg)
    msgBox.setReadOnly(True)
    user.setText("user : "+ str(user1))
    date.setText("date : "+ str(date1))
    version.setText("version : "+ str(ver))
    pushOpenReferenceReviewed.setText("open reference folder")

    self.verticalLayout_2.addWidget(widgetMsgQueue)
    self.verticalLayout_2.addItem(self.spacerForMsgBox)
    pushOpenReferenceReviewed.clicked.connect(lambda item, ver=str(ver),revCount=str(revCount) : self.openReferenceFolder(item,ver,revCount))

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  Form = QtGui.QMainWindow()
  ui = Ui_Form()
  ui.setupUi(Form)
  Form.show()
  sys.exit(app.exec_())
    