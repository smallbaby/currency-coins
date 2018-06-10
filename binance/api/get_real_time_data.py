import sys
sys.path.append('../..')
from common.string_tools import *
from datetime import datetime
from binance.client import Client
from binance.websockets import BinanceSocketManager
from conf.setting import *

binance_symbol = ['ETHBTC', 'LTCBTC', 'BNBBTC', 'NEOBTC', 'QTUMETH', 'EOSETH', 'SNTETH', 'BNTETH', 'BCCBTC', 'GASBTC', 'BNBETH', 'HSRBTC', 'OAXETH', 'DNTETH', 'MCOETH', 'ICNETH', 'MCOBTC', 'WTCBTC', 'WTCETH', 'LRCBTC', 'LRCETH', 'QTUMBTC', 'YOYOBTC', 'OMGBTC', 'OMGETH', 'ZRXBTC', 'ZRXETH', 'STRATBTC', 'STRATETH', 'SNGLSBTC', 'SNGLSETH', 'BQXBTC', 'BQXETH', 'KNCBTC', 'KNCETH', 'FUNBTC', 'FUNETH', 'SNMBTC', 'SNMETH', 'NEOETH', 'IOTABTC', 'IOTAETH', 'LINKBTC', 'LINKETH', 'XVGBTC', 'XVGETH', 'SALTBTC', 'SALTETH', 'MDABTC', 'MDAETH', 'MTLBTC', 'MTLETH', 'SUBBTC', 'SUBETH', 'EOSBTC', 'SNTBTC', 'ETCETH', 'ETCBTC', 'MTHBTC', 'MTHETH', 'ENGBTC', 'ENGETH', 'DNTBTC', 'ZECBTC', 'ZECETH', 'BNTBTC', 'ASTBTC', 'ASTETH', 'DASHBTC', 'DASHETH', 'OAXBTC', 'ICNBTC', 'BTGBTC', 'BTGETH', 'EVXBTC', 'EVXETH', 'REQBTC', 'REQETH', 'VIBBTC', 'VIBETH', 'HSRETH', 'TRXBTC', 'TRXETH', 'POWRBTC', 'POWRETH', 'ARKBTC', 'ARKETH', 'YOYOETH', 'XRPBTC', 'XRPETH', 'MODBTC', 'MODETH', 'ENJBTC', 'ENJETH', 'STORJBTC', 'STORJETH', 'VENBTC', 'VENETH', 'KMDBTC', 'KMDETH', 'RCNBTC', 'RCNETH', 'NULSBTC', 'NULSETH', 'RDNBTC', 'RDNETH', 'XMRBTC', 'XMRETH', 'DLTBTC', 'DLTETH', 'AMBBTC', 'AMBETH', 'BCCETH', 'BATBTC', 'BATETH', 'BCPTBTC', 'BCPTETH', 'ARNBTC', 'ARNETH', 'GVTBTC', 'GVTETH', 'CDTBTC', 'CDTETH', 'GXSBTC', 'GXSETH', 'POEBTC', 'POEETH', 'QSPBTC', 'QSPETH', 'BTSBTC', 'BTSETH', 'XZCBTC', 'XZCETH', 'LSKBTC', 'LSKETH', 'TNTBTC', 'TNTETH', 'FUELBTC', 'FUELETH', 'MANABTC', 'MANAETH', 'BCDBTC', 'BCDETH', 'DGDBTC', 'DGDETH', 'ADXBTC', 'ADXETH', 'ADABTC', 'ADAETH', 'PPTBTC', 'PPTETH', 'CMTBTC', 'CMTETH', 'XLMBTC', 'XLMETH', 'CNDBTC', 'CNDETH', 'LENDBTC', 'LENDETH', 'WABIBTC', 'WABIETH', 'LTCETH', 'TNBBTC', 'TNBETH', 'WAVESBTC', 'WAVESETH', 'GTOBTC', 'GTOETH', 'ICXBTC', 'ICXETH', 'OSTBTC', 'OSTETH', 'ELFBTC', 'ELFETH', 'AIONBTC', 'AIONETH', 'NEBLBTC', 'NEBLETH', 'BRDBTC', 'BRDETH', 'EDOBTC', 'EDOETH', 'WINGSBTC', 'WINGSETH', 'NAVBTC', 'NAVETH', 'LUNBTC', 'LUNETH', 'TRIGBTC', 'TRIGETH', 'APPCBTC', 'APPCETH', 'VIBEBTC', 'VIBEETH', 'RLCBTC', 'RLCETH', 'INSBTC', 'INSETH', 'PIVXBTC', 'PIVXETH', 'IOSTBTC', 'IOSTETH', 'CHATBTC', 'CHATETH', 'STEEMBTC', 'STEEMETH', 'NANOBTC', 'NANOETH', 'VIABTC', 'VIAETH', 'BLZBTC', 'BLZETH', 'AEBTC', 'AEETH', 'RPXBTC', 'RPXETH', 'NCASHBTC', 'NCASHETH', 'POABTC', 'POAETH', 'ZILBTC', 'ZILETH', 'ONTBTC', 'ONTETH', 'STORMBTC', 'STORMETH', 'XEMBTC', 'XEMETH', 'WANBTC', 'WANETH', 'WPRBTC', 'WPRETH', 'QLCBTC', 'QLCETH', 'SYSBTC', 'SYSETH', 'GRSBTC', 'GRSETH', 'CLOAKBTC', 'CLOAKETH', 'GNTBTC', 'GNTETH', 'LOOMBTC', 'LOOMETH', 'BCNBTC', 'BCNETH', 'REPBTC', 'REPETH', 'TUSDBTC', 'TUSDETH', 'ZENBTC', 'ZENETH', 'SKYBTC', 'SKYETH', 'CVCBTC', 'CVCETH', 'THETABTC', 'THETAETH', 'IOTXBTC', 'IOTXETH', 'QKCBTC', 'QKCETH', 'AGIBTC', 'AGIETH', 'NXSBTC', 'NXSETH', 'DATABTC', 'DATAETH']


def process_message(msg):
    print("message type: {}".format(msg['e']))
    print(msg)

def main():
    client = Client('', '')
    bm = BinanceSocketManager(client)
    for symbol in binance_symbol:
        bm.start_kline_socket(symbol, process_message)

    bm.start()


if __name__ == '__main__':
    main()


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
