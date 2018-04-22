# coding=utf-8
####定义单例的日志logger模块

import logging
import logging.config
import ConfigParser
import os

cf = ConfigParser.ConfigParser()
cf.read(os.path.join(os.path.dirname(__file__),'global.conf'))  # 读配置文件（ini、conf）返回结果是列表
cf.sections()  # 获取读到的所有sections(域)，返回列表类型
# cf.options('sectionname')  # 某个域下的所有key，返回列表类型
# cf.items('global')  # 某个域下的所有key，value对
# value = cf.get('global', 'envType')  # 获取某个yu下的key对应的value值
logconfigPath = cf.get(cf.get('global', 'envType'),'logConfig')
print logconfigPath


class logControl:
    logging.config.fileConfig(os.path.join(os.path.dirname(__file__),logconfigPath))

    ##create logger
    def getLogger(self):
        logger = logging.getLogger('run')
        return logger
