from ib_async import *


def get_option_chain_exp_data():
    


# util.startLoop()
def main():
    try:
        ib = IB()
        ib.connect(port=7496, clientId=35)

        values =  ib.accountValues() 

        print( len(values))

        get_option_chain_exp_data()

        ib.disconnect()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise


main()