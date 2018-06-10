import logging
import time
import sys

from btfxwss import BtfxWss

log = logging.getLogger(__name__)

fh = logging.FileHandler('test.log')
fh.setLevel(logging.DEBUG)
sh = logging.StreamHandler(sys.stdout)
sh.setLevel(logging.DEBUG)

log.addHandler(sh)
log.addHandler(fh)
logging.basicConfig(level=logging.DEBUG, handlers=[fh, sh])

wss = BtfxWss()
wss.start()

while not wss.conn.connected.is_set():
    time.sleep(1)

wss.subscribe_to_ticker('BTCUSD')
wss.subscribe_to_ticker('ETHUSD')
wss.subscribe_to_ticker('EOSUSD')
wss.subscribe_to_ticker('ETHBTC')
wss.subscribe_to_ticker('EOSBTC')
wss.subscribe_to_ticker('EOSETH')



while (1):
    q1 = wss.tickers('BTCUSD')
    q2 = wss.tickers('ETHBTC')
    q3 = wss.tickers('BTCUSD')
    q4 = wss.tickers('ETHBTC')
    q5 = wss.tickers('BTCUSD')
    q6 = wss.tickers('ETHBTC')
    print({'BTCUSD': q1.get()})
    print({'ETHUSD': q2.get()})
    print({'EOSUSD': q3.get()})
    print({'ETHBTC': q4.get()})
    print({'EOSBTC': q5.get()})
    print({'EOSETH': q6.get()})

