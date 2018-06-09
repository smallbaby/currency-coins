# -*- coding: utf-8 -*-
#author: kai.zhang
import pandas as pd
import numpy as np
import arrow
import time
import datetime
from conf.setting import *
from core.common.string_tools import *

'''
sheet0
'''
class ConversionRateCalculation(object):

    def __init__(self, coin = 'xrpbtc'):
        self.benchmark = '2018-05-01'
        self.data_path = '../data/'
        self.data_name = coin + '-m1-huobi.csv'
        self.head = ' 00:00:00'
        self.tail = ' 23:59:59'
        self.columns = ['timestamp', 'open', 'high',
                   'low', 'close', 'volume', 'amount', 'count']

    def get_date_range(self, start, end):
        start += self.head
        end += self.head # 截止基准的00：00
        return self.get_timestamp(start), self.get_timestamp(end)

    def init(self):
        df = pd.read_csv(self.data_path + self.data_name).reset_index(drop=False)
        self.df = pd.DataFrame(df, columns=['timestamp', 'high', 'low'])
        return self


    def conver_rate(self, dalt = 1):
        '''
        计算距离N天的折算率
        :return:
        '''
        start = (datetime.datetime.strptime(self.benchmark, '%Y-%m-%d') - datetime.timedelta(days=dalt)).strftime('%Y-%m-%d')

        start, end = self.get_date_range(start, self.benchmark)

        datas = self.df[(self.df['timestamp'] / 1000 >= start) & (self.df['timestamp'] / 1000 <= end)]
        high, low = datas.loc[datas.high == datas.high.max()], datas.loc[datas.low == datas.low.min()]
        high = high.loc[high.index[0]]
        low = low.loc[low.index[0]]
        incr, decl = 0, 0
        if high.timestamp > low.timestamp:  # 涨幅
            rate = (high.high - low.low) / low.low
        elif high.timestamp < low.timestamp:  # 跌幅
            rate = (low.low - high.high) / high.high
        return round(rate, 4)


if __name__ == '__main__':
    all = {}
    for coin in coins_pair:
        res = {}
        for day in conve_rate_days:
            crc = ConversionRateCalculation(coin).init()
        #     res[day] = crc.conver_rate(day)
        # print(coin, res[1], res[3], res[7], res[15], res[30], res[45], res[60])

