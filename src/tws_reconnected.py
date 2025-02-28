import sys
from ib_async import *

def connect_to_ibkr(clientId=0):
    """
    Connect to a running TWS/gateway application.
    """
    print('Trying to connect...')
    max_attempts = 10
    current_reconnect = 0
    delaySecs = 60
    ib.disconnect()
    while True:
        try:
            ib.connect("127.0.0.1", port=7496, clientId=clientId, timeout=5)
            if ib.isConnected():
                print('Connected')
                break
        except Exception as err:
            print("Connection exception: ", err)
            if current_reconnect < max_attempts:
                current_reconnect += 1
                print('Connect failed')
                print(f'Retrying in {delaySecs} seconds, attempt {current_reconnect} of max {max_attempts}')
                ib.sleep(delaySecs)
            else:
                sys.exit(f"Reconnect Failure after {max_attempts} tries")
    ib.disconnectedEvent += onDisconnected
    
    # Function to call after successful connection
   #  do_something_important_upon_connection()

def onDisconnected():
    print("Disconnect Event")
    print("attempting restart and reconnect...")
    connect_to_ibkr()

def do_something_important_upon_connection():
    None

# https://github.com/erdewit/ib_insync/issues/41


ib = IB()
util.patchAsyncio()
connect_to_ibkr(33)
ib.disconnect()