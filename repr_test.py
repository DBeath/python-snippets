import logging

class Entry:
    def __init__(self, title, id):
        self.title = title
        self.id = id
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self.title}, {self.id})'

    def __str__(self):
        return f'{self.__class__.__name__}({self.title})'


entry = Entry('testing', 1)

print(entry)
print(str(entry))
print(repr(entry))
print('This is entry {0}'.format(entry))

logging.basicConfig(level=logging.DEBUG)
logging.info('This is entry %s', entry)
logging.info('This is entry {0} with .format'.format(entry))


entry2 = Entry('Second Test', 2)

entries = [entry, entry2]

print(entries)
print(str(entries))
print(list(map(str, entries)))

logging.info('Entries: {0}'.format(list(str(e) for e in entries)))
