import sys
import os
import socket
import MySQLdb
progPath =  sys.argv[0].split(os.sep)
if(len(progPath) > 1):
  pwd = os.sep.join(progPath[0:-1])
  cwd = os.path.abspath(pwd)
else:
  cwd = os.path.abspath(os.getcwd())

sys.path.append(cwd.rstrip(os.sep) + os.sep)
import dbPipe
import constantsPipe




def getDirMaps():
  dbconn = dbPipe.dbPipe()
  try:
    rows = dbconn.execute("SELECT * FROM dirMaps", dictionary=True)
    return(rows)
  except:
    print(str(sys.exc_info()))
    return(0)
  
 
 
def getProjTypes():
  dbconn = dbPipe.dbPipe()
  try:
    rows = dbconn.execute("SELECT * FROM projTypes", dictionary=True)
    return(rows)
  except:
    print(str(sys.exc_info()))
    return(0)
  
  
def getStageTypes():
  dbconn = dbPipe.dbPipe()
  try:
    rows = dbconn.execute("SELECT * FROM stageTypes", dictionary=True)
    return(rows)
  except:
    print(str(sys.exc_info()))
    return(0)


def getProjDefaults(self):
  try:
    rows = self.db_conn.execute("desc tasks",dictionary=True)
    taskFieldss = {}
    for row in rows:
      taskFieldss[row['Field']] = row['Default']
    return(taskFieldss)
  except:
    return(0)

def setupProj(projType,projName,projOs,directory,admins,rbhusRender,rbhusRenderServer,desc):
  dbconn = dbPipe.dbPipe()
  pTypes = getProjTypes()
  cScript = ""
  for pT in pTypes:
    if(pT['type'] == projType):
      cScript = pT['scriptDir']
      
  os.environ['rp_projName_c'] = projName
  os.environ['rp_projType_c'] = projType
  os.environ['rp_projDirectory_c'] = directory
  os.environ['rp_projAdmin_c'] = admins
  os.environ['rp_projRender_c'] = rbhusRender
  os.environ['rp_projRenderS_c'] = rbhusRenderServer
  os.environ['rp_projOs_c'] = projOs
  os.environ['rp_projDesc_c'] = desc
  try:
    dbconn.execute("insert into proj (projName,directory,admins,os,projType,rbhusRenderIntergration,rbhusRenderServer,description) \
                    values ('"+ str(projName) +"', \
                    '"+ str(directory) +"', \
                    '"+ str(admins) +"', \
                    '"+ str(projOs) +"', \
                    '"+ str(projType) +"', \
                    '"+ str(rbhusRender) +"', \
                    '"+ str(rbhusRenderServer) +"', \
                    '"+ str(desc) +"')")
  except:
    print(str(sys.exc_info()))
    
  