
class Author():
    def __init__(self, name):
        self.name = name


a1 = Author('Test1')
a2 = Author('Test2')
a3 = Author('Testing Author')

authors = [a1, a2, a3]

author_string = str.join(', ', [a.name for a in authors])

print(author_string)
