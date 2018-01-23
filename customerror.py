
class CustomError(Exception):
    def __init__(self, msg):
        self.msg = msg


def raise_error():
    raise CustomError('This is an error')


try:
    raise_error()
except CustomError as e:
    print('Failed: {0}'.format(e))
