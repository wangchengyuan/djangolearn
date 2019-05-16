# -*-conding:utf-8-*-
# @author:wangchengyuan
# @time:2019/3/25 11:13 AM
# @desc:


import configparser
import os

proDir=os.path.dirname(os.path.dirname(__file__))

class ReadConfig():


    def __init__(self):
        self.configdir = os.path.join(proDir,'config/config.ini')
        self.cf = configparser.ConfigParser()
        self.cf.read(self.configdir)

    # 增加获取对应配置的方法，获取 DATABASE、SSHRELATE，如有新配置，新增方法即可
    # 配置文件中DATABASE相关配置的获取和修改
    def get_database(self, name):
        value = self.cf.get('DATABASE', name)
        return value

    def set_database(self, name, value):
        self.cf.set('DATABASE', name, value)
        print('test')
        with open(self.configdir, 'w+') as f:
            self.cf.write(f)

    # 配置文件中SSHRELATE相关配置的获取和修改
    def get_sshrelate(self, name):
        value = self.cf.get('SSHRELATE', name)
        return value

    def set_sshrelate(self, name, value):
        self.cf.set('SSHRELATE', name, value)
        with open(self.configdir, 'w+') as f:
            self.cf.write(f)

    # 配置文件中URL相关配置的获取和修改
    def get_urlrelate(self, name):
        value = self.cf.get('URL', name)
        return value

    def set_urlrelate(self, name, value):
        self.cf.set('URL', name, value)
        with open(self.configdir, 'w') as f:
            self.cf.write(f)