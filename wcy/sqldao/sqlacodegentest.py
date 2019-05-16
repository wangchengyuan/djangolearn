# -*-conding:utf-8-*-
# @author:wangchengyuan
# @file:sqlacodegentest.py
# @time:2019/1/30下午7:00
# @desc:

import os
from wcy.bin import readconfig

proDir=os.path.dirname(__file__)

def sqlacodegenTest(tablename,dbname):
    readconf = readconfig.ReadConfig()
    filename = tablename + '.py'
    host = readconf.get_database('host')
    user = readconf.get_database('user')
    passwd = readconf.get_database('passwd')
    db = dbname
    dbaddress = 'mysql+pymysql://{}:{}@{}/{}'.format(user, passwd, host, db)
    dirpath=os.path.join(proDir,'modelfiles','%s') %db
    #判断包是否存在，不存创建包
    if os.path.exists(dirpath)&os.path.isdir(dirpath):
        print("文件目录已存在")
    else:
        print("文件目录不存在")
        os.mkdir(dirpath)
        with open(os.path.join(dirpath,'__init__.py'),'w'):
            print("创建包成功")
    #判断文件是否存在，不存在在对应路径下生成model文件
    lines = 'sqlacodegen --tables %s --outfile %s ' % (tablename, os.path.join(dirpath,filename)) + dbaddress
    if os.path.exists(os.path.join(dirpath,filename)):
        print('文件已存在')
    else:
        print('文件不存在')
        os.system(lines)

if __name__ == '__main__':
    dbname='auto_order'  #表所在数据库名称
    tablename='assets'      #表名称
    sqlacodegenTest(tablename,dbname)