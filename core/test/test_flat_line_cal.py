# -*- coding: utf-8 -*-
# author: kai.zhang
# 验证平仓线
import unittest
import csv
from core.huobi.analysis.ConversionRateCalculation import *
import arrow

'''
验证步骤：
1、相同的时间切片方法
2、不同的读取方式
3、不同的判断方式
4、对比结果

'''
def get_timestamp(date):
    return (int)(time.mktime(time.strptime(date, "%Y-%m-%d %H:%M:%S")))
def get_range(start, dalt=1):
    for i in range(dalt+1):
        td = (start + datetime.timedelta(minutes=1)).strftime('%Y-%m-%d %H:%M:')
        start = datetime.datetime.strptime(td, '%Y-%m-%d %H:%M:')
    return start

def process(start, dalt):
    end = get_range(start, dalt)
    return start, end

def as_num(x):
    y = '{:.7f}'.format(float(x))  # 5f表示保留5位小数点的float型
    return (y)
class testFlatLineCal(unittest.TestCase):

    def test_flat_line(self):
        s0501 = '2018-05-01'  # 2018-05-01 00:00:00
        s0429 = '2018-04-29'  # 2018-04-29 00:00:00   # 近三天
        start = datetime.datetime.strptime(
            (datetime.datetime.strptime(s0429, '%Y-%m-%d') + datetime.timedelta(minutes=-1)).strftime(
                '%Y-%m-%d %H:%M:'),
            '%Y-%m-%d %H:%M:')
        endt = datetime.datetime.strptime(s0501, '%Y-%m-%d')
        crc = ConversionRateCalculation('eosbtc')
        file = '../huobi/data/' + crc.data_name
        f = open(file)
        reader = csv.reader(f)
        datas = []
        for r in reader:
            datas.append(r)
        for minute in conve_rate_minutes:  # 窗口
            coin_min_rates = []
            i = 0
            while start < endt:  # %H:%M:%S'):
                i = i + 1
                td = (start + datetime.timedelta(minutes=1)).strftime('%Y-%m-%d %H:%M:')
                start = datetime.datetime.strptime(td, '%Y-%m-%d %H:%M:')
                start, end = process(start, minute)


                s1 = get_timestamp(start.strftime("%Y-%m-%d %H:%M:%S"))
                s2 = get_timestamp(end.strftime("%Y-%m-%d %H:%M:%S"))
                list = []
                if 1 == 1:
                    for r in datas:
                        if r[1] == 'timestamp':
                            continue
                        ts = int(float(r[1])/1000)
                        if ts >= s1 and ts <= s2:
                            list.append(r)
                list.sort(key=lambda it:float(it[3]), reverse=True)
                high1 = float(list[0][3])
                hst = list[0][1]
                list.sort(key=lambda it:float(it[4]), reverse=False)
                low1 = float(list[0][4])
                lst = list[0][1]
                print(start, high1, low1, list)
        #
        # if hst > lst:  # 涨幅
        #     rate = (high1 - low1) / low1
        # elif hst < lst:  # 跌幅
        #     rate = (low1 - high1) / high1
        # print(rate)
        # #self.assertEqual(abs(rate), 0.04697562823588834)