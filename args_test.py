
def test(url, timeout=30, **kwargs):
    print()
    for k in kwargs:
        print(f'{k} {kwargs[k]}')

test('testing.com', timeout=10, hello=True)
