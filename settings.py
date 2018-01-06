#!user/bin/python3
# -*- coding:utf-8 -*-

"""
设置文件分割器的基本配置
"""

import Result

"""
分割后文件输出路径
"""
output=u"D:\\song\\workspace\\PythonProject\\filesplitter\\output"

"""
分割后每个文件的大小(M)
"""
size=10

"""
分割后文件名称前缀，如果为空使用原始文件名称
"""
nameprefix="test";



def checksettings():
	checkresult= Result.Result()
	if output == "":
		checkresult.setfailed("-1","请配置输出文件夹")
	elif  isinstance(size,int) and size<=0: # 判断是否为int并且大于0
		checkresult.setfailed("-2","请配置输出文件大小")
	return checkresult;


