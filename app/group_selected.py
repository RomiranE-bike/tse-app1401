# # -*- coding: utf-8 -*-
# """
# edited on 1400/11/09 ---- 01/29/2022
#
# @author: mahmoud esmaeili
# """

import market_data
import best_co
import functions


# ------------------------------------------gat data from market_list------------------------------------
market_list = market_data.market_list
#top ten group list
best_group_list = best_co.best_group_list
#print(best_group_list)
# ------------------------------------------gat data from market_list------------------------------------
# --------------------------------------------find top ten group id -------------------------------------
def select_group(group_id):
    group_list = []
    group_list.append([item for item in market_list if item['group_id'] == group_id])
    return group_list
# -----------------------------------------find top ten group id code----------------------------------
# -----------------------------------------get top ten group id code-----------------------------------
def get_group_id():
    group_id_list = []
    for i in range(10):
         try:
        # split number fron string name of group
             group_id_list.append(functions.get_group_num(best_group_list[i]))
         except:
             # if group_id not found append 1 to list
             group_id_list.append(1)
             print('error_group_list not found')
         pass
    return group_id_list

group_id_list = get_group_id()
# print('group_id_list is;',group_id_list)
# ------------------------------------------get top ten group id code----------------------------------

# ------------------------------------------------sorting list ----------------------------------------
def sort(list,key):
    # sort by value
    sorted_list=sorted(list, key=lambda k : k[key],reverse=True)
    return sorted_list
# ------------------------------------------------bubblesort list -------------------------------------------
def bubblesort(list,key):
    # Looping from size of array from last index[-1] to index [0]
    sortlist=[]
    for n in range(len(list) - 1, 0, -1):
        for i in range(n):
            item1=list[i].get(key)
            item2=list[i + 1].get(key)
            if item2 > item1:
                # swapping data if the element is less than next element in the array
                list[i], list[i+1] = list[i+1], list[i]
    return list
# ------------------------------------------------sorting list -------------------------------------------
# ------------------------------------------------ average key -------------------------------------------
def average(list,key):
    key_list=[]
    average_key = 0
    sum_key=0
    sum_len=0
    for dict in list:
        item=dict.get(key)
        # create list of key
        key_list.append(item)
        # sum of key value
        if item != 0:
           sum_key += item
           sum_len += 1
    if sum_len != 0:
       average_key = round(sum_key/sum_len ,2)
    return average_key,key_list
# ------------------------------------------------ average key -------------------------------------------
# -------------------------------------------find best key of stock list ---------------------------------
def best_key(list,key,low,hig):
    best_key_list=[]
    for dict in list:
        item=dict.get(key)
        if item > low and item < hig:
            best_key_list.append(dict)
    return best_key_list
# -------------------------------------------find best key of stock list ---------------------------------
# -------------------------------------------neg or pos count of group-----------------------------------
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
        except:
                      print('error group neg or pos list!')
                      print(dict.get('symbole'))
        pass
    return negetive_list ,posetive_list ,negetive_items ,posetive_items
# -------------------------------------------neg or pos count of group-----------------------------------
# -----------------------------------------------get average of key--------------------------------------
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
# ----------------------------------------------get average of key---------------------------------------
# --------------------------------------------------group list1------------------------------------------
# ----------------------------------------------find sub group list1-------------------------------------
group_name1 = best_group_list[0]
group_list1 = select_group(group_id_list[0])[0]
group_sort_list1 = bubblesort(group_list1,'value')
group_sort_pe1 = bubblesort(group_list1,'pe')
group_sort_percent1 = bubblesort(group_list1,'last_percent')
group_pe_average1 = average(group_list1,'pe')[0]
group_pe_list1 = average(group_list1,'pe')[1]
group_best_pe_list1 = best_key(group_list1,'pe',1,15)
group_negetive_list1 = get_sign(group_list1,'last_percent')[0]
group_posetive_list1 = get_sign(group_list1,'last_percent')[1]
group_negetive_percent1 = get_sign(group_list1,'last_percent')[2]
group_posetive_percent1 = get_sign(group_list1,'last_percent') [3]
# -------------------------------------------find sub group list1----------------------------------------
# -------------------------------------------find sub group list2----------------------------------------
group_name2 = best_group_list[1]
group_list2 = select_group(group_id_list[1])[0]
group_sort_list2 = bubblesort(group_list2,'value')
group_sort_pe2 = bubblesort(group_list2,'pe')
group_sort_percent2 = bubblesort(group_list2,'last_percent')
group_pe_average2 = average(group_list2,'pe')[0]
group_pe_list2 = average(group_list2,'pe')[1]
group_best_pe_list2 = best_key(group_list2,'pe',1,15)
group_negetive_list2 = get_sign(group_list2,'last_percent')[0]
group_posetive_list2 = get_sign(group_list2,'last_percent')[1]
group_negetive_percent2 = get_sign(group_list2,'last_percent')[2]
group_posetive_percent2 = get_sign(group_list2,'last_percent')[3]
# -------------------------------------------find sub group list2----------------------------------------
# -------------------------------------------find sub group list3----------------------------------------
group_name3 = best_group_list[2]
group_list3 = select_group(group_id_list[2])[0]
group_sort_list3 = bubblesort(group_list3,'value')
group_sort_pe3 = bubblesort(group_list3,'pe')
group_sort_percent3 = bubblesort(group_list3,'last_percent')
group_pe_average3 = average(group_list3,'pe')[0]
group_pe_list3 = average(group_list3,'pe')[1]
group_best_pe_list3 = best_key(group_list3,'pe',1,15)
group_negetive_list3 = get_sign(group_list3,'last_percent')[0]
group_posetive_list3 = get_sign(group_list3,'last_percent')[1]
group_negetive_percent3 = get_sign(group_list3,'last_percent')[2]
group_posetive_percent3 = get_sign(group_list3,'last_percent') [3]
# -------------------------------------------find sub group list3----------------------------------------
# -------------------------------------------find sub group list4----------------------------------------
group_name4 = best_group_list[3]
group_list4 = select_group(group_id_list[3])[0]
group_sort_list4 = bubblesort(group_list4,'value')
group_sort_pe4 = bubblesort(group_list4,'pe')
group_sort_percent4 = bubblesort(group_list4,'last_percent')
group_pe_average4 = average(group_list4,'pe')[0]
group_pe_list4 = average(group_list4,'pe')[1]
group_best_pe_list4 = best_key(group_list4,'pe',1,15)
group_negetive_list4 = get_sign(group_list4,'last_percent')[0]
group_posetive_list4 = get_sign(group_list4,'last_percent')[1]
group_negetive_percent4 = get_sign(group_list4,'last_percent')[2]
group_posetive_percent4 = get_sign(group_list4,'last_percent') [3]
# -------------------------------------------find sub group list4----------------------------------------
# -------------------------------------------find sub group list5----------------------------------------
group_name5 = best_group_list[4]
group_list5 = select_group(group_id_list[4])[0]
group_sort_list5 = bubblesort(group_list5,'value')
group_sort_pe5 = bubblesort(group_list5,'pe')
group_sort_percent5 = bubblesort(group_list5,'last_percent')
group_pe_average5 = average(group_list5,'pe')[0]
group_pe_list5 = average(group_list5,'pe')[1]
group_best_pe_list5 = best_key(group_list5,'pe',1,15)
group_negetive_list5 = get_sign(group_list5,'last_percent')[0]
group_posetive_list5 = get_sign(group_list5,'last_percent')[1]
group_negetive_percent5 = get_sign(group_list5,'last_percent')[2]
group_posetive_percent5 = get_sign(group_list5,'last_percent') [3]
# -------------------------------------------find sub group list5----------------------------------------
# --------------------------------------find average of last percent-------------------------------------
group_list6 = select_group(group_id_list[5])[0]
group_list7 = select_group(group_id_list[6])[0]
group_list8 = select_group(group_id_list[7])[0]
group_list9 = select_group(group_id_list[8])[0]
group_list10 = select_group(group_id_list[9])[0]

average_percent1 = get_average(group_list1,'last_percent')[0]
average_percent2 = get_average(group_list2,'last_percent')[0]
average_percent3 = get_average(group_list3,'last_percent')[0]
average_percent4 = get_average(group_list4,'last_percent')[0]
average_percent5 = get_average(group_list5,'last_percent')[0]
average_percent6 = get_average(group_list6,'last_percent')[0]
average_percent7 = get_average(group_list7,'last_percent')[0]
average_percent8 = get_average(group_list8,'last_percent')[0]
average_percent9 = get_average(group_list9,'last_percent')[0]
average_percent10 = get_average(group_list10,'last_percent')[0]

average_percent = {}
average_percent={'average1': average_percent1,'average2':  average_percent2,'average3': average_percent3,
                 'average4': average_percent4,'average5': average_percent5,'average6': average_percent6,
                 'average7': average_percent7,'average8': average_percent8,
                 'average9': average_percent9, 'average10': average_percent10
}
average_percent_list = [ average_percent1,average_percent2,average_percent3,average_percent4,
      average_percent5, average_percent6, average_percent7,average_percent8,average_percent9,average_percent10
]


# print(average_percent.get('average10'))
# print(average_percent_list)
# --------------------------------------find average of last percent-------------------------------------
# ------------------------------------------------group list1--------------------------------------------
# -------------------------------------------------print test--------------------------------------------
# print(group_name1)
# print(group_list1)
# print(group_list1[0].get('value'))
# print(len(group_list1))
# print(group_sort_list1)
# print(group_sort_pe1)
# print(group_sort_percent1)
# print(group_pe_average1)
# print(group_pe_list1)
#
# for i in range(len(group_best_pe_list1)):
#       print(group_best_pe_list1[i])
#
# print(group_negetive_list1)
# print(group_posetive_list1)
# print(group_negetive_percent1)
# print(group_posetive_percent1)
# -------------------------------------------------print test--------------------------------------------
# -----------------------------------------group selected items dictionary-------------------------------
group_selected_items = {}
group_selected_items = dict(

    group_name = [group_name1,group_name2,group_name3,group_name4,group_name5],
    group_list = [group_list1,group_list2,group_list3,group_list4,group_list5],
    group_sort_list = [group_sort_list1,group_sort_list2,group_sort_list3,group_sort_list4,group_sort_list5],
    group_sort_pe = [group_sort_pe1,group_sort_pe2,group_sort_pe3,group_sort_pe4,group_sort_pe5],
    group_sort_percent = [group_sort_percent1,group_sort_percent2,group_sort_percent3,group_sort_percent4,group_sort_percent5],
    group_pe_average = [group_pe_average1,group_pe_average2,group_pe_average3,group_pe_average4,group_pe_average5],
    group_pe_list =  [group_pe_list1,group_pe_list2,group_pe_list3,group_pe_list4,group_pe_list5],
    group_best_pe_list = [group_best_pe_list1,group_best_pe_list2,group_best_pe_list3,group_best_pe_list4,group_best_pe_list5],
    group_negetive_list = [group_negetive_list1,group_negetive_list2,group_negetive_list3,group_negetive_list4,group_negetive_list5],
    group_posetive_list = [group_posetive_list1,group_posetive_list2,group_posetive_list3,group_posetive_list4,group_posetive_list5],
    group_negetive_percent = [group_negetive_percent1,group_negetive_percent2,group_negetive_percent3,
                              group_negetive_percent4, group_negetive_percent5],
    group_posetive_percent = [group_posetive_percent1,group_posetive_percent2,
                              group_posetive_percent3,group_posetive_percent4,group_posetive_percent5]

)

# -----------------------------------------group selected items dictionary-------------------------------
import os
from winsound import Beep
import time
import datetime

# time.sleep(1)
Beep(2000,100)
print('group_selected:executed.')

t = datetime.datetime.now()
print(t.minute,':', t.second,':',str(t.microsecond)[:2])
# ---------------------------------------------------------------------------------------------------------








