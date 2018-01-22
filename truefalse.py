tests = ['blah', None, True, False, 'blah2']


def is_true(item):
    return item


result = list(filter(is_true, tests))

print(result)
