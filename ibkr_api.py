from ib_insync import *
import sys
import time
import random

def get_price_data(symbols):
    ib = IB()
    ib.connect('127.0.0.1', 2506, clientId=1576)

    for s in symbols:
        print('Collecting price data for: ' + s)
        contract = Stock(s, 'NYSE', 'USD')

        bars = ib.reqHistoricalData(
                contract,
                endDateTime = '',
                durationStr = '3 M',
                barSizeSetting = '15 mins',
                whatToShow = 'MIDPOINT',
                useRTH = True,
                formatDate = 1)

        df = util.df(bars)
        df.to_csv('data/stocks/' + s + '.csv', index_label = False)
        time.sleep(1)

    ib.disconnect()

if __name__ == '__main__':

    default_symbols = ['V']

    n_symbols = len(sys.argv) - 1
    symbols = None

    if(n_symbols == 0):
        symbols = default_symbols
    else:
        symbols = [s for s in sys.argv[-1:]]

    get_price_data(symbols)

    print("Complete...")
