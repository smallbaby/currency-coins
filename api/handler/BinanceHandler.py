# -*- coding: utf-8 -*-
import sys
import os
sys.path.append('../..')
import json
from pandas.core.frame import DataFrame
import pandas as pd
from conf.setting import *

import json

'''
    格式化历史数据
    # 周二，完成格式化、归档、写入文件

'''
class BinanceHandler():

    KEY = 'binance'
    def __init__(self):
        log.info('BinanceHandler is starting...')
        self.path = data_path + BinanceHandler.KEY + '/'
        #self.target_name = BinanceHandler.KEY + '_1y.csv'
        if not is_on:
            self.path += 'test/'

        self.binance_columns = binance_columns
        self.df = pd.DataFrame(columns = binance_columns)
    def output(self):
        log.info('格式化完成。准备写入文件')
        #self.df.to_csv(target_path + self.target_name)

    def input(self):
        self.file_list = []
        for parent, dirnames, filenames in os.walk(self.path):
            for filename in [fn for fn in filenames if fn.endswith('.json')]:
                file_path = os.path.join(parent, filename)
                self.file_list.append(parent + filename)

    def get_pairs(self, filename): # 'Binance_EOSBTC_1m_1493596800000 - 1528502400000.json'
        return filename.split('_')[1]

    def handler(self):
        for fn in self.file_list:
            log.info('{0} is processing....'.format(fn))
            fn, name = fn, self.get_pairs(fn)
            with open(fn) as f:
                line = eval(f.readlines()[0])
                DataFrame(line).to_csv(target_path + BinanceHandler.KEY + '_' + name + '.csv')



if __name__ == '__main__':
    bh = BinanceHandler()
    bh.input()
    bh.handler()
    bh.output()
    log.info('End.')