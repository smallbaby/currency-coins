# -*- coding: utf-8 -*-
# author: 半熟的韭菜

from websocket import create_connection
import gzip
import time

def send(ws):
    # 订阅 KLine 数据
    t1 = """{"sub": "market.ethbtc.kline.1min","id": "id10"}"""
    t2 = """{"sub": "market.eosbtc.kline.1min","id": "id11"}"""
    t3 = """{"sub": "market.bchbtc.kline.1min","id": "id12"}"""
    ws.send(t1)
    ws.send(t2)
    ws.send(t3)
    return ws

def main():
    while (1):
        try:
            ws = create_connection("wss://api.huobipro.com/ws")
            break
        except:
            print('connect ws error,retry...')
            time.sleep(5)
    send(ws)
    while (1):
        compressData = ws.recv()
        result = gzip.decompress(compressData).decode('utf-8')
        if result[:7] == '{"ping"':
            ts = result[8:21]
            pong = '{"pong":' + ts + '}'
            ws.send(pong)
            send(ws)
        else:
            print(result)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)



