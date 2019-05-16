# -*-conding:utf-8-*-
# @author:wangchengyuan
# @time:2019/3/14 5:30 PM
# @desc:获取股票列表，并写入excel表格中


import xlrd
import xlwt
import os
from xlutils.copy import copy
import requests
import re

proDir = os.path.dirname(__file__)

class GetStockList():


    def __init__(self):
        self.stocklistdir = os.path.join(proDir, 'stocklist.xls')
        self.sheetinfo=['股票名称','股票编号']
        self.sheetmap = {'sz': 0, 'sh': 1, 'cy': 2}  #工作表序列与交易所缩写映射关系
        self.filtermap={'sz': '00', 'sh': '60', 'cy': '30'} #过滤数据与交易所缩写映射关系
        self.url='http://quote.eastmoney.com/stocklist.html'
        if os.path.exists(self.stocklistdir):
            print("文件已存在")
            exit()
        else:
            self.excel_create('深证', '上证', '创业板')

    #生成excel表方法
    def excel_create(self, *args):
        workbook = xlwt.Workbook(encoding='utf-8')
        for list in args:
            worksheet = workbook.add_sheet(list)
            for id in range(0, len(self.sheetinfo)):
                worksheet.write(0, id, self.sheetinfo[id])
        workbook.save(self.stocklistdir)

    def write_stock_info(self,exchangeName, list):
        sheetindex = self.sheetmap[exchangeName]
        rb = xlrd.open_workbook(self.stocklistdir)
        rs = rb.sheet_by_index(sheetindex)
        n = rs.nrows
        wb = copy(rb)
        ws = wb.get_sheet(sheetindex)
        for i in range(0, len(list)):
            for j in range(len(list[i])):
                ws.write(i + n, j, list[i][j])
        wb.save(self.stocklistdir)

    def get_stock_list(self,exchangeName):
        stocklist = []
        filtername = self.filtermap[exchangeName]
        ##获取抓取页页面内容
        resp = requests.get(self.url)
        resp.encoding = 'gbk'
        stockcontent = resp.text
        ##定义正则表达式，过滤数据
        ret = 'href=".*?">(.*?)\((.*?)\)<'
        recontent = re.findall(ret, stockcontent)
        for recon in recontent:
            if recon[1].startswith(filtername):
                stocklist.append(recon)
            else:
                pass
        ##调用写入方法，写入对应板块股票信息
        if len(stocklist) > 0:
            print("开始写入%s板块的股票信息" % exchangeName)
            self.write_stock_info(exchangeName, stocklist)
            print("写入%s板块股票信息结束" % exchangeName)
        else:
            print("没有抓取到数据")


if __name__=='__main__':
    getstocklisttest=GetStockList()
    getstocklisttest.get_stock_list('sz')
    getstocklisttest.get_stock_list('sh')
    getstocklisttest.get_stock_list('cy')

