# Retrieve commission and margin impact without actually placing the order
#

# https://github.com/erdewit/ib_insync/blob/master/notebooks/basics.ipynb


# Cushion

from ib_async import *


def get_all_acount_data():
   try:
         values =  ib.accountValues() 

         for value in values:
             if value.tag == 'Cushion':
                print(f' tag => {value.tag}')
                print(f' value => {value.value} ')
   except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise




# util.startLoop()
ib = IB()
try:
    ib.connect(port=7496, clientId=35)
    get_all_acount_data()
    ib.disconnect()
    
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise


