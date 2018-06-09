#!/usr/bin/python
# -*- coding: utf-8 -*-
# 1514736000 2018-01-01 00:00:00
# 1527897600

'''
	获取分钟级获取数据的参数对
'''
m3    = 1519833600 # 2018-03-01
m3_end = 1522511940
m4    = 1522512000 # 2018-04-01
m4_end = 1525103940
m5    = 1525104000 # 2018-05-01  1个月
m5_end = 1527696000 # 2018-05-31
min_dict = {

    '3' : {
        'f' : m3,
        't' : m3_end
    },
    '4' : {
        'f': m4,
        't': m4_end
    },
    '4.5': {
        'f': 1523743020,
        't': m5_end
    },
    '5': {
        'f': m5,
        't': m5_end
    },
    'all': {
        'f': m3,
        't': m5_end
    }
}

def get_trade_date_min(key, range, step = 18000):
    sum = 0
    topics   = []
    start = min_dict[range]['f']
    end_line = min_dict[range]['t']
    while  start <= end_line:
        sum += 1
        end = start + step
        topic = '{"req": "market.' + key + '.kline.1min","id": "id10", "from": '+str(start)+', "to":'+str(end)+'}'
        start += step
        topics.append(topic)
    return topics
