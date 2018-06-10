
import json
file = '/Users/kaizhang/Documents/exchangeInfo'


infos = open(file).readlines()
list = [symbol['symbol'] for symbol in eval(infos[0])['symbols'] if symbol['symbol'][-3:] in ['BTC', 'ETH']]

print(list)