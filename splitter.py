# -*- coding:utf-8 -*-
"""
文件分割器
"""
import settings
import io
import os

class FileSplitter:
	"""
	构造函数
	"""
	def __init__(self,inputpath):
		self.inputpath=inputpath
		self.outoutpath=settings.output
		self.filesize=settings.size
		self.name=settings.nameprefix
		self.number=1
	
	"""
	分割主方法
	"""
	def split(self):
		totalsize=self.getsize(self.inputpath)
		file=self.open();
		line = file.readline()
		lines = []
		size=0;
		while line:
			size = size+len(line)
			print(size)
			lines.append(line)
			if size>self.filesize:
		 		self.write(lines)
		 		size=0;
		 		self.number=self.number+1
		 		del lines[:]
			line=file.readline()
		self.write(lines)
		
	"""
	得到文件大小和计算分割文件的数量
	"""	
	def getsize(self,filepath):
		fsize = os.path.getsize(filepath)
		return fsize;

	"""
	读取文件
	"""	
	def open(self):
		return open(self.inputpath,'rb')

	"""
	写文件
	"""
	def write(self,lines):
		if len(lines)==0 :
			return
		filename = self.name+str(self.number)+".txt";
		print(filename)
		filepath=os.path.join(self.outoutpath,filename)
		file = open(filepath,"wb");
		for line in lines:
			file.write(line);