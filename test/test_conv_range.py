# -*- coding: utf-8 -*-
# author: kai.zhang
# 验证最大涨跌幅
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

        s0501 = 1525104000 # 2018-05-01 00:00:00
        s0428 = 1524844800 # 2018-04-28 00:00:00   # 近三天 、
        crc = ConversionRateCalculation('eosbtc')
        file = '../huobi/data/' + crc.data_name
        list = []
        with open(file) as f:
            reader = csv.reader(f)
            for r in reader:
                if r[1] == 'timestamp':
                    continue
                ts = int(float(r[1])/1000)
                if ts >= s0428 and ts <= s0501:
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
        print(rate)
        #self.assertEqual(abs(rate), 0.04697562823588834)