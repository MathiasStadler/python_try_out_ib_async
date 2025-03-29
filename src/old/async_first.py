# FROM HERE
# https://github.com/erdewit/ib_insync/issues/303

from ib_async import *
import logging
import time

# logger


def init_logger():

    # Setup logger
    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)

    # nice log output
    # FROM HERE
    # https://stackoverflow.com/questions/20618570/python-logging-formatter-is-there-any-way-to-fix-the-width-of-a-field-and-jus
    formatter = logging.Formatter(
        "%(levelname)8s | %(asctime)s | %(name)s | %(filename)s:%(funcName)25s | Line# %(lineno)s | %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%SZ",
    )

    # Log to console
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    log.addHandler(handler)

    # Also log to a file
    file_handler = logging.FileHandler("portfolio.log")
    file_handler.setFormatter(formatter)
    log.addHandler(file_handler)
    log.debug("start")
    log.debug("finished")
    return log


HOST, PORT, CID = ('127.0.0.1', 7496, 10)


def run():
    with IB().connect(HOST, PORT, CID) as ib:
        ib.reqMarketDataType(3)
        # print(type(ib.portfolio()))
       #  print(ib.portfolio())
        # con_list = util.df(ib.portfolio()).loc[:,'contract']
        # con_list = util.df(ib.portfolio()).loc[:,'marketPrice']
        #  contract  position  marketPrice  marketValue  averageCost  unrealizedPNL  realizedPNL    account
        # df2=df.loc[(df['Discount'] >= 1200) | (df['Fee'] >= 23000 )]
       # con_list = util.df(ib.portfolio()).loc[:,'marketPrice']
        con_list = util.df(ib.portfolio())
        con_list.index()
        log.info(con_list)


# main
if __name__ == "__main__":
    # https://metana.io/blog/mastering-python-exception-handling-best-practices-for-try-except/
    try:
        log = init_logger()
        log.debug("program call direct")
        log.info("start program")
        run()
        log.info("finished program")
        exit(0)
    except Exception as e:
        print(f"An error occurred: {e}")
else:
    print("call as module")
