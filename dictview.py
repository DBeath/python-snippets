class Author:
    def __init__(self, name, familyname=None):
        self.name = name
        self.familyname = familyname

    def __repr__(self):
        return u'{0}'.format(self.name)


authors = {'1': Author('Test Author'), '2': Author('Testy McTesterson')}
print(list(authors.values()))
print(u'Found {0} unique authors: {1}'.format(len(authors), list(authors.values())))

author2 = Author('Test Author 2')
name = author2.familyname or author2.name
print('Name: {0}'.format(name))
print(author2.familyname)
