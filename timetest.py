import functools
import time
import logging


logger = logging.getLogger('tasks')
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()

logger.addHandler(ch)

def timeit(func):
    """A decorator used to log the function execution time."""


    # Use functools.wraps to ensure function name is not changed
    # http://stackoverflow.com/questions/13492603/celery-task-with-multiple-decorators-not-auto-registering-task-name
    @functools.wraps(func)
    def wrap(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        dur = time.perf_counter() - start
        msg = {
            'task_name': func.__module__ + '.' + func.__name__,
            'duration': dur,

            # Use 'task_args' instead of 'args' because 'args' conflicts with
            # attribute of LogRecord
            'task_args': args,
            'task_kwargs': kwargs
        }
        print(dur)
        logger.info('Task %s %sms', func.__name__, int(dur *1000), extra=msg)
        return result

    return wrap


@timeit
def run():
    print('Sleeping')
    time.sleep(.025)
    print('Slept')


run()
