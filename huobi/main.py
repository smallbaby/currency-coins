# -*- coding: utf-8 -*-
#author: 半熟的韭菜

from websocket import create_connection
from core.common.get_date_range import *
import gzip
import json
import time
import logging
import pandas as pd

logging.basicConfig(filename='coin.log',level=logging.DEBUG)

def get_ws():
    while (1):
        try:
            ws = create_connection("wss://api.huobipro.com/ws")
            break
        except:
            print('connect ws error,retry...')
            time.sleep(5)
    return ws

def main(ws, key, range):
    df = pd.DataFrame(columns=['timestamp', 'open', 'high',
                               'low', 'close'])
    topics = get_trade_date_min(key, range)
    if range != 'all':
        csv_name = key + range
    print('all topics:', len(topics))
    for i, param in enumerate(topics):
        tradeStr = param
        ws.send(tradeStr)
        while (1):
            compressData = ws.recv()
            result = json.loads(gzip.decompress(compressData).decode('utf-8'))
            print(tradeStr, ' start', result)
            if result.get('ping', None):
                continue
            if result.get('data', None) is None:
                continue
            for item in result['data']:
                print(item)
                df = df.append({
                    'timestamp': item['id'] * 1000,
                    'open': item['open'],
                    'close': item['close'],
                    'low': item['close'],
                    'high': item['high'],
                    'volume': item['vol']
                }, ignore_index=True)
            break
    df.to_csv('./data/' + csv_name + '-huobi.csv', chunksize=10000)


if __name__ == '__main__':
    s1 = ['btc', 'eth']
    s2 = ['Ripple', 'Bitcoin Cash', 'eos', 'Litecoin', 'Cardano']
    symbols = ['btcusdt','ethbtc',] + [x + y for x in s2 for y in s1]
    main(get_ws(),'adabtc', '4.5')

