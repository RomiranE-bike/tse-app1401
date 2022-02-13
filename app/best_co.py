# -*- coding: utf-8 -*-
"""
Created on 1400/10/06 ---- 12/27/2021

@author: mahmoud esmaeili
"""

from bs4 import BeautifulSoup
import requests
import functions



url3 = "http://www.tsetmc.com/Loader.aspx?Partree=15131O"

# --------------------------------- best co data function------------------------------------------------

scrap_result = []
def scrap_data (url,tag,id):
    get_page = requests.get(url)
    page_soup = BeautifulSoup(get_page.content, 'html.parser')
    page_items = page_soup.find(tag , id=id)

    for item in page_items.find_all('td'):
        try:
            scrap_result.append(item.text)
        except:
            scrap_result.append('item not fount')
            print('error item not fount!')
        pass
    return scrap_result


best_co = scrap_data(url3,'span','PureData')

# print(best_co_data1)

# ------------------------------ best co data -------------------------------------
best_co_data=[best_co[i:i + 5] for i in range(0, len(best_co), 5)]

# print(best_co_data[0][4])

#------------------------ best co lists -------------------------
group_name = [(best_co_data[i][0]) for i in range(len(best_co_data))]
market_value = [(best_co_data[i][1]) for i in range(len(best_co_data))]
trade_count = [(best_co_data[i][2]) for i in range(len(best_co_data))]
trade_vol = [(best_co_data[i][3]) for i in range(len(best_co_data))]

trade_value_temp = [(best_co_data[i][4]) for i in range(len(best_co_data))]



trade_value=[]
for i in range(len(trade_value_temp)):
    int_num=functions.chang_num(trade_value_temp[i])
    trade_value.append(int_num)

# print(trade_value_temp)
# print(trade_value)
#
# print(type(trade_value))

# for i in range(len(trade_value)):
#       print(trade_value[i])

# ---------------------------------best co dict-------------------------------------------
best_co_dict = {}
best_co_dict = dict(
    group_name= group_name,
    market_value= market_value,
    trade_count= trade_count,
    trade_vol = trade_vol,
    trade_value= trade_value
)

# for key, value in best_co_dict.items():
#     print(key,'',':','', value)
best_group_list=[]
best_group_value=[]
# print(group_name)
try:
    for i in range(1,11):
        best_group_list.append(group_name[i])
        best_group_value.append(trade_value[i])
except:pass

top_ten_co={}
top_ten_co=dict(
    best_group_list=best_group_list,
    best_group_value=best_group_value
)

# print(best_co_dict)
# print(best_group_list)
# print(top_ten_co)
# print(top_ten_co.get('best_group_value'))

# -----------------------------------------------------------------------------------

import os
from winsound import Beep
import time
import datetime

# time.sleep(1)
Beep(2000,100)
print('best_co:executed.')

t = datetime.datetime.now()
print(t.minute,':', t.second,':',str(t.microsecond)[:2])