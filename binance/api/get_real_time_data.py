import sys
sys.path.append('../..')
from common.string_tools import *
from datetime import datetime
from binance.client import Client
from binance.websockets import BinanceSocketManager
from conf.setting import *

def process_message(msg):
    print("message type: {}".format(msg['e']))
    print(msg)
    # do something

if __name__ == '__main__':
    client = Client('', '')
    bm = BinanceSocketManager(client)
    conn_key = bm.start_kline_socket('BNBBTC', process_message)
    bm.start()


'''
{
  "e": "kline",     // Event type
  "E": 123456789,   // Event time
  "s": "BNBBTC",    // Symbol
  "k": {
    "t": 123400000, // Kline start time
    "T": 123460000, // Kline close time
    "s": "BNBBTC",  // Symbol
    "i": "1m",      // Interval
    "f": 100,       // First trade ID
    "L": 200,       // Last trade ID
    "o": "0.0010",  // Open price
    "c": "0.0020",  // Close price
    "h": "0.0025",  // High price
    "l": "0.0015",  // Low price
    "v": "1000",    // Base asset volume
    "n": 100,       // Number of trades
    "x": false,     // Is this kline closed?
    "q": "1.0000",  // Quote asset volume
    "V": "500",     // Taker buy base asset volume
    "Q": "0.500",   // Taker buy quote asset volume
    "B": "123456"   // Ignore
  }
}
'''
