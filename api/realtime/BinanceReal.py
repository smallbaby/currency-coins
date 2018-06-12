import sys
from binance.client import Client
from binance.websockets import BinanceSocketManager
from conf.setting import *

'''

get sbinance realtime data

'''
def process_message(msg):
    print("message type: {}".format(msg['e']))
    print(msg)

    # need to add action..
    # format
    # save


class BinanceRealtime():

    def __init__(self):
        pass

    def main(self):
        client = Client('', '')
        bm = BinanceSocketManager(client)
        for symbol in binance_symbols:
            bm.start_kline_socket(symbol, process_message)

        bm.start()


if __name__ == '__main__':
    BinanceRealtime().main()



