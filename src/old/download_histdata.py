# found here
# https://pydigger.com/pypi/ib_async

from ib_async import *
# util.startLoop()  # uncomment this line when in a notebook

ib = IB()
# ib.connect('127.0.0.1', 7497, clientId=1)
# use paper account port 7496
ib.connect('127.0.0.1', 7496, clientId=1)

ib.reqMarketDataType(4)  # Use free, delayed, frozen data
contract = Forex('EURUSD')
bars = ib.reqHistoricalData(
    contract, endDateTime='', durationStr='30 D',
    barSizeSetting='1 hour', whatToShow='MIDPOINT', useRTH=True)

# convert to pandas dataframe (pandas needs to be installed):
df = util.df(bars)
print(df)