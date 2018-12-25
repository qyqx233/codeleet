import typing
import tushare as ts

ts.set_token('cc905670ba914cf0e6b89a98d5b2058ce373945f52d22cf483f0b648')
pro = ts.pro_api()


data = pro.stock_basic(exchange='', list_status='L',
                       fields='ts_code,symbol,name,area,industry,list_date')
