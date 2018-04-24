#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/19 23:08
# @Author  : Aries
# @Site    : 
# @File    : doOntime.py
# @Software: PyCharm

import datetime
import os

import schedule
import threading
import time

import sqlite3

DATABASE = os.path.join(os.path.dirname(__file__),'db','house.db');


def housReduceDay():
    conn = sqlite3.connect(DATABASE)
    print(u"I'm working for housReduceDay,每天上午11:30的时候就要统计好昨天的房价和今天相比较，今天涨幅情况如何！！！")
    sql="replace  into houseReduceDay(houseCode,date,reducePercent) select a.houseCode,b.date,(b.totalPrice-a.totalPrice)/a.totalPrice from houseEveryDayPrice as a,houseEveryDayPrice as b where a.houseCode=b.houseCode and  a.date=date('now','-1 day') and b.date=date('now') and a.totalPrice != b.totalPrice;"
    conn.execute(sql);
    conn.commit();
    print("housReduceDay:", datetime.datetime.now())

def houseReduceMonth():
    print("I'm working for job2")
    time.sleep(2)
    print("job2:", datetime.datetime.now())
def houseReduceWeek():
    print("I'm working for job2")
    time.sleep(2)
    print("job2:", datetime.datetime.now())
def houseReduceUntilNow():
    print("I'm working for job2")
    time.sleep(2)
    print("job2:", datetime.datetime.now())
def scrapyHouseInfo():
    print(u"I'm working for scrapyHouseInfo,每天上午10:00的时候就要开始抓取今天的房价数据！！！")
    os.system(os.path.join(os.path.dirname(__file__),"scripts","startScrapy.bat"))
    time.sleep(2)
    print("job2:", datetime.datetime.now())

def housReduceDay_task():
    threading.Thread(target=housReduceDay).start()
def houseReduceMonth_task():
    threading.Thread(target=houseReduceMonth).start()
def houseReduceWeek_task():
    threading.Thread(target=houseReduceWeek).start()
def houseReduceUntilNow_task():
    threading.Thread(target=houseReduceUntilNow).start()
def scrapyHouseInfo_task():
    threading.Thread(target=scrapyHouseInfo).start()
def run():
    schedule.every().day.at("11:30").do(housReduceDay_task)
    schedule.every().day.at("10:00").do(scrapyHouseInfo_task)





if __name__ == '__main__':
    print("start")
    print(DATABASE)
    run()
    while True:
        schedule.run_pending()
        time.sleep(1)