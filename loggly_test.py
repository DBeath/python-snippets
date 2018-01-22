import logging
import logging.config
from loggly.handlers import HTTPSHandler
import time
from pprint import pprint
from pythonjsonlogger import jsonlogger
import uuid
import socket


class UTCFormatter(jsonlogger.JsonFormatter):
    """
    Format logs times in UTC
    """
    converter = time.gmtime


class ContextFilter(logging.Filter):
    hostname = socket.gethostname()

    def filter(self, record):
        record.hostname = ContextFilter.hostname
        record.request_id = uuid.uuid1()

token = 'f2766e74-5933-4654-b141-86b737c1b389'
url = 'https://logs-01.loggly.com/inputs/'+token+'/tag/python'
print(url)

handler = HTTPSHandler(url)

log_format = ('{ "loggerName":"%(name)s", "asciTime":"%(asctime)s", '
              '"fileName":"%(filename)s", '
              '"logRecordCreationTime":"%(created)f", '
              '"functionName":"%(funcName)s", "levelNo":"%(levelno)s", '
              '"lineNo":"%(lineno)d", "time":"%(msecs)d", '
              '"levelName":"%(levelname)s", "message":"%(message)s"}, '
              '"hostname:"%(hostname)s, "requestId":"%(request_id)s')


# formatter = jsonlogger.JsonFormatter(log_format)
formatter = UTCFormatter(log_format)

handler.setFormatter(formatter)

# logger = logging.getLogger('myLogger')


logger = logging.getLogger('myLogger')

logger.setLevel(logging.INFO)

logger.addHandler(handler)

pprint(vars(logger))
pprint(vars(handler))


def method3():
    raise Exception('This is a test exception')


def method2():
    method3()


def method1():
    method2()


try:
    method1()
except Exception as e:
    logger.exception(e)
