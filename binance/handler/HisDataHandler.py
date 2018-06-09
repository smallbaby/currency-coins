# -*- coding: utf-8 -*-
#author: kai.zhang
import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame

'''
币安历史数据处理

'''
class HisDataHandler(object):
    def __init__(self):
        self.data = open('../data/his_data.csv').readlines()

    def handler(self):
        klink_data = eval(self.data[0])
        kd = DataFrame(klink_data)
        print(kd[2])



if __name__ == '__main__':
    HisDataHandler().handler()