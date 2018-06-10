from websocket import create_connection
import ast
import json

_URI = "wss://api.bitfinex.com/ws"

class Public:

    def order_book(self, pair, precision='P0', freq='F0', length=25, return_socket=False):
        ws = create_connection(_URI)
        ws.send(json.dumps({
            "event": "subscribe",
            "channel": "book",
            "pair": pair.upper(),
            "prec": precision,
            "freq": freq,
            'len': length
        }))

        return ws

    def ticker(self, pair):
        ws = create_connection(_URI)
        ws.send(json.dumps({
            "event": "subscribe",
            "channel": "ticker",
            "pair": pair.upper(),
        }))

        return ws


def parse_ticker_response(response):
    keys = ['channel_id', 'bid', 'bid_size', 'ask', 'ask_size', 'daily_change', 'daily_change_perc', 'last_price', 'vol', 'high', 'low']
    response = ast.literal_eval(response)
    parsed_res = {k:r for k, r in zip(keys, response)}
    return parsed_res