#! user/bin/python3
# -*- coding:utf-8 -*-
"""
author:songmohan
date:2018-01-06
desc:实现大文件的分割
"""

import os
import settings

def createdirifnotexists(dirpath):
	if os.path.exists(dirpath)==False:
	  os.makedirs(dirpath)

    
def main():
  print("文件分割器!")
  checkresult = settings.checksettings()
  
  if checkresult.success==False:
  	print(checkresult.msg)
  	return

  createdirifnotexists(settings.output)
  
  inputpath=input(u"请输入需要分割的文件路径：")
  if os.path.isfile(inputpath):
  	print(u"文件存在")
  else:
    print(u"没有找到文件：%s" % (inputpath))
  
main();