from ib_async import *


def get_all_position():
    positions = ib.positions()

    for position in positions:
        print(f' {position.position} => {position.contract.symbol} - {position.contract.strike}  ')
        
      #  print(f'=> {position.contract.symbol} ')
      #        print(f'- ConId=> {position.contract.conId} ')
      #        - Bid => {position.contract}  - {position.avgCost}')

# util.startLoop()
ib = IB()
try:
    ib.connect(port=7496, clientId=35)
    get_all_position()
    ib.disconnect()
    
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise


