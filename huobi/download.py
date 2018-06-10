"""
author: thomaszdxsn
"""
import gzip
import json

import arrow
import aiohttp
from aiohttp.http_websocket import WSMsgType
import pandas as pd
import requests

def getIP(url):
    r = requests.get(url)
    print(r.text.split('\n')[0])
    return 'http://' + r.text.split('\n')[0]


async def fetch_data():
    api = 'wss://api.huobi.pro/ws'
    proxy = 'http://74.94.80.101:53281'
    #proxy = 'http://159.65.9.66:80'
    key = 'adabtc'
    #proxy = getIP('http://api.ip.data5u.com/api/get.shtml?order=ae66ab7ae9159e686bd236c7294454be&num=3&area=%E9%9D%9E%E4%B8%AD%E5%9B%BD&port=8080&carrier=0&protocol=1&an1=1&an2=2&an3=3&sp1=1&sp2=2&sort=2&system=1&distinct=0&rettype=1&seprator=%0A')
    df = pd.DataFrame(columns=['timestamp', 'open', 'high',
                               'low', 'close', 'volume', 'amount', 'count'])
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect(api, proxy=proxy) as ws:
            for start, end in arrow.Arrow.span_range(
                    'hour', arrow.get('2018-03-01'), arrow.get('2018-03-02')):
                payload = {
                    'req': "market."+key+".kline.1min",
                    'id': start.timestamp,
                    'from': start.timestamp,
                    'to': end.timestamp
                }
                await ws.send_json(payload)
                async for msg in ws:
                    if msg.type == WSMsgType.binary:
                        data = json.loads(gzip.decompress(msg.data))
                        if data.get('ping', None):
                            continue
                        if data.get('data', None) is None:
                            continue
                        for item in data['data']:
                            print(payload, item['id'])
                            df = df.append({
                                'timestamp': item['id'] * 1000,
                                'open': item['open'],
                                'close': item['close'],
                                'low': item['close'],
                                'high': item['high'],
                                'volume': item['vol'],
                                'amount': item['amount'],
                                'count': item['count']
                            }, ignore_index=True)
                        break
    df.to_csv('./data/' + key + '-m1-huobi.csv')



if __name__ == '__main__':
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(fetch_data())