from ib_insync import *
import sys
import time
import random

def get_price_data(ticker, months = 24):
    ib = IB()
    ib.connect('127.0.0.1', 4001, clientId=153)

    dt = ''
    barsList = []
    bars = None
    contract = Stock(ticker, 'BATS', 'USD')
    i = 1

    try:
        while True:
            bars = ib.reqHistoricalData(
                contract,
                endDateTime=dt,
                durationStr='1 M',
                barSizeSetting='1 min',
                whatToShow='TRADES',
                useRTH=True,
                formatDate=1)

            if not bars:
                break
            if i >= months:
                break
            else:
                i += 1

            barsList.append(bars)
            dt = bars[0].date
            print(dt)

    finally:
        # save to CSV file
        allBars = [b for bars in reversed(barsList) for b in bars]
        df = util.df(allBars)
        df.to_csv('data/stocks/' + ticker + '.csv', index_label = False)

        try:
            ib.disconnect()
        except:
            pass

def main():
    default_symbol = 'AMD'
    n_symbols = len(sys.argv) - 1
    symbol = None

    if(n_symbols == 0):
        symbol = default_symbol
    else:
        symbol = sys.argv[-1]

    get_price_data(symbol)

    print("Complete...")

if __name__ == '__main__':
    main()
