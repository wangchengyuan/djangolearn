# -*-conding:utf-8-*-
# @author:wangchengyuan
# @time:2019/3/27 11:00 AM
# @desc:

from wcy.sqldao.modelfiles.helper_auto_order import Helper_auto_order
from wcy.sqldao.modelfiles.helper_auto_product import Helper_auto_product
from wcy.sqldao.modelfiles.auto_order.orders import Order
from wcy.sqldao.modelfiles.auto_order.order_amount_items import OrderAmountItem
from wcy.sqldao.modelfiles.auto_product.cars import Car
from wcy.sqldao.modelfiles.auto_product.car_license_plates import CarLicensePlate


# 修改订单金额为0.01，方便下单
def update_order_amount(orderid):
    dbhelper = Helper_auto_order()
    session = dbhelper.get_session()
    # 修改order_amount_items中数据
    acts = session.query(OrderAmountItem).filter(OrderAmountItem.order_id == orderid).all()
    for act in acts:
        act.item_amount = 0
    # 修改orders表中数据
    orderact = session.query(Order).filter_by(id=orderid).one()
    orderact.down_payment = 0.01
    orderact.deposit = 0
    orderact.break_amount = 0
    dbhelper.close_session()
    print("数据修改完成")


## 查看车辆的车架号和车牌号
def get_car_info(carid):
    dbhelper = Helper_auto_product()
    session = dbhelper.get_session()
    act1 = session.query(Car).filter(Car.id == carid).one()
    act2 = session.query(CarLicensePlate).filter(CarLicensePlate.car_id == carid).one()
    print("车架号：" + act1.frame_no)
    print("车牌号：" + act2.license_plate_prefix + act2.license_plate)
    dbhelper.close_session()


## 查看车辆的车架号和车牌号
def testget_car_info(carid):
    dbhelper = Helper_auto_product()
    session = dbhelper.get_session()
    act1 = session.query(Car)
    print(type(act1))
    print(act1)


## 解绑车辆与订单之间关系
def unbind_order_car(carid):
    dbhelper_product = Helper_auto_product()  #清除car表中的绑定关系
    session_product = dbhelper_product.get_session()
    act_product = session_product.query(Car).filter(Car.id==carid).all()
    for act_p in act_product:
        act_p.order_id=0
        act_p.order_no=''
        act_p.status=3
        act_p.hosting_status=3
    dbhelper_product.close_session()
    print("清除car表中的绑定关系已结束")
    dbhelper_order = Helper_auto_order() #清除order表中的绑定关系
    session_order=dbhelper_order.get_session()
    act_order=session_order.query(Order).filter(Order.car_id==carid).all()
    for act_o in act_order:
        act_o.car_id=0
    dbhelper_order.close_session()
    print("清除order表中的绑定关系已结束")


if __name__ == '__main__':
    choose = input("选择修改订单选择：1，选择查询车辆信息选择：2 , 解除订单车辆绑定关系：3 \n ")
    #choose = '3'
    if choose == '1':
        orderid = input("请输入你的订单ID： ")
        update_order_amount(orderid)
    elif choose == '2':
        carid = input("请输入你的车辆ID： ")
        get_car_info(carid)
    elif choose == '3':
        carid = input("请输入你的车辆ID： ")
        unbind_order_car(carid)
    else:
        carid = input("请输入你的车辆ID： ")
        testget_car_info(carid)
