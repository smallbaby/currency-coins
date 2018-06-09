def process_message(msg):
    print("message type: {}".format(msg['e']))
    print(msg)
    # do something



from binance.websockets import BinanceSocketManager
from binance.client import Client

# create the Binance client, no need for api key
client = Client("", "")
bm = BinanceSocketManager(client)
# start any sockets here, i.e a trade socket
conn_key = bm.start_trade_socket('BNBBTC', process_message)
# then start the socket manager
bm.start()
