# -*-conding:utf-8-*-
# @author:wangchengyuan
# @time:2019/3/14 4:44 PM
# @desc:

import re
import requests
import xlwt
import xlrd
import os
import time
from wcy.bin.readconfig import ReadConfig
from xlutils.copy import copy

proDir = os.path.dirname(__file__)
date = time.strftime("%Y%m%d")


class GetStockData():

    def __init__(self):
        self.rfconfig = ReadConfig()
        self.stocklistdir = os.path.join(proDir, 'stocklist.xls')
        self.stockinfodir = os.path.join(proDir, date + 'stockinfo.xls')
        self.sheetinfo = ['股票编号', '股票名称', '今日开盘价', '昨日收盘价', '当前价格', '今日最高价', '今日最低价', '成交的股票数', '成交金额']
        self.sheetmap = {'sz': 0, 'sh': 1, 'cy': 2}  # 工作表与序列映射关系
        # 判断文件是否存在，不存在创建当天的excel表（多个工作表）
        if os.path.exists(self.stockinfodir):
            print("文件已存在")
            exit()
        else:
            self.excel_create('深证', '上证', '创业板')

    # 生成excel表方法
    def excel_create(self, *args):
        workbook = xlwt.Workbook(encoding='utf-8')
        for list in args:
            worksheet = workbook.add_sheet(list)
            for id in range(0, len(self.sheetinfo)):
                worksheet.write(0, id, self.sheetinfo[id])
        workbook.save(self.stockinfodir)

    # 数据写入excel表方法
    def write_stock_info(self, exchangeName, list):
        sheetindex = self.sheetmap[exchangeName]
        rb = xlrd.open_workbook(self.stockinfodir)
        rs = rb.sheet_by_index(sheetindex)
        n = rs.nrows
        wb = copy(rb)
        ws = wb.get_sheet(sheetindex)
        for i in range(0, len(list)):
            for j in range(len(list[i])):
                ws.write(i + n, j, list[i][j])
        wb.save(self.stockinfodir)

    ##读取股票列表数据,n为一次请求股票数量，exchangeName为券商简称
    def read_stocklist(self, n, exchangeName):
        sheetindex = self.sheetmap[exchangeName]
        stockno3 = []
        ##读取对应excel对应工作表数据
        workbook = xlrd.open_workbook(self.stocklistdir)
        worksheet = workbook.sheet_by_index(sheetindex)
        stockno = worksheet.col_values(1)
        stockno.remove('股票编号')
        if exchangeName != 'cy':
            stockno2 = [exchangeName + i for i in stockno]
        else:
            stockno2 = ['sz' + i for i in stockno]

        for i in range(0, len(stockno2) // n + 1):
            stockno3.append(stockno2[i * n:(i + 1) * n])
        return stockno3

    # 获取股票数据，n一次请求股票数量，exchangeName为券商简称
    def get_stock_data(self, n, exchangeName):
        stockinfo = self.read_stocklist(n, exchangeName)
        for datas in stockinfo:
            listdata = []
            url = 'http://hq.sinajs.cn/list='
            for data in datas:
                url = url + data + ','
            resp = requests.get(url)
            if exchangeName == 'cy':
                ret = 'str_sz(.*?)=\"(.*?)\"'
            else:
                ret = 'str_%s(.*?)=\"(.*?)\"' % exchangeName
            recontent = re.findall(ret, resp.text)
            for rec in recontent:
                listdata.append(rec[0] + ',' + rec[1])
            liststockdata = [i.split(',')[0:7] + i.split(',')[9:11] for i in listdata]
            # print(liststockdata)
            # print("=======================")
            self.write_stock_info(exchangeName, liststockdata)


if __name__ == '__main__':
    getdatatest = GetStockData()
    print("开始抓取sz数据")
    getdatatest.get_stock_data(50, 'sz')
    print("抓取sz数据结束")
    print("开始抓取sh数据")
    getdatatest.get_stock_data(50, 'sh')
    print("抓取sh数据结束")
    print("开始抓取cy数据")
    getdatatest.get_stock_data(50, 'cy')
    print("抓取cy数据结束")
