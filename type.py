

class TestType:
    def __init__(self, *args, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


item = TestType(name='One', value=2)

print(type(item))
print(vars(item))
