#!/usr/bin/python
from PyQt4 import QtCore, QtGui
import glob
import os
import sys


dirSelf = os.path.dirname(os.path.realpath(__file__))
print(dirSelf)
sys.path.append(dirSelf.rstrip(os.sep).rstrip("guiBin").rstrip(os.sep) + os.sep + "lib")


import rbhusPipeProjCreateMod
print(dirSelf.rstrip(os.sep).rstrip("guiBin").rstrip(os.sep).rstrip("rbhusUI").rstrip(os.sep) + os.sep +"rbhus")
sys.path.append(dirSelf.rstrip(os.sep).rstrip("guiBin").rstrip(os.sep).rstrip("rbhusUI").rstrip(os.sep) + os.sep +"rbhus")
import dbPipe
import constantsPipe
import authPipe
import utilsPipe


try:
  _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
  _fromUtf8 = lambda s: s
  

class Ui_Form(rbhusPipeProjCreateMod.Ui_MainWindow):
  def setupUi(self, Form):
    rbhusPipeProjCreateMod.Ui_MainWindow.setupUi(self,Form)
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(_fromUtf8(dirSelf.rstrip(os.sep).rstrip("guiBin").rstrip(os.sep).rstrip("rbhusUI").rstrip(os.sep)+ os.sep +"etc/icons/rbhusPipe.svg")), QtGui.QIcon.Normal, QtGui.QIcon.On)
    Form.setWindowIcon(icon)
    self.center()
    self.setProjTypes()
    self.setDirectory()
    self.dateEditDue.setDateTime(QtCore.QDateTime.currentDateTime())
    
    
    
  def center(self):
    Form.move(QtGui.QApplication.desktop().screen().rect().center()- Form.rect().center())

  def setProjTypes(self):
    rows = utilsPipe.getProjTypes()
    self.comboProjType.clear()  
    if(rows):
      for row in rows:
        self.comboProjType.addItem(_fromUtf8(row['type']))
      
      return(1)
    return(0)     
  
  
  def setDirectory(self):
    dirs = utilsPipe.getDirMaps()
    self.comboDirectory.clear()
    if(dirs):
      for d in dirs:
        self.comboDirectory.addItem(_fromUtf8(d['directory']))
      return(1)
    return(0)
    
    
  def setDefaults(self):
    defs = utilsPipe.getProjDefaults()
    




if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  Form = QtGui.QMainWindow()
  ui = Ui_Form()
  ui.setupUi(Form)
  Form.show()
  sys.exit(app.exec_())
    