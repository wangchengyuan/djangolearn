# -*-conding:utf-8-*-
# @author:wangchengyuan
# @time:2019/3/21 11:53 AM
# @desc:


import xlrd
import os

proDir = os.path.dirname(os.path.dirname(__file__))


class ReadStockData():

    def __init__(self):
        self.stocklistdir = os.path.join(proDir, 'stockdatas/stocklist.xls')
        self.stockdatadir = os.path.join(proDir, 'stockdatas/20190321stockinfo.xls')
        self.sheetmap = {'sz': 0, 'sh': 1, 'cy': 2}  # 工作表序列与交易所缩写映射关系
        self.stocklist = xlrd.open_workbook(self.stocklistdir)
        self.stockdata = xlrd.open_workbook(self.stockdatadir)

    # 读取股票列表数据
    def readstocklist(self, n, exchangeName):
        datas = []
        n = n + 1
        worksheet = self.stocklist.sheet_by_index(self.sheetmap[exchangeName])
        for i in range(0, n):
            if worksheet.row_values(i)[0] == '股票名称':
                titles = worksheet.row_values(i)
            else:
                datas.append(worksheet.row_values(i))
        return datas, titles

    # 读取股票信息
    def readstockdata(self, n, exchangeName):
        datas = []
        n = n + 1
        worksheet = self.stockdata.sheet_by_index(self.sheetmap[exchangeName])
        for i in range(0, n):
            if worksheet.row_values(i)[0] == '股票编号':
                titles = worksheet.row_values(i)
            else:
                datas.append(worksheet.row_values(i))
        return datas, titles
