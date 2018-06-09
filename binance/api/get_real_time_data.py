import time
import dateparser
import pytz
import json
import sys
sys.path.append('../..')
from common.string_tools import *
from datetime import datetime
from binance.client import Client
from binance.websockets import BinanceSocketManager

def process_message(msg):
    print("message type: {}".format(msg['e']))
    print(msg)
    # do something

if __name__ == '__main__':
    client = Client('', '')
    bm = BinanceSocketManager(client)
    # start any sockets here, i.e a trade socket
    conn_key = bm.start_kline_socket('BNBBTC', process_message)
    bm.start()
