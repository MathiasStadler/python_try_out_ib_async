import time
from ib_async import *


ib = IB()
try:
    ib.connect(port=7496, clientId=38)
    time.sleep(3)
    ib.disconnect()
    
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise