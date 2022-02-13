# # -*- coding: utf-8 -*-
# """
# Created on 1400/10/06 ---- 12/27/2021
#
# @author: mahmoud esmaeili
# """
from bs4 import BeautifulSoup
import requests
import functions

list=[]

url2 = "https://www.fipiran.ir/Home/_MarketDailyTop"

def get_text(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    for element in soup.find_all("h6"):
        try:
            list.append(element.text)
        except:
            list.append(1)
            print('error fipiran not work')
        pass
    return  list

fipiran_data=get_text(url2)
# print(fipiran_data)
    
str_0 =fipiran_data[0]
list_0 = str_0.split()
#print(list_0)

str_2 =fipiran_data[2]
list_2 = str_2.split()
#print(list_2)

str_4 =fipiran_data[4]
list_4 = str_4.split()
#print(list_4)

str_5 =fipiran_data[5]
list_5 = str_5.split()
#print(list_5)

saraneh_bourse = []
saraneh_fara = []
if functions.chang_num(list_0[8]) != 0 :
        saraneh_bourse= round((functions.chang_num(list_0[15])
                               / functions.chang_num(list_0[8])) / 10000000,2)
if functions.chang_num(list_5[8]) != 0 :
        saraneh_fara = round((functions.chang_num(list_5[16])
                              / functions.chang_num(list_5[8])) / 10000000, 2)

bourse_status={}
bourse_status=dict(
                
                index_all=list_2[0],
                change=list_2[1],
                percent=list_2[2],
                market_val=list_0[19],
                date=list_2[3],
                time=list_2[4],
                status=list_0[4],
                trade_num=list_0[8],
                trade_vol=list_0[12],
                trade_val=list_0[15],
                saraneh_bourse=saraneh_bourse,
                stock_pos=list_0[24],
                stock_neg=list_0[29]
                )


fara_bourse_status={}
fara_bourse_status=dict(
                index_fara=list_4[0],
                change_fara=list_4[1],
                percent_fara=list_4[2],
                market_val_fara=list_5[20],
                date_fara=list_4[3],
                time_fara=list_4[4],
                status_fara=list_5[4],
                trade_num_fara=list_5[8],
                trade_vol_fara=list_5[12],
                trade_val_fara=list_5[16],
                saraneh_fara=saraneh_fara,
                stock_pos_fara=list_5[25],
                stock_neg_fara=list_5[30]
                )

# print(bourse_status)
# print(fara_bourse_status)
# --------------------------------------------------------------------------------



