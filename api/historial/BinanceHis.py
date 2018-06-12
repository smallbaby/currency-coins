# -*- coding: utf-8 -*-
import json
import sys
sys.path.append('../..')
from conf.setting import *
from common.date_utils import *
from binance.client import Client
from multiprocessing import Process, Pool
#from log.logger import *

#log = get_logger(colorful=True, filename='./tamc_analysis.log')

def get_historical_klines(symbol, interval, start_str, end_str=None):
    '''

    :param symbol:coin pairs
    :param interval:
    :param start_str:
    :param end_str:
    :return:
    '''
    output_data = []
    try:
        client = Client("", "")
        # setup the max limit
        limit = 500

        # convert interval to useful value in seconds
        timeframe = interval_to_milliseconds(interval)

        # convert our date strings to milliseconds
        start_ts = date_to_milliseconds(start_str)

        # if an end time was passed convert it
        end_ts = None
        if end_str:
            end_ts = date_to_milliseconds(end_str)

        idx = 0
        # it can be difficult to know when a symbol was listed on Binance so allow start time to be before list date
        symbol_existed = False
        while True:
            # fetch the klines from start_ts up to max 500 entries or the end_ts if set
            temp_data = client.get_klines(
                symbol=symbol,
                interval=interval,
                limit=limit,
                startTime=start_ts,
                endTime=end_ts
            )

            # handle the case where our start date is before the symbol pair listed on Binance
            if not symbol_existed and len(temp_data):
                symbol_existed = True

            if symbol_existed:
                # append this loops data to our output data
                output_data += temp_data

                # update our start timestamp using the last value in the array and add the interval timeframe
                start_ts = temp_data[len(temp_data) - 1][0] + timeframe
            else:
                # it wasn't listed yet, increment our start date
                start_ts += timeframe

            idx += 1
            # check if we received less than the required limit and exit the loop
            if len(temp_data) < limit:
                # exit the while loop
                break

            # sleep after every 3rd call to be kind to the API
            if idx % 3 == 0:
                time.sleep(1)
    except:
        return None

    return output_data

def historical(coin):
    '''
    get and save
    :param coin:
    :return:
    '''
    ks = {}
    # log.info('{0} is starting....'.format(coin + 'BTC'))
    print(coin + 'BTC', ' is starting....')
    try:
        ks[coin] = get_historical_klines(coin + 'BTC', interval, start, end)
        print(coin + 'BTC', len(ks[coin]))
        with open(
                "/home/ec2-user/data/binance/Binance_{}_{}_{}-{}.json".format(
                            coin + 'BTC',
                    interval,
                    date_to_milliseconds(start),
                    date_to_milliseconds(end)
                ),
                'w'  # set file write mode
        ) as f:
            f.write(json.dumps(ks[coin]))
    except Exception as err:
        print(coin, ' error',err)
        pass



if __name__ == '__main__':

    # log.info('binance history data task is starting....')
    if len(sys.argv) == 3:
        start = sys.argv[1]
        start = sys.argv[2]
    else:
        start = "1 May, 2017"
        end = "9 Jun, 2018"
    # log.info('start_time:' + start)
    # log.info('end_time:' + end)
    interval = Client.KLINE_INTERVAL_1MINUTE

    pool = Pool(processes=2)
    res_l = []
    for name, coin in coins.items():  # all coins needed..
        res = pool.apply_async(historical, (coin,))
    ks = {}
    pool.close()
    pool.join()
