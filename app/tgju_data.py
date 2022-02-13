# -*- coding: utf-8 -*-
"""
Created on 1400/10/06 ---- 12/27/2021

@author: mahmoud esmaeili
"""
from bs4 import BeautifulSoup
import requests
import functions



url1 = "https://www.tgju.org/profile/ons"
url2 = "https://www.tgju.org/profile/price_dollar_rl"
url3 = "https://www.tgju.org/profile/nima_sell_usd"
url4 = "https://www.tgju.org/profile/energy-crude-oil"
url5 = "https://www.tgju.org/profile/energy-brent-oil"
url6 = "https://www.tgju.org/profile/crypto-bitcoin"
url7 = "https://www.tgju.org/profile/crypto-ethereum"



def get_data (url):
    data = []
    page = requests.get(url)
    temp = BeautifulSoup(page.text, 'html.parser')
    for item in temp.find_all("td"):
        data.append(item.text)
    return data
# -----------------------------------------------------------------
ons= get_data(url1)
ons[21]= functions.convert(ons[1])- functions.convert(ons[15])
ons_now = {}
ons_now = dict(
    date=ons[13],
    price_now=ons[1],
    price_yes=ons[15],
    change=ons[21],
    persent=ons[17]

)
# print(ons_now)
ons_price = [
    ons[13],
    ons[1],
    ons[15],
    ons[21],
    ons[17],
]
# -----------------------------------------------------------------------

dollar = get_data(url2)
dollar[21]= functions.convert(dollar[1])- functions.convert(dollar[15])
dollar_now = {}
dollar_now = dict(
    date=dollar[13],
    price_now=dollar[1],
    price_yes=dollar[15],
    change=dollar[21],
    persent=dollar[17]

)
# print(dollar_now)
dollar_price = [
    dollar[13],
    dollar[1],
    dollar[15],
    dollar[21],
    dollar[17]
]
# -----------------------------------------------------------------------

dollar_nima = get_data(url3)
dollar_nima[21]= functions.convert(dollar_nima[1])- functions.convert(dollar_nima[15])
dollar_nima_now = {}
dollar_nima_now = dict(
    date=dollar_nima[13],
    price_now=dollar_nima[1],
    price_yes=dollar_nima[15],
    change=dollar_nima[21],
    persent=dollar_nima[17]

)
# print(dollar_nima_now)

dollar_nima_price = [
    dollar_nima[13],
    dollar_nima[1],
    dollar_nima[15],
    dollar_nima[21],
    dollar_nima[17],

]
# -----------------------------------------------------------------------

wti = get_data(url4)
wti[21]= functions.convert(wti[1])- functions.convert(wti[15])
wti_now = {}
wti_now = dict(
    date=wti[13],
    price_now=wti[1],
    price_yes=wti[15],
    change=wti[21],
    persent=wti[17]

)
# print(wti_now)
wti_price = [
    wti[13],
    wti[1],
    wti[15],
    wti[21],
    wti[17],
]

# ----------------------------------------------------------------------

brent = get_data(url5)
brent[21]= functions.convert(brent[1])- functions.convert(brent[15])
brent_now = {}
brent_now = dict(
    date=brent[13],
    price_now=brent[1],
    price_yes=brent[15],
    change=brent[21],
    persent=brent[19]
)
# print(brent_now)

brent_price = [
    brent[13],
    brent[1],
    brent[15],
    brent[21],
    brent[19],
]
# ----------------------------------------------------------------------

bitcoin = get_data(url6)
bitcoin[21]= functions.convert(bitcoin[1])- functions.convert(bitcoin[17])

bitcoin_now = {}
bitcoin_now = dict(
    date=bitcoin[15],
    price_now=bitcoin[1],
    price_yes=bitcoin[17],
    persent=bitcoin[19],
    change=bitcoin[21]
)

bitcoin_price = [
    bitcoin[15],
    bitcoin[1],
    bitcoin[17],
    bitcoin[21],
    bitcoin[19]
]
# ----------------------------------------------------------------------

ethereum = get_data(url7)
ethereum[21]= functions.convert(ethereum[1])- functions.convert(ethereum[17])
ethereum_now = {}
ethereum_now = dict(
    date=ethereum[15],
    price_now=ethereum[1],
    price_yes=ethereum[17],
    change=ethereum[21],
    persent=ethereum[11]

)

ethereum_price = [
    ethereum[15],
    ethereum[1],
    ethereum[17],
    ethereum[21],
    ethereum[11]

]
# --------------------------------------------------------------------

tgju_list=[
    dollar_price,
    dollar_nima_price,
    bitcoin_price,
    ethereum_price,
    ons_price ,
    wti_price ,
    brent_price
]

# print(tgju_list)

# ---------------------------------------------------------------------
import os
from winsound import Beep
import time
import datetime

time.sleep(1)
Beep(2000,100)
print('tgju_data:executed.')

t = datetime.datetime.now()
print(t.minute,':', t.second,':',str(t.microsecond)[:2])