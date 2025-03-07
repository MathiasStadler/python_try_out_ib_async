from ib_async import *


def get_all_position():
    # positions = ib.positions()
    positions = ib.reqPositions()


    positions_data = []
    for position in positions:
       # print(f'{position.account} {position.contract.tradingClass}  {position.position} => {position.contract.symbol} - {position.contract.strike} {position.avgCost} ')
       
        print(f'{position.contract.symbol} Pos => {position.position}  - Strike => {position.contract.strike} - Cost => {position.avgCost} ')
        
        # ib.qualifyContracts(position)

        singleOptionPrice = position.avgCost /100

        column = []
        column.append( position.contract.symbol)
        column.append(position.contract.strike)
        column.append(position.contract.strike)
        column.append(position.avgCost)
        column.append(singleOptionPrice)

        print(f'{column}')


        # singleOptionPrice = position.avgCost /100

        print(f'singleOptionPrice => {singleOptionPrice}')
       # print(f'{position.contract.comboLegs}')
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


