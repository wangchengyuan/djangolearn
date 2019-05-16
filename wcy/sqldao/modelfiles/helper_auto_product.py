# -*-conding:utf-8-*-
# @author:wangchengyuan
# @time:2019/3/28 7:16 PM
# @desc:

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from wcy.bin import readconfig

class Helper_auto_product():
    def __init__(self):
        readconf = readconfig.ReadConfig()
        host = readconf.get_database('host')
        user = readconf.get_database('user')
        passwd = readconf.get_database('passwd')
        db = 'auto_product'
        dbaddress = 'mysql+pymysql://{}:{}@{}/{}?charset=utf8'.format(user, passwd, host, db)
        engine=create_engine(dbaddress)
        Session=sessionmaker(bind=engine)
        self.session=Session()

    def get_session(self):
        return self.session

    def close_session(self):
        self.session.commit()
        self.session.close()