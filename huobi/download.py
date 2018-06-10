# -*- coding: utf-8 -*-
import gzip
import json
import sys

import arrow
import aiohttp
from aiohttp.http_websocket import WSMsgType
import pandas as pd
import requests
from multiprocessing import Process, Pool

coins = {
# 'Bitcoin': 'BTC',
# 'Ethereum': 'ETH',
'Ripple': 'XRP',
'Bitcoin Cash': 'BCH',
'EOS': 'EOS',
'Litecoin': 'LTC',
'Stellar': 'XLM',
'Cardano': 'ADA',
'IOTA': 'MIOTA',
'TRON': 'TRX',
'NEO': 'NEO',
'Monero': 'XMR',
'Dash': 'DASH',
'Tether': 'USDT',
'NEM': 'XEM',
'VeChain': 'VEM',
'Binance Coin': 'BNB',
'Ethereum Classic': 'ETC',
'Ontology': 'ONT',
'Qtum': 'QTUM',
'OmiseGO': 'OMG',
'Bytecoin': 'BCN',
'ICON': 'ICX',
'Zilliqa': 'ZIL',
'Zcash': 'ZEC',
'Lisk': 'LSK',
'Aeternity': 'AE',
'Bitcoin Gold': 'BTG',
'Decred': 'DCR',
'0x': 'ZRX',
'Bytom': 'BTM',
'Steem': 'STEEM',
'Siacoin': 'SC',
'Verge': 'XVG',
'BitShares': 'BTS',
'Nano': 'NANO',
'Maker': 'MKR',
'Wanchain': 'WAN',
'Golem': 'GNT',
'RChain': 'RHOC',
'Waves': 'WAVES',
'Stratis': 'STRAT',
'Augur': 'REP',
'Bitcoin Diamond': 'BDC',
'Dogecoin': 'DOGE',
'Populous': 'PPT',
'Bitcoin Private': 'BTCP',
'Waltonchain': 'WTC',
'DigiByte': 'DGB',
'IOST': 'IOST',
'Mixin': 'XIN',
'WaykiChain': 'WICC',
'Status': 'SNT'
}

def getIP(url):
    r = requests.get(url)
    print(r.text.split('\n')[0])
    return 'http://' + r.text.split('\n')[0]


async def fetch_data(key, data, end_date = None):
    if end_date:
        end_date = arrow.get(end_date)
    else:
        end_date = arrow.utcnow()

    api = 'wss://api.huobi.pro/ws'
    proxy = 'http://74.94.80.101:53281'
    #proxy = 'http://159.65.9.66:80'
    #proxy = getIP('http://api.ip.data5u.com/api/get.shtml?order=ae66ab7ae9159e686bd236c7294454be&num=3&area=%E9%9D%9E%E4%B8%AD%E5%9B%BD&port=8080&carrier=0&protocol=1&an1=1&an2=2&an3=3&sp1=1&sp2=2&sort=2&system=1&distinct=0&rettype=1&seprator=%0A')
    df = pd.DataFrame(columns=['timestamp', 'open', 'high',
                               'low', 'close', 'volume', 'amount', 'count'])
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect(api, proxy=None) as ws:
            for start, end in arrow.Arrow.span_range(
                    'hour', arrow.get(data), end_date):

                payload = {
                    'req': "market."+key.lower()+"btc.kline.1min",
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

                        print(payload, start)
                        for item in data['data']:
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
        df.to_csv('./data/hb/'+key+'btc-m1-huobi.csv')


def loop(coin, data):
    loop = asyncio.get_event_loop()
    print(coin, ' is starting....')
    loop.run_until_complete(fetch_data(coin, data))


if __name__ == '__main__':
    import asyncio
    data = '2018-06-09'
    if len(sys.argv) > 1:
        data = sys.argv[1]

    pool = Pool(processes=8)
    res_l = []
    for name, coin in coins.items():
        res = pool.apply_async(loop, (coin, data))
    pool.close()
    pool.join()