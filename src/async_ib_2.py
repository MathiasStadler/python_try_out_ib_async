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

    log.info("RUN START")
    try:
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
            
           # print(" => {}".format("Test"))
           # log.info("Type => {}").format( type(con_list))
            
            # get pandas Index
            # log.info(con_list.columns)
           #  log.info(con_list['contract'])
            
            positions = con_list['contract']

           #  print (" => {position.__class__}")
           # print("TYPE position => ".format(type(position)))
           # log.info("position => {}".format(position ))
            for pos in positions:
                print("{}".format(pos))
                pos

            # complete output
            # log.info(con_list.describe)
            
            log.info("RUN EXIT")
    except Exception as e:
        log.error("An error => {} occurred line:#{}".format(
            e, e.__traceback__.tb_lineno))


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
   # FROM HERE last entry
    # https://stackoverflow.com/questions/1278705/when-i-catch-an-exception-how-do-i-get-the-type-file-and-line-number
    except Exception as e:
        log.error("An error => {} occurred line:#{}".format(
            e, e.__traceback__.tb_lineno))


else:
    print("call as module")
