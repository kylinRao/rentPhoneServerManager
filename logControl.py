#coding=utf-8
####定义单例的日志logger模块

import  logging
import logging.config
import os,path
class logControl:
	print os.path.abspath(__file__)
	print os.path.join(os.path.dirname(os.path.abspath(__file__)),"logger.conf")
	logging.config.fileConfig(os.path.join(os.path.dirname(os.path.abspath(__file__)),"conf","logger.conf"))
	##create logger
	@staticmethod
	def getLogger():
		logger = logging.getLogger('run')
		return logger