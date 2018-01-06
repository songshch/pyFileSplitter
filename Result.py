#!user/bin/python3
# -*- coding:utf-8 -*-

"""
公共执行结果
"""

class Result:
    def __init__(self):
        self.code=0       # 错误码
        self.success=True # 成功失败标识
        self.msg=""       # 错误消息
        self.data=None    # 返回数据

    """
     设置失败消息
    """
    def setfailed(self,code,msg):
        self.setfailed(msg,None)
    
    """
    设置失败消息和数据
    """
    def setfailed(self,code,msg,data):
        self.msg=msg
        self.code=code
        self.success=False
        self.data=data
     
    """
    设置成功消息
    """
    def setsuccessed(self,data):
     	self.msg="成功";
     	self.data=data;
