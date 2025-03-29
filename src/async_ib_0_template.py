# this should here my async template /w logging ;-)

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


# connect data for local running TWS
HOST, PORT, CID = ('127.0.0.1', 7496, 10)


def run():

    log.info("RUN START")
    try:
        with IB().connect(HOST, PORT, CID) as ib:
            ib.reqMarketDataType(3)

            con_list = util.df(ib.portfolio())

            # get akt. market data for each contract
            ib.qualifyContracts(*con_list)

            # get all contract
            # [position](https://www.investopedia.com/terms/p/position.asp)
            # [contract](https://www.investopedia.com/terms/o/optionscontract.asp)

            # we use here position for stocks and options ;-)
            positions = con_list['contract']
         
            # log.info("position => {}".format(position ))

            for pos in positions:
                # print("{}".format(pos))

                option = Option(pos)

                # print("Option => {}".format(option))

                print(" {} {} {} {}".format(
                    option.symbol,
                    option.strike,
                    option.lastTradeDateOrContractMonth,
                    option.primaryExchange,
                ))

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
