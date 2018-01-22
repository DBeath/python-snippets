from testfixtures import LogCapture
from logging import getLogger
from pprint import pprint

logger = getLogger()

pprint(vars(logger))

with LogCapture() as l:
    logger.error('Testing error handling', exc_info=True)

    for r in l.records:
        pprint(vars(r))
