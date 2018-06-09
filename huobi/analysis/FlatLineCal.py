# -*- coding: utf-8 -*-
#author: kai.zhang
import pandas as pd
import numpy as np
import arrow
import time
import datetime
from conf.setting import *
from core.common.string_tools import *
import logging

logging.basicConfig(filename='../logs/FlatLineCal.log',level=logging.DEBUG)

benchmark = '2018-03-01'
end_date = '2018-05-01'

class FlatLineCal(object):

    def __init__(self, coin = 'xrpbtc'):
        self.data_path = '../data/'
        self.data_name = coin + '-m1-huobi.csv'
        self.head = ':00'
        self.tail = ':59'

    def get_timestamp(self, date):
        return (int)(time.mktime(time.strptime(date, "%Y-%m-%d %H:%M:%S")))

    def get_date_range(self, start):
        start += self.head
        end = start + self.tail # 截止基准的00：00
        return self.get_timestamp(start), self.get_timestamp(end)

    def init(self):
        df = pd.read_csv(self.data_path + self.data_name).reset_index(drop=False)
        self.df = pd.DataFrame(df, columns=['timestamp', 'high', 'low'])
        return self


    def conver_rate(self, start ,end):
        '''
        计算窗口内的折价率
        :param start: 窗口开始
        :param end: 结束
        :return: 窗口指标
        '''
        start = self.get_timestamp(start)
        end = self.get_timestamp(end)
        datas = self.df[(self.df['timestamp'] / 1000 >= start) & (self.df['timestamp'] / 1000 < end)]
        high, low = datas.loc[datas.high == datas.high.max()], datas.loc[datas.low == datas.low.min()]
        if high.empty:
            return 0.0
        high = high.loc[high.index[0]]
        low = low.loc[low.index[0]]
        rate = 0.0
        if high.timestamp > low.timestamp:  # 涨幅
            rate = (high.high - low.low) / low.low
        elif high.timestamp < low.timestamp:  # 跌幅
            rate = (low.low - high.high) / high.high
        print(start,as_num(high.high), as_num(low.low))
        return round(rate, 4)


if __name__ == '__main__':
    ## test
    benchmark = '2018-04-29'
    end_date = '2018-05-01'
    all = {}
    t0 = time.time()
    for coin in ['xrpbtc']:#coins_pair: # 币
        res = {}
        start = datetime.datetime.strptime((datetime.datetime.strptime(benchmark, '%Y-%m-%d') + datetime.timedelta(minutes=-1)).strftime('%Y-%m-%d %H:%M:'),
                                           '%Y-%m-%d %H:%M:')
        for minute in conve_rate_minutes: # 窗口
            crc = FlatLineCal(coin).init()
            coin_min_rates = []
            i = 0
            logging.info({'coin': coin, 'minute': minute, 'status': 'Starting....'})
            while start < datetime.datetime.strptime(end_date, '%Y-%m-%d'):# %H:%M:%S'):
                i = i + 1
                td = (start + datetime.timedelta(minutes=1)).strftime('%Y-%m-%d %H:%M:')
                start = datetime.datetime.strptime(td, '%Y-%m-%d %H:%M:')
                start, end = process(start, minute)
                rate = crc.conver_rate(start.strftime("%Y-%m-%d %H:%M:%S"), end.strftime("%Y-%m-%d %H:%M:%S"))
                coin_min_rates.append({
                    'start': start,
                    'end': end,
                    'rate': rate
                })
                logging.info({'i':i, 's':start, 'r':rate})
            cs = sorted(coin_min_rates, key=lambda e: e['rate'], reverse=True)
            big = 0

            small = 0
            try:
                big = cs[0]
                small = cs[-1]
            except:
                pass

            print(coin, minute, big, small)
            logging.debug({'c': coin, 'm': minute, 'b': big, 's': small})
            logging.info({'coin': coin, 'minute': minute, 'status': 'End....'})
    print('all times taken:', time.time() - t0)
            # 最大涨幅、最大跌幅


