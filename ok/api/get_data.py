import websocket
import time
import sys
import json
import hashlib
import zlib
import base64

#business
def buildMySign(params,secretKey):
    sign = ''
    for key in sorted(params.keys()):
        sign += key + '=' + str(params[key]) +'&'
    return  hashlib.md5((sign+'secret_key='+secretKey).encode("utf-8")).hexdigest().upper()
#spot trade
def spotTrade(channel,api_key,secretkey,symbol,tradeType,price='',amount=''):
    params={
      'api_key':api_key,
      'symbol':symbol,
      'type':tradeType
     }
    if price:
        params['price'] = price
    if amount:
        params['amount'] = amount
    sign = buildMySign(params,secretkey)
    finalStr =  "{'event':'addChannel','channel':'"+channel+"','parameters':{'api_key':'"+api_key+"',\
                'sign':'"+sign+"','symbol':'"+symbol+"','type':'"+tradeType+"'"
    if price:
        finalStr += ",'price':'"+price+"'"
    if amount:
        finalStr += ",'amount':'"+amount+"'"
    finalStr+="},'binary':'true'}"
    return finalStr

#spot cancel order
def spotCancelOrder(channel,api_key,secretkey,symbol,orderId):
    params = {
      'api_key':api_key,
      'symbol':symbol,
      'order_id':orderId
    }
    sign = buildMySign(params,secretkey)
    return "{'event':'addChannel','channel':'"+channel+"','parameters':{'api_key':'"+api_key+"','sign':'"+sign+"','symbol':'"+symbol+"','order_id':'"+orderId+"'},'binary':'true'}"

#subscribe trades for self
def realtrades(channel,api_key,secretkey):
   params={'api_key':api_key}
   sign=buildMySign(params,secretkey)
   return "{'event':'addChannel','channel':'"+channel+"','parameters':{'api_key':'"+api_key+"','sign':'"+sign+"'},'binary':'true'}"

# trade for future
def futureTrade(api_key,secretkey,symbol,contractType,price='',amount='',tradeType='',matchPrice='',leverRate=''):
    params = {
      'api_key':api_key,
      'symbol':symbol,
      'contract_type':contractType,
      'amount':amount,
      'type':tradeType,
      'match_price':matchPrice,
      'lever_rate':leverRate
    }
    if price:
        params['price'] = price
    sign = buildMySign(params,secretkey)
    finalStr = "{'event':'addChannel','channel':'ok_futuresusd_trade','parameters':{'api_key':'"+api_key+"',\
               'sign':'"+sign+"','symbol':'"+symbol+"','contract_type':'"+contractType+"'"
    if price:
        finalStr += ",'price':'"+price+"'"
    finalStr += ",'amount':'"+amount+"','type':'"+tradeType+"','match_price':'"+matchPrice+"','lever_rate':'"+leverRate+"'},'binary':'true'}"
    return finalStr

#future trade cancel
def futureCancelOrder(api_key,secretkey,symbol,orderId,contractType):
    params = {
      'api_key':api_key,
      'symbol':symbol,
      'order_id':orderId,
      'contract_type':contractType
    }
    sign = buildMySign(params,secretkey)
    return "{'event':'addChannel','channel':'ok_futuresusd_cancel_order','parameters':{'api_key':'"+api_key+"',\
            'sign':'"+sign+"','symbol':'"+symbol+"','contract_type':'"+contractType+"','order_id':'"+orderId+"'},'binary':'true'}"

#subscribe future trades for self
def futureRealTrades(api_key,secretkey):
    params = {'api_key':api_key}
    sign = buildMySign(params,secretkey)
    return "{'event':'addChannel','channel':'ok_sub_futureusd_trades','parameters':{'api_key':'"+api_key+"','sign':'"+sign+"'},'binary':'true'}"

def on_open(self):

    self.send("{'event':'addChannel','channel':'ok_sub_spot_btc_usd_kline_1min'}");

def on_message(self,evt):
    print(evt)
    #data = inflate(evt) #data decompress
def inflate(data):
    print(data)
    decompress = zlib.decompressobj(
            -zlib.MAX_WBITS  # see above
    )
    inflated = decompress.decompress(data)
    inflated += decompress.flush()
    return inflated

def on_error(self,evt):
    print (self,evt)

def on_close(self,evt):
    print ('DISCONNECT')

if __name__ == "__main__":
    url = "wss://real.okcoin.com:10440/websocket/okcoinapi"
    api_key=''
    secret_key = ''

    websocket.enableTrace(False)
    if len(sys.argv) < 2:
        host = url
    else:
        host = sys.argv[1]
    ws = websocket.WebSocketApp(host,
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
