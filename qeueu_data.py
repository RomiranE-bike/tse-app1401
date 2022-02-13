# # -*- coding: utf-8 -*-
# """
# edited on 1400/11/14 ---- 02/04/2022
#
# @author: mahmoud esmaeili
# """

import requests
import functions
from market_data import*

#---------------------market_list  all stock data with id and name and other info--------ok------------------
def get_qeueu_list():
    url1='http://www.tsetmc.com/tsev2/data/MarketWatchPlus.aspx'
    get_data=requests.get(url1)
    stock_data = get_data.content.decode('utf-8').split('@')
    # print(stock_data)
    qeueu_items = stock_data[3].split(';')#ردیف های سفارش خرید و فروش#
    # print(qeueu_items)
    qeueu_list = []
    for i in range(len(qeueu_items)):
        qeueu_info = qeueu_items[i].split(',')
        id = int(qeueu_info[0])
        radif = int(qeueu_info[1])
        seller = int(qeueu_info[2])
        buyer = int(qeueu_info[3])
        buyer_price = functions.chang_num(qeueu_info[4])
        seller_price = functions.chang_num(qeueu_info[5])
        buyer_vol = functions.chang_num(qeueu_info[6])
        seller_vol = functions.chang_num(qeueu_info[7])
        buyer_val =  round(buyer_price*buyer_vol,2)
        seller_val = round(seller_price*seller_vol,2)

        qeueu_list.append(dict(
                id = id,
                radif = radif,
                buyer = buyer,
                seller = seller,
                buyer_price = buyer_price,
                seller_price = seller_price,
                buyer_vol = buyer_vol,
                seller_vol = seller_vol,
                buyer_val = buyer_val,
                seller_val = seller_val
        ))

    return qeueu_list

qeueu_list = get_qeueu_list()

# for item in qeueu_list:
#     print(item)
# ----------------------------------------------------------------------------------------

def set_stock_qeueu_list():
    radif_list = []
    stock_qeueu_list = {}
    for dict in market_list:
        stock_id = dict.get('id')
        symbol = dict.get('symbol')
        for item in qeueu_list:
            qeueu_id = item.get('id')
            if int(stock_id) == qeueu_id:
               item.update({'symbol': symbol})
               if item.get('radif') == 1 :
                  radif_list.append(item)

    return   radif_list
# -----------------------------------------------------------------------------------------

radif_list = set_stock_qeueu_list()
# print(radif_list)
# -----------------------------------------------------------------------------------------
buyer_qeueu = []
seller_qeueu = []
buyer_qeueu.append([item for item in radif_list if item['buyer_vol'] >= 1000000])
seller_qeueu.append([item for item in radif_list if item['seller_vol'] >= 1000000])

# print(buyer_qeueu[0])
# print(seller_qeueu[0])
# ------------------------------------------------------------------------------------------
buyer_sum_val = 0
seller_sum_val = 0
for item in qeueu_list:
    buyer_sum_val += item.get('buyer_val')
    seller_sum_val += item.get('seller_val')
power_qeueu_val = round(buyer_sum_val/seller_sum_val,3)

# print(buyer_sum_val)
# print(seller_sum_val)
# print(power_qeueu_val)

# -------------------------------------------------------------------------------------------
qeueu_items = {
    'radif_list' : radif_list,
    'buyer_qeueu' : buyer_qeueu[0],
    'seller_qeueu' : seller_qeueu[0],
    'buyer_sum_val' : round(buyer_sum_val/10000000000,2),
    'seller_sum_val' : round(seller_sum_val/10000000000,2),
    'power_qeueu_val' : power_qeueu_val
}

# --------------------------------------------------------------------------------------------
# for k,v in qeueu_items.items():
#     print(k ,' is:',v)

# --------------------------------------------------------------------------------------------
import os
from winsound import Beep
import time
import datetime

# time.sleep(1)
Beep(2000,100)
print('qeueu_data:executed.')

t = datetime.datetime.now()
print(t.minute,':', t.second,':',str(t.microsecond)[:2])