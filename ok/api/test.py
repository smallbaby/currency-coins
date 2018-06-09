# -*- coding: utf-8 -*-
# author: 半熟的韭菜

from websocket import create_connection
import gzip
import time

if __name__ == '__main__':
    while (1):
        try:
            ws = create_connection("wss://real.okcoin.com:10440/websocket/okcoinapi")
            break
        except:
            print('connect ws error,retry...')
            time.sleep(5)

    # 订阅 KLine 数据
    tradeStr ="{'event':'addChannel','channel':'ok_sub_spotusd_btc_ticker','binary':'true'}"


    ws.send("{'event':'addChannel','channel':'ok_sub_spotusd_btc_ticker','binary':'true'}")
    while (1):
        compressData = ws.recv()
        print(compressData)
        result = gzip.decompress(compressData).decode('utf-8')
        if result[:7] == '{"ping"':
            ts = result[8:21]
            pong = '{"pong":' + ts + '}'
            ws.send(pong)
            ws.send(tradeStr)
        else:
            print(result)



