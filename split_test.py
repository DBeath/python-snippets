import re
from nameparser import HumanName
from pprint import pprint
import unittest

names = "Joe (Davy) Blogs, (jane@smith.com) Jane Smith; John Doe {john@doe.com} and Jim Jones - Tim (tim@tim.com)"

delimiters = ',', ';', 'and', '&', 'the', '-', '--'

regexPattern = '|'.join(map(re.escape, delimiters))
regex = re.compile(regexPattern)

emailRegex = re.compile('[\w.-]+@[\w.-]+')
emailWithBracketsRegex = re.compile('[\{\(\[\<]?[\w.-]+@[\w.-]+[\}\]\)\>]?')

# out = split(names)
# print(out)

# authors = []


class Author:
    def __init__(self, first=None, last=None, email=None):
        if first and last:
            self.name = ' '.join([first, last])
        elif first:
            self.name = first
        elif last:
            self.name = last
        self.first = first
        self.last = last
        self.email = email


def split(string, maxsplit=0):
    return regex.split(string, maxsplit)


def parse_name(item):
    emailGroup = emailRegex.search(item)
    email = None
    if emailGroup:
        email = emailGroup.group(0)
    item = emailWithBracketsRegex.sub('', item)

    item = item.strip()
    name = HumanName(item)
    author = Author(name.first, name.last)
    if email:
        author.email = email
    return author


def parse_namestring(string):
    authors = []
    names = split(string)
    for i, item in enumerate(names):
        author = parse_name(item)
        authors.append(author)
    return authors

# pprint(authors)

names = [
    ('Joe Blogs (joe@blogs)', [('Joe', 'Blogs', 'joe@blogs')]), (
        'Jane Doe, John Doe (john@doe.com)', [('Jane', 'Doe'),
                                              ('John', 'Doe', 'john@doe.com')])
]


class TestAuthor:
    def __init__(self, namestring, expected):
        self.namestring = namestring
        self.expected = expected


tests = [
    TestAuthor('Joe Blogs (joe@blogs.com)',
               [Author('Joe', 'Blogs', 'joe@blogs.com')]), TestAuthor(
                   '(jane@doe.com) Jane Doe',
                   [Author('Jane', 'Doe', 'jane@doe.com')]),
    TestAuthor(
        'Joe (Davy) Blogs, (jane@smith.com) Jane Smith',
        [Author('Joe', 'Blogs'), Author('Jane', 'Smith', 'jane@smith.com')]),
    TestAuthor(
        'Joe (Davy) Blogs, (jane@smith.com) Jane Smith; John Doe {john@doe.com} and Jim Jones - Tim (tim@tim.com)',
        [Author('Joe', 'Blogs'), Author('Jane', 'Smith', 'jane@smith.com'),
         Author('John', 'Doe', 'john@doe.com'), Author('Jim', 'Jones'),
         Author('Tim', None, 'tim@tim.com')])
]


class TestAuthorParsing(unittest.TestCase):
    def test_authors(self):
        for test in tests:
            result = parse_namestring(test.namestring)
            print(result)
            for i, item in enumerate(result):
                self.assertEqual(result[i].first, test.expected[i].first)
                self.assertEqual(result[i].last, test.expected[i].last)
                self.assertEqual(result[i].email, test.expected[i].email)


if __name__ == '__main__':
    unittest.main()
