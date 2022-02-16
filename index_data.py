# # -*- coding: utf-8 -*-
# """
# edited on 1400/11/10 ---- 01/30/2022
#
# @author: mahmoud esmaeili
# """
from bs4 import BeautifulSoup
import requests
import functions

#----------------------------------csv شاخص ها به صورت فایل-------ok-----------------------------------------

# -----------------------------------------------------------------------------------------
def get_indices(id):
    # url='http://www.tsetmc.com/tsev2/chart/data/Index.aspx?i=32097828799138957&t=value'
    # http: // www.tsetmc.com / tsev2 / chart / data / Index.aspx?i = 43685683301327984 & t = value
    url='http://www.tsetmc.com/tsev2/chart/data/Index.aspx?i=%i&t=value'%id
    get_data=requests.get(url)
    index_data = functions.Reverse(get_data.content.decode('utf-8').split(';'))
    # print(index_data)
    # index_items = index_data
    # for item in index_items:
    #    index_items=item.split(',')
    #    # print(index_items)
    return index_data

def get_index(data):
    index_data=data
    index = []
    try:
        for item in index_data:
            index_items = item.split(',')

            index.append( dict(
                index_time=index_items[0],
                index_value=index_items[1]
            ))
    except:pass
    return index
# ------------------------------------------------------
# ------------------------------------------------------
kool_bourse_id=32097828799138957
kool_hamvazn_id=67130298613737946
kool_fara_id=43685683301327984
vazni_id=5798407779416661
gheymat_id=8384385859414435
big30co_id=10523825119011581
best50co_id=69932667409721265
# ------------------------------------------------------
kool_index = get_indices(kool_bourse_id)
kool_last_time = kool_index[0].split(',')[0]
kool_last_value = functions.convert(kool_index[0].split(',')[1])
kool_yesterday_time = kool_index[1].split(',')[0]
kool_yesterday_value = functions.convert(kool_index[1].split(',')[1])
kool_change = kool_last_value - kool_yesterday_value
kool_percent = round(kool_change/kool_yesterday_value*100,2)
kool_all = get_index(kool_index)# all data of index

hamvazn_index = get_indices(kool_hamvazn_id)
hamvazn_last_time = hamvazn_index[0].split(',')[0]
hamvazn_last_value = functions.convert(hamvazn_index[0].split(',')[1])
hamvazn_yesterday_time = hamvazn_index[1].split(',')[0]
hamvazn_yesterday_value = functions.convert(hamvazn_index[1].split(',')[1])
hamvazn_change = hamvazn_last_value - hamvazn_yesterday_value
hamvazn_percent = round(hamvazn_change/hamvazn_yesterday_value*100,2)
hamvazn_all = get_index(hamvazn_index)# all data of index

fara_index = get_indices(kool_fara_id)
fara_last_time = fara_index[0].split(',')[0]
fara_last_value = functions.convert(fara_index[0].split(',')[1])
fara_yesterday_time = fara_index[1].split(',')[0]
fara_yesterday_value = functions.convert(fara_index[1].split(',')[1])
fara_change = fara_last_value - fara_yesterday_value
fara_percent = round(fara_change/fara_yesterday_value*100,2)
fara_all = get_index(fara_index)# all data of index

vazni_index = get_indices(vazni_id)
vazni_last_time = vazni_index[0].split(',')[0]
vazni_last_value = functions.convert(vazni_index[0].split(',')[1])
vazni_yesterday_time = vazni_index[1].split(',')[0]
vazni_yesterday_value = functions.convert(vazni_index[1].split(',')[1])
vazni_change = vazni_last_value - vazni_yesterday_value
vazni_percent = round(vazni_change/vazni_yesterday_value*100,2)
vazni_all = get_index(vazni_index)# all data of index

gheymat_index = get_indices(gheymat_id)
gheymat_last_time = gheymat_index[0].split(',')[0]
gheymat_last_value = functions.convert(gheymat_index[0].split(',')[1])
gheymat_yesterday_time = gheymat_index[1].split(',')[0]
gheymat_yesterday_value = functions.convert(gheymat_index[1].split(',')[1])
gheymat_change = gheymat_last_value - gheymat_yesterday_value
gheymat_percent = round(gheymat_change/gheymat_yesterday_value*100,2)
gheymat_all = get_index(gheymat_index)# all data of index

big30co_index = get_indices(big30co_id)
big30co_last_time = big30co_index[0].split(',')[0]
big30co_last_value = functions.convert(big30co_index[0].split(',')[1])
big30co_yesterday_time = big30co_index[1].split(',')[0]
big30co_yesterday_value = functions.convert(big30co_index[1].split(',')[1])
big30co_change = big30co_last_value - big30co_yesterday_value
big30co_percent = round(big30co_change/big30co_yesterday_value*100,2)
big30co_all = get_index(big30co_index)# all data of index

best50co_index = get_indices(best50co_id)
best50co_last_time = best50co_index[0].split(',')[0]
best50co_last_value = functions.convert(best50co_index[0].split(',')[1])
best50co_yesterday_time = best50co_index[1].split(',')[0]
best50co_yesterday_value = functions.convert(best50co_index[1].split(',')[1])
best50co_change = best50co_last_value - best50co_yesterday_value
best50co_percent = round(best50co_change/best50co_yesterday_value*100,2)
best50co_all = get_index(best50co_index)# all data of index
##----------------------------------csv شاخص ها به صورت فایل-----------------ok-----------------------------
index_items = {}
index_items = dict(
    last_time = [kool_last_time,hamvazn_last_time,fara_last_time,gheymat_last_time,big30co_last_time,best50co_last_time],
    last_value = [kool_last_value,hamvazn_last_value,fara_last_value,gheymat_last_value,big30co_last_value,best50co_last_value],
    yesterday_time = [kool_yesterday_time,hamvazn_yesterday_time,fara_yesterday_time,gheymat_yesterday_time,big30co_yesterday_time,best50co_yesterday_time],
    yesterday_value = [kool_yesterday_value ,hamvazn_yesterday_value ,fara_yesterday_value ,gheymat_yesterday_value,big30co_yesterday_value ,best50co_yesterday_value],
    change = [kool_change,hamvazn_change,fara_change,gheymat_change,big30co_change,best50co_change],
    percent = [kool_percent,hamvazn_percent,fara_percent,gheymat_percent,big30co_percent,best50co_percent],
    history = [kool_all,hamvazn_all,fara_all,gheymat_all,big30co_all,best50co_all]
)

##----------------------------------csv شاخص ها به صورت فایل-----------------ok-----------------------------

# print(kool_index)
# print(kool_last_time)
# print(kool_last_value)
# print(kool_yesterday_time)
# print(kool_yesterday_value)
# print(kool_change)
# print(kool_percent)
# print(kool_all)

# print(index_items.get('percent')[2])
##----------------------------------dayli شاخص ها----------------------------ok-----------------------------

url2 = "https://www.fipiran.ir/Home/_TopIndex"
index_list = []
get_page = requests.get(url2)
page_soup = BeautifulSoup(get_page.content, 'html.parser')
index_items = page_soup.find_all('h6')

for item in index_items:
    index_list.append(item.text)
# print(index_list)
# for item in index_list:
#     print(item)
day_time=(index_list[0]).split('/')
# print(day_time)
kool_last_time = kool_last_time.split('/')
# print(kool_last_time)
# print(day_time[2])
# print(kool_last_time[2])

last_kool_value = 0
last_hamvazn_value = 0
last_fara_value = 0
last_vazni_value = 0
last_gheymat_value = 0
last_big30co_value = 0
last_best50co_value = 0
if int(day_time[2]) == int(kool_last_time[2]):
    last_kool_value = kool_yesterday_value
    last_hamvazn_value = hamvazn_yesterday_value
    last_fara_value = fara_yesterday_value
    last_vazni_value = vazni_yesterday_value
    last_gheymat_value = gheymat_yesterday_value
    last_big30co_value = big30co_yesterday_value
    last_best50co_value = best50co_yesterday_value


time = index_list[0]
kool = index_list[4].split()[0]
kool_change = functions.convert(index_list[4].split()[0]) - last_kool_value
kool_percent = index_list[4].split()[1]

hamvazn = index_list[6].split()[0]
hamvazn_change = functions.convert(index_list[6].split()[0]) - last_hamvazn_value
hamvazn_percent = index_list[6].split()[1]

fara = index_list[5].split()[0]
fara_change = functions.convert(index_list[5].split()[0]) - last_fara_value
fara_percent = index_list[5].split()[1]

vazni = index_list[1].split()[0]
vazni_change = functions.convert(index_list[1].split()[0]) - last_vazni_value
vazni_percent = index_list[1].split()[1]

gheymat = index_list[2].split()[0]
gheymat_change = functions.convert(index_list[2].split()[0]) - last_gheymat_value
gheymat_percent = index_list[2].split()[1]

big30co = index_list[3].split()[0]
big30co_change = functions.convert(index_list[3].split()[0]) - last_big30co_value
big30co_percent = index_list[3].split()[1]

best50co = index_list[7].split()[0]
best50co_change = functions.convert(index_list[7].split()[0]) - last_best50co_value
best50co_percent = index_list[7].split()[1]

index_now = {}
index_now = {
    'last_time' : time,
    'last_value' : [kool,hamvazn,fara,vazni,gheymat,big30co,best50co],
    'change' : [kool_change,hamvazn_change,fara_change,vazni_change,gheymat_change,big30co_change,best50co_change],
    'percent' : [kool_percent,hamvazn_percent,fara_percent,gheymat_percent,big30co_percent,best50co_percent],
}

# print(index_now.get('last_value'))





##----------------------------------dayli شاخص ها----------------------------ok-----------------------------
# -----------------------------------index_data-----------------------------ok-----------------------------
# import os
# from winsound import Beep
# import time
# import datetime
#
# # time.sleep(1)
# Beep(2000,100)
# print('index_data:executed.')
#
# t = datetime.datetime.now()
# print(t.minute,':', t.second,':',str(t.microsecond)[:2])