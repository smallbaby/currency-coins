# -*- coding: utf-8 -*-
#author: kai.zhang
import time
import datetime

def get_not_null(tuple):
    for item in tuple:
        for it in item:
            if it != 0.0:
                return it

def as_num(x):
    y = '{:.7f}'.format(float(x))  # 5f表示保留5位小数点的float型
    return (y)


def get_time_by_st(st, fmt = '%Y-%m-%d %H:%M:%S'):
    return time.strftime(fmt, time.localtime(st))




def get_range(start, dalt=1):
    for i in range(dalt+1):
        td = (start + datetime.timedelta(minutes=1)).strftime('%Y-%m-%d %H:%M:')
        start = datetime.datetime.strptime(td, '%Y-%m-%d %H:%M:')
    return start


def process(start, dalt):
    end = get_range(start, dalt)
    return start, end


    def get_timestamp(date):
        return (int)(time.mktime(time.strptime(date, "%Y-%m-%d %H:%M:%S")))