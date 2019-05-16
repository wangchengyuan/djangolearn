# -*-conding:utf-8-*-
# @author:wangchengyuan
# @time:2019/4/16 2:36 PM
# @desc:

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from wcy.bin import readconfig
from wcy.sqldao.modelfiles.auto_order.orders import Order

readconf = readconfig.ReadConfig()
host = readconf.get_database('host')
user = readconf.get_database('user')
passwd = readconf.get_database('passwd')
db = 'auto_order'
dbaddress = 'mysql+pymysql://{}:{}@{}/{}?charset=utf8'.format(user, passwd, host, db)
engine=create_engine(dbaddress)
Session=sessionmaker(bind=engine)
session=Session()


# 增加
obj = Order(name="test1", extra='ex1')
session.add(obj)
session.add_all([
    Order(name="test2", extra='ex2'),
    Order(name="test3", extra='ex3'),
])
session.commit()

#删除
session.query(Order).filter_by(Order.id==1).delete()
session.query(Order).filter_by(Order.id>1).delete()

# 改
session.query(Order).filter(Order.id > 2).update({"car_id" : "0"})
session.commit()

ret = session.query(Order).all()
ret = session.query(Order.id, Order.order_no).all()
ret = session.query(Order).filter_by(id=1).all()
ret = session.query(Order).filter_by(id=1).first()