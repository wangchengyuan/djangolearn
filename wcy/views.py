from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from wcy.bin.readstocklist import ReadStockData
import json

import time
# Create your views here.

def current_datetime(request):
    datetime=time.strftime('%Y-%m-%d %H:%M:%S')
    html="<html><body>%s</body></html>" %datetime
    return HttpResponse(html)


def get_stock_data(request):
    getdata=ReadStockData()
    stocklists,stocklisttitles=getdata.readstocklist(30,'sz')
    stockdatas,stockdatatitles=getdata.readstockdata(30,'sz')
    return render(request,'stocklist.html',{'stocklists':stocklists,'stockdatas':stockdatas,'stocklisttitles':stocklisttitles,'stockdatatitles':stockdatatitles})



