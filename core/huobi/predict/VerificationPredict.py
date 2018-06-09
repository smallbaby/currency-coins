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
from core.common.string_tools import *

def get_timestamp(date):
    return (int)(time.mktime(time.strptime(date, "%Y-%m-%d %H:%M:%S")))



'''
公式：
建仓时点价格：5月1日0：00价格，编号M
建仓时间之后的价格：5月1日0：00-5月31日的价格。N
If N（1+X）<=M(1/(1-A) )平仓时点与平仓价格。

'''
class VerificationPredict(object):

    def __init__(self, coin):
        self.coin = coin
        self.data_path = '../data/'
        self.data_name = coin + '-m1-huobi.csv'

    def init(self):
        df = pd.read_csv(self.data_path + self.data_name).reset_index(drop=False)
        self.df = pd.DataFrame(df, columns=['timestamp', 'open', 'high', 'low']).sort_values(by="timestamp")
        return self

    def predict(self, X = 0):
        #排序、建仓
        b = 1525104060

        datas = self.df[(self.df['timestamp'] / 1000 >= get_timestamp('2018-05-01 00:00:00')) & (self.df['timestamp'] / 1000 <= get_timestamp('2018-05-31 00:00:00'))]
        datas.to_csv(self.coin + '--05010531.csv',sep=',')
        bench_open = 0
        bench_st = 0
        print(len(datas))

        for index, row in datas.iterrows():
            st = int(row['timestamp']/1000)
            if st < b:
                continue
            elif st == b:
                bench_open = row['open']
                bench_st = st
                print(bench_open, bench_open * (1.0 / (1 - 0.337)))
            else:
                curr_price = row['open']

                # If N（1 + X） <= M(1 / (1 - A))
                if curr_price*(1 + 0.0445) <= bench_open*(1.0/(1-0.337)):
                    #print(as_num(curr_price), as_num(bench_open))
                    print(get_time_by_st(st), as_num(curr_price)) # 时间  平仓价格
        # print(datas)

if __name__ == '__main__':
    for coin in coins_pair:
        vcp = VerificationPredict(coin)
        vcp.init()
        vcp.predict()