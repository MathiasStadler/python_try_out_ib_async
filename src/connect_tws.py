from ib_async import *
util.startLoop()
ib = IB()
try:
    ib.connect(port=7496, clientId=35)
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
