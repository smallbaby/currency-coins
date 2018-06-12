# -*- coding: utf-8 -*-
# Const Data

from log.logger import *

home_path = '/home/ec2-user/'
data_path = '/home/ec2-user/data/'
target_path = '/home/ec2-user/data/target/'
is_on = True
log = get_logger(colorful=True, filename=home_path + 'tamc.log')

binance_columns = ['timestamp', 'open', 'high', 'low', 'close', 'valume', 'close_time', 'quote_volume', 'trades_num', 'buy_base_v','buy_quote_v']

'''
Binance Data
################binance history data style

[
                [
                    1499040000000,      # Open time
                    "0.01634790",       # Open
                    "0.80000000",       # High
                    "0.01575800",       # Low
                    "0.01577100",       # Close
                    "148976.11427815",  # Volume
                    1499644799999,      # Close time
                    "2434.19055334",    # Quote asset volume
                    308,                # Number of trades
                    "1756.87402397",    # Taker buy base asset volume
                    "28.46694368",      # Taker buy quote asset volume
                    "17928899.62484339" # Can be ignored
                ]
            ]


################binance realtime data format
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


### Coin50

coins = {
# 'Bitcoin': 'BTC',
# 'Ethereum': 'ETH',
'Ripple': 'XRP',
'Bitcoin Cash': 'BCH',
'EOS': 'EOS',
'Litecoin': 'LTC',
'Stellar': 'XLM',
'Cardano': 'ADA',
'IOTA': 'MIOTA',
'TRON': 'TRX',
'NEO': 'NEO',
'Monero': 'XMR',
'Dash': 'DASH',
'Tether': 'USDT',
'NEM': 'XEM',
'VeChain': 'VEM',
'Binance Coin': 'BNB',
'Ethereum Classic': 'ETC',
'Ontology': 'ONT',
'Qtum': 'QTUM',
'OmiseGO': 'OMG',
'Bytecoin': 'BCN',
'ICON': 'ICX',
'Zilliqa': 'ZIL',
'Zcash': 'ZEC',
'Lisk': 'LSK',
'Aeternity': 'AE',
'Bitcoin Gold': 'BTG',
'Decred': 'DCR',
'0x': 'ZRX',
'Bytom': 'BTM',
'Steem': 'STEEM',
'Siacoin': 'SC',
'Verge': 'XVG',
'BitShares': 'BTS',
'Nano': 'NANO',
'Maker': 'MKR',
'Wanchain': 'WAN',
'Golem': 'GNT',
'RChain': 'RHOC',
'Waves': 'WAVES',
'Stratis': 'STRAT',
'Augur': 'REP',
'Bitcoin Diamond': 'BDC',
'Dogecoin': 'DOGE',
'Populous': 'PPT',
'Bitcoin Private': 'BTCP',
'Waltonchain': 'WTC',
'DigiByte': 'DGB',
'IOST': 'IOST',
'Mixin': 'XIN',
'WaykiChain': 'WICC',
'Status': 'SNT'
}

binance_symbols = ['ETHBTC', 'LTCBTC', 'BNBBTC', 'NEOBTC', 'QTUMETH', 'EOSETH', 'SNTETH', 'BNTETH', 'BCCBTC', 'GASBTC', 'BNBETH', 'HSRBTC', 'OAXETH', 'DNTETH', 'MCOETH', 'ICNETH', 'MCOBTC', 'WTCBTC', 'WTCETH', 'LRCBTC', 'LRCETH', 'QTUMBTC', 'YOYOBTC', 'OMGBTC', 'OMGETH', 'ZRXBTC', 'ZRXETH', 'STRATBTC', 'STRATETH', 'SNGLSBTC', 'SNGLSETH', 'BQXBTC', 'BQXETH', 'KNCBTC', 'KNCETH', 'FUNBTC', 'FUNETH', 'SNMBTC', 'SNMETH', 'NEOETH', 'IOTABTC', 'IOTAETH', 'LINKBTC', 'LINKETH', 'XVGBTC', 'XVGETH', 'SALTBTC', 'SALTETH', 'MDABTC', 'MDAETH', 'MTLBTC', 'MTLETH', 'SUBBTC', 'SUBETH', 'EOSBTC', 'SNTBTC', 'ETCETH', 'ETCBTC', 'MTHBTC', 'MTHETH', 'ENGBTC', 'ENGETH', 'DNTBTC', 'ZECBTC', 'ZECETH', 'BNTBTC', 'ASTBTC', 'ASTETH', 'DASHBTC', 'DASHETH', 'OAXBTC', 'ICNBTC', 'BTGBTC', 'BTGETH', 'EVXBTC', 'EVXETH', 'REQBTC', 'REQETH', 'VIBBTC', 'VIBETH', 'HSRETH', 'TRXBTC', 'TRXETH', 'POWRBTC', 'POWRETH', 'ARKBTC', 'ARKETH', 'YOYOETH', 'XRPBTC', 'XRPETH', 'MODBTC', 'MODETH', 'ENJBTC', 'ENJETH', 'STORJBTC', 'STORJETH', 'VENBTC', 'VENETH', 'KMDBTC', 'KMDETH', 'RCNBTC', 'RCNETH', 'NULSBTC', 'NULSETH', 'RDNBTC', 'RDNETH', 'XMRBTC', 'XMRETH', 'DLTBTC', 'DLTETH', 'AMBBTC', 'AMBETH', 'BCCETH', 'BATBTC', 'BATETH', 'BCPTBTC', 'BCPTETH', 'ARNBTC', 'ARNETH', 'GVTBTC', 'GVTETH', 'CDTBTC', 'CDTETH', 'GXSBTC', 'GXSETH', 'POEBTC', 'POEETH', 'QSPBTC', 'QSPETH', 'BTSBTC', 'BTSETH', 'XZCBTC', 'XZCETH', 'LSKBTC', 'LSKETH', 'TNTBTC', 'TNTETH', 'FUELBTC', 'FUELETH', 'MANABTC', 'MANAETH', 'BCDBTC', 'BCDETH', 'DGDBTC', 'DGDETH', 'ADXBTC', 'ADXETH', 'ADABTC', 'ADAETH', 'PPTBTC', 'PPTETH', 'CMTBTC', 'CMTETH', 'XLMBTC', 'XLMETH', 'CNDBTC', 'CNDETH', 'LENDBTC', 'LENDETH', 'WABIBTC', 'WABIETH', 'LTCETH', 'TNBBTC', 'TNBETH', 'WAVESBTC', 'WAVESETH', 'GTOBTC', 'GTOETH', 'ICXBTC', 'ICXETH', 'OSTBTC', 'OSTETH', 'ELFBTC', 'ELFETH', 'AIONBTC', 'AIONETH', 'NEBLBTC', 'NEBLETH', 'BRDBTC', 'BRDETH', 'EDOBTC', 'EDOETH', 'WINGSBTC', 'WINGSETH', 'NAVBTC', 'NAVETH', 'LUNBTC', 'LUNETH', 'TRIGBTC', 'TRIGETH', 'APPCBTC', 'APPCETH', 'VIBEBTC', 'VIBEETH', 'RLCBTC', 'RLCETH', 'INSBTC', 'INSETH', 'PIVXBTC', 'PIVXETH', 'IOSTBTC', 'IOSTETH', 'CHATBTC', 'CHATETH', 'STEEMBTC', 'STEEMETH', 'NANOBTC', 'NANOETH', 'VIABTC', 'VIAETH', 'BLZBTC', 'BLZETH', 'AEBTC', 'AEETH', 'RPXBTC', 'RPXETH', 'NCASHBTC', 'NCASHETH', 'POABTC', 'POAETH', 'ZILBTC', 'ZILETH', 'ONTBTC', 'ONTETH', 'STORMBTC', 'STORMETH', 'XEMBTC', 'XEMETH', 'WANBTC', 'WANETH', 'WPRBTC', 'WPRETH', 'QLCBTC', 'QLCETH', 'SYSBTC', 'SYSETH', 'GRSBTC', 'GRSETH', 'CLOAKBTC', 'CLOAKETH', 'GNTBTC', 'GNTETH', 'LOOMBTC', 'LOOMETH', 'BCNBTC', 'BCNETH', 'REPBTC', 'REPETH', 'TUSDBTC', 'TUSDETH', 'ZENBTC', 'ZENETH', 'SKYBTC', 'SKYETH', 'CVCBTC', 'CVCETH', 'THETABTC', 'THETAETH', 'IOTXBTC', 'IOTXETH', 'QKCBTC', 'QKCETH', 'AGIBTC', 'AGIETH', 'NXSBTC', 'NXSETH', 'DATABTC', 'DATAETH']
MYSQL_IP = ''
MYSQL_PORT = ''
MYSQL_USER = ''
MYSQL_PASSWORD = ''
MYSQL_DB = 'utf8'