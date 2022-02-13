# # -*- coding: utf-8 -*-
# """
# edited on 1400/11/09 ---- 01/29/2022
#
# @author: mahmoud esmaeili
# """

from market_data import*
from group_selected import*
from functions import*
from best_co import*

# ----------------------------------------------------------------------------
# --------------------------------------------get_client_info------------------------------------
def get_client_info():
    url2 = 'http://www.tsetmc.com/tsev2/data/ClientTypeAll.aspx'
    get_data = requests.get(url2)
    client_info_data = get_data.content.decode('utf-8').split(';')
    # print(client_info_data)
    client_dict_list = []
    hot_money_list = []
    for i in range(len(client_info_data)):
        client_info = client_info_data[i].split(',')
        # print(client_info)
        id = client_info[0]
        haghighi_buy_count = functions.chang_num(client_info[1])
        haghighi_buy_volume = functions.chang_num(client_info[3])
        haghighi_sell_count = functions.chang_num(client_info[5])
        haghighi_sell_volume = functions.chang_num(client_info[7])
        hoghughi_buy_count = functions.chang_num(client_info[2])
        hoghughi_buy_volume = functions.chang_num(client_info[4])
        hoghughi_sell_count = functions.chang_num(client_info[6])
        hoghughi_sell_volume = functions.chang_num(client_info[8])
        client_dict_list.append(dict(
            id = id,
            haghighi_buy_count = haghighi_buy_count,
            haghighi_buy_volume = haghighi_buy_volume,
            # haghighi_buy_value = haghighi_buy_value,
            haghighi_sell_count = haghighi_sell_count,
            haghighi_sell_volume = haghighi_sell_volume,
            # haghighi_sell_value = haghighi_sell_value,
            hoghughi_buy_count = hoghughi_buy_count,
            hoghughi_buy_volume = hoghughi_buy_volume,
            hoghughi_sell_count = hoghughi_sell_count,
            hoghughi_sell_volume = hoghughi_sell_volume
        ))
    # print(len(market_list))
    # print(len(client_dict_list))

    for client_dict in client_dict_list:
        client_id = client_dict.get('id')
        # print('client_id;',client_id)
        for market_dict in market_list:
            for (key, value) in market_dict.items():
                if value == client_id:
                    symbol = market_dict.get('symbol')
                    last_price = market_dict.get('last_price')
                    last_percent = market_dict.get('last_percent')
                    group_id = market_dict.get('group_id')
                    saraneh_kharid = 0
                    saraneh_forsh = 0
                    power = 0
                    hot_money = 0
                    haghighi_buy_count = client_dict.get('haghighi_buy_count')
                    haghighi_buy_value = last_price * client_dict.get('haghighi_buy_volume')
                    haghighi_sell_count = client_dict.get('haghighi_sell_count')
                    haghighi_sell_value = last_price * client_dict.get('haghighi_sell_volume')
                    if haghighi_buy_count != 0:
                        saraneh_kharid = round((haghighi_buy_value / haghighi_buy_count) / 10000000, 2)
                        power = round((haghighi_sell_count / haghighi_buy_count), 2)
                    if haghighi_sell_count != 0:
                        saraneh_forsh = round((haghighi_sell_value / haghighi_sell_count) / 10000000, 2)

                    hot_money = round(saraneh_kharid - saraneh_forsh, 2)
                    if hot_money is not None and hot_money < 1000 and hot_money > -1000:

                        hot_money_list.append(dict(
                            symbol = symbol,
                            group_id = group_id,
                            last_price = last_price,
                            last_percent = last_percent,
                            saraneh_kharid = saraneh_kharid,
                            saraneh_forsh = saraneh_forsh,
                            power = power,
                            hot_money = hot_money ))
                        # print(client_dict)

    return hot_money_list


# --------------------------------------------get_client_info------------------------------------

# --------------------------------------------get hot money data ----------------------------------
hot_money_list = get_client_info()
# for dict in hot_money_list:
#     print(dict.get('hot_money'))
# print(hot_money_list[1] )
# -----------------------------------------market average hot_money ------------------------------
market_average_hotmoney = get_average(hot_money_list,'hot_money')
# print(market_average_hotmoney[0])
# print(len(market_average_hotmoney[1]))

# ----------------------------------------------------------------------------
def select_group(group_id):
    group_list = []
    group_list.append([item for item in hot_money_list if item['group_id'] == group_id])
    return group_list
# ----------------------------------------------------------------------------
group_hotmoney_name1 = best_group_list[0]
group_hotmoney_list1 = select_group(group_id_list[0])[0]
group_hotmoney_average1 = get_average(group_hotmoney_list1,'hot_money')
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
group_hotmoney_name2 = best_group_list[1]
group_hotmoney_list2 = select_group(group_id_list[1])[0]
group_hotmoney_average2 = get_average(group_hotmoney_list2,'hot_money')
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
group_hotmoney_name3 = best_group_list[2]
group_hotmoney_list3 = select_group(group_id_list[2])[0]
group_hotmoney_average3 = get_average(group_hotmoney_list3,'hot_money')
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
group_hotmoney_name4 = best_group_list[3]
group_hotmoney_list4 = select_group(group_id_list[3])[0]
group_hotmoney_average4 = get_average(group_hotmoney_list4,'hot_money')
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
group_hotmoney_name5 = best_group_list[4]
group_hotmoney_list5 = select_group(group_id_list[4])[0]
group_hotmoney_average5 = get_average(group_hotmoney_list5,'hot_money')
# ----------------------------------------------------------------------------
# print(group_hotmoney_name5)
# print(group_hotmoney_list5)
# print(group_hotmoney_average5[0])
# print(group_hotmoney_average5[1])
# ----------------------------------------------------------------------------
group_hotmoney_items = {}
group_hotmoney_items = dict(

    group_name = [group_hotmoney_name1,group_hotmoney_name2,group_hotmoney_name3,
                  group_hotmoney_name4,group_hotmoney_name5],
    group_hotmoney_list = [group_hotmoney_list1,group_hotmoney_list2,
                           group_hotmoney_list3,group_hotmoney_list4,group_hotmoney_list5],
    group_hotmoney_average = [group_hotmoney_average1,group_hotmoney_average2,
                              group_hotmoney_average3,group_hotmoney_average4,group_hotmoney_average5]
       )

# ----------------------------------------------------------------------------
# print(group_hotmoney_items.get('group_name')[0])
# print(group_hotmoney_items.get('group_hotmoney_average')[0][0])
# print(group_hotmoney_items.get('group_hotmoney_average')[0][1])
# print(group_hotmoney_items.get('group_hotmoney_list')[0][5].get('symbole'))
# print(group_hotmoney_items.get('group_hotmoney_list')[0][5].get('hot_money'))

# ----------------------------------------------------------------------------
import os
from winsound import Beep
import time
import datetime

# time.sleep(1)
Beep(2000,100)
print('hot_money_data:executed.')

t = datetime.datetime.now()
print(t.minute,':', t.second,':',str(t.microsecond)[:2])
# ---------------------------------------------------------------------------------------------------------