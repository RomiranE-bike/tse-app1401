# # -*- coding: utf-8 -*-
# """
# edited on 1400/11/27 ---- 02/16/2022
#
# @author: mahmoud esmaeili
# """
from flask import Flask, render_template
import time
import threading


import fipiran_data
import tgju_data
import best_co
import index_data
import market_data
import group_selected
import hot_money_data
import qeueu_data

bourse_status = fipiran_data.bourse_status
fara_bourse_status = fipiran_data.fara_bourse_status
tgju_list=tgju_data.tgju_list

market_list = market_data.market_list
market_average_pe = market_data.market_average_pe
market_best_pe_list = market_data.market_best_pe_list
market_negetive_percent = market_data.market_sign[2]
market_posetive_percent = market_data.market_sign[3]

hot_money_list = hot_money_data.hot_money_list
market_average_hotmoney = hot_money_data.market_average_hotmoney
group_hotmoney_items = hot_money_data.group_hotmoney_items

qeueu_items = qeueu_data.qeueu_items

group_selected_items = group_selected.group_selected_items
average_percent_list = group_selected.average_percent_list


index_now = index_data.index_now

best_co_dict = best_co.best_co_dict
top_ten_co = best_co.top_ten_co

last_update = time.ctime()


app = Flask(__name__)

@app.route('/')
def market_view():

    return render_template  ("market_view.html",
               bourse_status=bourse_status,
               fara_bourse_status=fara_bourse_status,
               tgju_list=tgju_list,

               market_list=market_list,
               market_average_pe=market_average_pe,
               market_best_pe_list=market_best_pe_list,
               market_negetive_percent=market_negetive_percent,
               market_posetive_percent=market_posetive_percent,

               group_selected_items=group_selected_items,
               average_percent_list=average_percent_list,

               index_now=index_now,

               best_co_dict=best_co_dict,
               top_ten_co=top_ten_co,
               last_update=last_update,

               hot_money_list = hot_money_list,
               market_average_hotmoney = market_average_hotmoney,
               group_hotmoney_items = group_hotmoney_items
              )

@app.route('/hot_money_table/')
def hot_money_table():

    return render_template ("hot_money_table.html",
                bourse_status = bourse_status,
                fara_bourse_status = fara_bourse_status,
                tgju_list = tgju_list,

                market_list = market_list,
                market_average_pe = market_average_pe,
                market_best_pe_list = market_best_pe_list,
                market_negetive_percent = market_negetive_percent,
                market_posetive_percent = market_posetive_percent,

                group_selected_items = group_selected_items,
                average_percent_list = average_percent_list,

                index_now = index_now,

                best_co_dict = best_co_dict,
                top_ten_co = top_ten_co,
                last_update = last_update,

                hot_money_list = hot_money_list,
                market_average_hotmoney = market_average_hotmoney,
                group_hotmoney_items = group_hotmoney_items
                )

@app.route('/hot_money_chart/')
def hot_money_chart():

    return render_template ("hot_money_chart.html",
                bourse_status = bourse_status,
                fara_bourse_status = fara_bourse_status,
                tgju_list = tgju_list,

                market_list = market_list,
                market_average_pe = market_average_pe,
                market_best_pe_list = market_best_pe_list,
                market_negetive_percent = market_negetive_percent,
                market_posetive_percent = market_posetive_percent,

                group_selected_items = group_selected_items,
                average_percent_list = average_percent_list,

                index_now = index_now,

                best_co_dict = best_co_dict,
                top_ten_co = top_ten_co,
                last_update = last_update,

                hot_money_list = hot_money_list,
                market_average_hotmoney = market_average_hotmoney,
                group_hotmoney_items = group_hotmoney_items
                )

@app.route('/neg_pos_chart/')
def neg_pos_chart():

    return render_template ("neg_pos_chart.html",
                bourse_status = bourse_status,
                fara_bourse_status = fara_bourse_status,
                tgju_list = tgju_list,

                market_list = market_list,
                market_average_pe = market_average_pe,
                market_best_pe_list = market_best_pe_list,
                market_negetive_percent = market_negetive_percent,
                market_posetive_percent = market_posetive_percent,

                group_selected_items = group_selected_items,
                average_percent_list = average_percent_list,

                index_now = index_now,

                best_co_dict = best_co_dict,
                top_ten_co = top_ten_co,
                last_update = last_update,

                hot_money_list = hot_money_list,
                market_average_hotmoney = market_average_hotmoney,
                group_hotmoney_items=group_hotmoney_items
                )

@app.route('/best_co_chart/')
def best_co_chart():

    return render_template ("best_co_chart.html",
                bourse_status = bourse_status,
                fara_bourse_status = fara_bourse_status,
                tgju_list = tgju_list,

                market_list = market_list,
                market_average_pe = market_average_pe,
                market_best_pe_list = market_best_pe_list,
                market_negetive_percent = market_negetive_percent,
                market_posetive_percent = market_posetive_percent,

                group_selected_items = group_selected_items,
                average_percent_list = average_percent_list,

                index_now = index_now,

                best_co_dict = best_co_dict,
                top_ten_co = top_ten_co,
                last_update = last_update,

                hot_money_list = hot_money_list,
                market_average_hotmoney = market_average_hotmoney,
                group_hotmoney_items=group_hotmoney_items
                )

@app.route('/pe_chart/')
def pe_chart():

    return render_template ("pe_chart.html",
                bourse_status = bourse_status,
                fara_bourse_status = fara_bourse_status,
                tgju_list = tgju_list,

                market_list = market_list,
                market_average_pe = market_average_pe,
                market_best_pe_list = market_best_pe_list,
                market_negetive_percent = market_negetive_percent,
                market_posetive_percent = market_posetive_percent,

                group_selected_items = group_selected_items,
                average_percent_list = average_percent_list,

                index_now = index_now,

                best_co_dict = best_co_dict,
                top_ten_co = top_ten_co,
                last_update = last_update,

                hot_money_list = hot_money_list,
                market_average_hotmoney = market_average_hotmoney,
                group_hotmoney_items=group_hotmoney_items
                )

@app.route('/pe_table/')
def pe_table():

    return render_template ("pe_table.html",
                bourse_status = bourse_status,
                fara_bourse_status = fara_bourse_status,
                tgju_list = tgju_list,

                market_list = market_list,
                market_average_pe = market_average_pe,
                market_best_pe_list = market_best_pe_list,
                market_negetive_percent = market_negetive_percent,
                market_posetive_percent = market_posetive_percent,

                group_selected_items = group_selected_items,
                average_percent_list = average_percent_list,

                index_now = index_now,

                best_co_dict = best_co_dict,
                top_ten_co = top_ten_co,
                last_update = last_update,

                hot_money_list = hot_money_list,
                market_average_hotmoney = market_average_hotmoney,
                group_hotmoney_items=group_hotmoney_items
                )

@app.route('/data_table/')
def data_table():

    return render_template ("data_table.html",
                bourse_status = bourse_status,
                fara_bourse_status = fara_bourse_status,
                tgju_list = tgju_list,

                market_list = market_list,
                market_average_pe = market_average_pe,
                market_best_pe_list = market_best_pe_list,
                market_negetive_percent = market_negetive_percent,
                market_posetive_percent = market_posetive_percent,

                group_selected_items = group_selected_items,
                average_percent_list = average_percent_list,

                index_now = index_now,

                best_co_dict = best_co_dict,
                top_ten_co = top_ten_co,
                last_update = last_update,

                hot_money_list = hot_money_list,
                market_average_hotmoney = market_average_hotmoney,
                group_hotmoney_items=group_hotmoney_items
                )

@app.route('/qeueu_table/')
def qeueu_table():

    return render_template ("qeueu_table.html",
                bourse_status = bourse_status,
                fara_bourse_status = fara_bourse_status,
                tgju_list = tgju_list,

                market_list = market_list,
                market_average_pe = market_average_pe,
                market_best_pe_list = market_best_pe_list,
                market_negetive_percent = market_negetive_percent,
                market_posetive_percent = market_posetive_percent,

                group_selected_items = group_selected_items,
                average_percent_list = average_percent_list,

                index_now = index_now,

                best_co_dict = best_co_dict,
                top_ten_co = top_ten_co,
                last_update = last_update,

                hot_money_list = hot_money_list,
                market_average_hotmoney = market_average_hotmoney,
                group_hotmoney_items=group_hotmoney_items,
                qeueu_items = qeueu_items
                )

@app.route('/filter/')
def filter():
    return render_template ("filter.html",
                bourse_status = bourse_status,
                fara_bourse_status = fara_bourse_status,
                tgju_list = tgju_list,

                market_list = market_list,
                market_average_pe = market_average_pe,
                market_best_pe_list = market_best_pe_list,
                market_negetive_percent = market_negetive_percent,
                market_posetive_percent = market_posetive_percent,

                group_selected_items = group_selected_items,
                average_percent_list = average_percent_list,

                index_now = index_now,

                best_co_dict = best_co_dict,
                top_ten_co = top_ten_co,
                last_update = last_update,

                hot_money_list = hot_money_list,
                market_average_hotmoney = market_average_hotmoney,
                group_hotmoney_items=group_hotmoney_items,
                qeueu_items = qeueu_items
                )

@app.route('/risk/')
def risk():
    return render_template ("risk.html",
                bourse_status = bourse_status,
                fara_bourse_status = fara_bourse_status,
                tgju_list = tgju_list,

                market_list = market_list,
                market_average_pe = market_average_pe,
                market_best_pe_list = market_best_pe_list,
                market_negetive_percent = market_negetive_percent,
                market_posetive_percent = market_posetive_percent,

                group_selected_items = group_selected_items,
                average_percent_list = average_percent_list,

                index_now = index_now,

                best_co_dict = best_co_dict,
                top_ten_co = top_ten_co,
                last_update = last_update,

                hot_money_list = hot_money_list,
                market_average_hotmoney = market_average_hotmoney,
                group_hotmoney_items=group_hotmoney_items,
                qeueu_items = qeueu_items
                )

@app.route('/about_us/')
def about_us():
    return render_template ("about_us.html",
                bourse_status = bourse_status,
                fara_bourse_status = fara_bourse_status,
                tgju_list = tgju_list,

                market_list = market_list,
                market_average_pe = market_average_pe,
                market_best_pe_list = market_best_pe_list,
                market_negetive_percent = market_negetive_percent,
                market_posetive_percent = market_posetive_percent,

                group_selected_items = group_selected_items,
                average_percent_list = average_percent_list,

                index_now = index_now,

                best_co_dict = best_co_dict,
                top_ten_co = top_ten_co,
                last_update = last_update,

                hot_money_list = hot_money_list,
                market_average_hotmoney = market_average_hotmoney,
                group_hotmoney_items=group_hotmoney_items,
                qeueu_items = qeueu_items
                )

if __name__ == '__main__':
       app.run(debug=True)

# --------------------------------------------------------------------
