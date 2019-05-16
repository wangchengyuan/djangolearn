# -*-conding:utf-8-*-
# @author:wangchengyuan
# @file:helper_auto_account.py
# @time:2019/2/22下午2:19
# @desc:


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from wcy.bin import readconfig

class Helper_auto_account():
    def __init__(self):
        readconf = readconfig.ReadConfig()
        host = readconf.get_database('host')
        user = readconf.get_database('user')
        passwd = readconf.get_database('passwd')
        db = 'auto_account'
        dbaddress = 'mysql+pymysql://{}:{}@{}/{}?charset=utf8'.format(user, passwd, host, db)
        engine=create_engine(dbaddress)
        Session=sessionmaker(bind=engine)
        self.session=Session()

    def get_session(self):
        return self.session

    def close_session(self):
        self.session.commit()
        self.session.close()