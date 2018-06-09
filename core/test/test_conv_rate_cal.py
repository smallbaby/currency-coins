# -*- coding: utf-8 -*-
# author: kai.zhang
# 验证折算率
import unittest
import csv
from core.huobi.analysis.ConversionRateCalculation import *

def high(elem):
    return elem[3]
def low(elem):
    return elem[4]


# index,timestamp,open,high,low,close,volume,amount,count

def as_num(x):
    y = '{:.7f}'.format(float(x))  # 5f表示保留5位小数点的float型
    return (y)
class testConvRate(unittest.TestCase):

    def test_conv_rate(self):

        s0531 = 1527696000 # 2018/5/31 0:0:0
        s0530 = 1527609600 # 018/5/30 0:0:0
        crc = ConversionRateCalculation('adabtc')
        file = '../huobi/data/' + crc.data_name
        list = []
        with open(file) as f:
            reader = csv.reader(f)
            for r in reader:
                if r[1] == 'timestamp':
                    continue
                ts = int(float(r[1])/1000)
                if ts >= s0530 and ts <= s0531:
                    list.append(r)
        list.sort(key=lambda it:float(it[3]), reverse=True)
        high1 = float(list[0][3])
        hst = list[0][1]
        list.sort(key=lambda it:float(it[4]), reverse=False)
        low1 = float(list[0][4])
        lst = list[0][1]

        if hst > lst:  # 涨幅
            rate = (high1 - low1) / low1
        elif hst < lst:  # 跌幅
            rate = (low1 - high1) / high1
        self.assertEqual(abs(rate), 0.04697562823588834)