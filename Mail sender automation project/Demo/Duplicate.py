import os
from Hashfile import *

def FindDuplicate(path):
     flag=os.path.isabs(path)

     if flag==False:
          path=os.path.abspath(path)

     exists=os.path.isdir(path)
     cnt=0

     dups={}
     if exists:
          for dirName,subdirs,fileList in os.walk(path):
               
               for filen in fileList:
                    cnt+=1
                    path=os.path.join(dirName,filen)
                    file_hash=hashfile(path)
                    if file_hash in dups:
                    
                         dups[file_hash].append(path)
                    else:
                         dups[file_hash]=[path]
          return dups,cnt
     else:
          print("Invalid path")     


def DeleteFiles(dict1):
     results=list(filter(lambda x:len(x)>1,dict1.values()))
     icnt=0
     deleteCount=0

     if len(results)>0:
          for result in results:
               for subresult in result:
                    icnt+=1
                    if icnt>=2:
                         os.remove(subresult)
                         deleteCount+=1
               icnt=0
     else:
          print("No duplicate files found.")
          
     return deleteCount


def PrintDuplicate(dict1):
     resultList=[]
     results=list(filter(lambda x:len(x)>1,dict1.values()))

     if len(results)>0:
          print("Duplicate Founds")
          print("Duplicate files are stored into Log file")

          icnt=0
          for result in results:
               for subresult in result:
                    icnt+=1
                    if icnt>=2:
                         resultList.append('\t\t%s'%subresult)
     else:
        print("No duplicate found.")
     
     return resultList

