import traceback
import sys
from flask import Flask
import logging
import socket

try:
    raise Exception('This is a test')
except Exception as e:
    print(str(e))
    print
    print(sys.exc_info())
    print
    traceback.print_exc()


app = Flask(__name__)


class ContextFilter(logging.Filter):
    hostname = socket.gethostname()

    def filter(self, record):
        record.hostname = ContextFilter.hostname
        return True


def add_logger_stdout(app):
    """Creates a StreamHandler logger"""

    f = ContextFilter()
    app.logger.addFilter(f)

    stdout_handler = logging.StreamHandler(sys.stdout)
    FORMAT = '%(asctime)s %(hostname)s {0} :%(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'.format('Tester')
    formatter = logging.Formatter(FORMAT, datefmt='%Y-%m-%dT%H:%M:%S')
    stdout_handler.setFormatter(formatter)
    stdout_handler.setLevel(logging.INFO)
    stdout_handler._name = 'StreamHandler'
    app.logger.addHandler(stdout_handler)

add_logger_stdout(app)

@app.route('/')
def index():
    return 'Hello world'


@app.route('/e/')
def throw_error():
    try:
        raise Exception('This is a test')
    except Exception as e:
        app.logger.error(sys.exc_info())
        # print(str(e))
        # print
        # print(sys.exc_info())
        # print
        # traceback.print_exc()

    return 'Thrown exception'


if __name__ == '__main__':
    app.run(debug=False)
