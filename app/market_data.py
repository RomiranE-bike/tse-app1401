# -*- coding: utf-8 -*-
"""
edited on 1400/11/14 ---- 02/04/2022

@author: mahmoud esmaeili
"""

import requests
import functions

#---------------------market_list  all stock data with id and name and other info--------ok------------------
def get_market_list():
    url1='http://www.tsetmc.com/tsev2/data/MarketWatchPlus.aspx'
    get_data=requests.get(url1)
    stock_data = get_data.content.decode('utf-8').split('@')
    # print(stock_data)
    # qeueu_items = stock_data[3].split(';')#ردیف های سفارش خرید و فروش#
    stock_items = stock_data[2].split(';')#نمای بازار روز#
    # print(stock_items[0])
    # print(qeueu_items)
    market_list = []

    for i in range(len(stock_items)):
        stock_info = stock_items[i].split(',')
        close_price = functions.chang_num(stock_info[6])
        last_price = functions.chang_num(stock_info[7])
        yesterday_price = functions.chang_num(stock_info[13])
        if yesterday_price != 0:
            close_percent = round((close_price - yesterday_price) / yesterday_price * 100, 2)
            last_percent = round((last_price - yesterday_price) / yesterday_price * 100, 2)

        eps = functions.chang_num(stock_info[14])
        pe = 0
        # print(eps, type(eps))
        try:
            if eps != 0 or eps is not none:
                pe = round(last_price / eps, 2)
        except:pass

        if pe != 0 and last_percent < 20 and last_percent > -20:
            market_list.append(dict(
                symbol=stock_info[2],
                group_id=stock_info[18],
                close_price=close_price,
                close_percent=close_percent,
                last_price=last_price,
                last_percent=last_percent,
                count=stock_info[8],
                volume=stock_info[9],
                value=stock_info[10],
                first_price=stock_info[5],
                yesterday_price=yesterday_price,
                min_traded_price=stock_info[11],
                max_treaded_price=stock_info[12],
                max_allowed_price=stock_info[19],
                min_allowed_price=stock_info[20],
                eps=eps,
                pe=pe,
                base_volume=stock_info[15],
                c2=stock_info[16],
                table_id=stock_info[17],
                id=stock_info[0],
                name=stock_info[3],
                code=stock_info[1],
                type_of_symbol=stock_info[22],
                all_count_of_symbol=stock_info[21]

            ))

    return market_list


# ------------------------------------------get average of key-----------------------------------
def get_average(list,key):
    key_list=[]
    average_key = 0
    sum_key=0
    sum_len=0
    for dict in list:
        item=dict.get(key)
        # create list of key
        key_list.append(item)
        # sum of key value
        sum_key += item
        sum_len += 1
    if sum_len != 0:
       average_key = round(sum_key/sum_len ,2)
    return average_key,key_list
# ------------------------------------------get average of key-----------------------------------

# ------------------------------------market find best stock by best p/e    ----------------------
def get_market_best_pe():
    market_best_pe_list=[]
    market_pe=0
    for dict in market_list:
        try:
            pe=dict.get('pe')
            if pe > 1 and pe < 8:
                market_best_pe_list.append(dict)
        except:
             print('error market best co list!')
        pass
    return market_best_pe_list

# ------------------------------------market find best stock by best p/e    ----------------------
# ---------------------------------------------market find sign   --------------------------------
def get_sign(list,key):
    negetive_list = []
    posetive_list = []
    negetive_items = []
    posetive_items = []

    for dict in list:
        try:
            key_item = dict.get(key)
            # print(key_item)
            if  key_item < 0:
                negetive_list.append(dict)
                negetive_items.append(key_item)
            if  key_item >= 0:
                posetive_list.append(dict)
                posetive_items.append(key_item)
        except:print('error market neg or pos list!')
        pass
    return negetive_list ,posetive_list ,negetive_items ,posetive_items
# ---------------------------------------------market find sign   --------------------------------
# ----------------------------------------------get market data ----------------------------------
market_list = get_market_list()
# print(market_list[0])
# print(market_list[0].get('eps'))

# client_dict_list = get_client_info()
# print(client_dict_list[0])
# # print(client_dict_list[0].get('haghighi_buy_volume'))
# ----------------------------------------get gruop name and gruop code----------------------------

def set_group_list(code):
    group_list = []
    group_code = code

    # print('group_code is;',group_code)
    for dict in market_list:
        group_id = dict.get('group_id')
        # print(group_id,dict)
        if  int(group_id) is group_code:
                # print(dict,)
                group_list.append(dict)
    return group_list

# --------------------------------------------market average p/e ---------------------------------
market_average_pe = get_average(market_list,'pe')
# print(market_average_pe[0])
# print(len(market_average_pe[1]))
# ----------------------------------------------market best p/e ---------------------------------
market_best_pe_list = get_market_best_pe()
# for i in range(len(market_best_pe_list)):
#      print(market_best_pe_list[i])

market_sign = get_sign(market_list,'last_percent')
market_negetive_list = market_sign[0]
market_posetive_list = market_sign[1]
market_negetive_percent = market_sign[2]
market_posetive_percent = market_sign[3]
# #
# print(market_negetive_list)
# print(market_posetive_list)
# print(market_negetive_percent)
# print(market_posetive_percent)

# -------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------

import os
from winsound import Beep
import time
import datetime

# time.sleep(1)
Beep(2000,100)
print('market_data:executed.')

t = datetime.datetime.now()
print(t.minute,':', t.second,':',str(t.microsecond)[:2])
