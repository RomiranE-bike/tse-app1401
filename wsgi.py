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

from app.tse_app import app

if __name__ == "__main__":
  app.run()