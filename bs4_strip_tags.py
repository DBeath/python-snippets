from bs4 import BeautifulSoup, Comment, Tag
from pprint import pprint
import time

with open('/home/dbeath/code/python/brin.html', 'r') as f:
    html = f.read()

start = time.perf_counter()

soup = BeautifulSoup(html, 'html.parser')

# pprint(soup)

# pprint(str(soup))

def delete_style(soup):
    for tag in soup.find_all():
        if tag.name.lower() == 'style':
            tag.decompose()
        else:
            del tag['style']
            del tag['class']


def delete_comments(soup):
    for comment in soup.findAll(text=lambda text:isinstance(text, Comment)):
        comment.extract()


def find_empty_tags(soup):
    """
    Find all empty tags
    """
    # empty = s.find_all(lambda t: not t.contents or (
    #         not t.contents and (
    #             t.string is None or t.stripped_string == '' or t.string.replace('\n', '') == '')))
    # new_empty = list([x for x in empty if x.name not in ['a', 'br', 'img']])
    # return new_empty
    tags = soup.find_all()
    empty = []
    for t in tags:
        if t.name.lower() in ['a', 'br', 'img']:
            continue
        if not t.contents and not t.text:
            empty.append(t)
            continue
        if not has_tag_in_contents(t) and t.text and t.text.replace('\n', '').strip() == '':
            empty.append(t)
            continue

    return empty

def is_empty_tag(tag):
    if tag.name.lower() in ['a', 'br', 'img']:
        return False
    if not tag.contents and not tag.text:
        return True
    if not has_tag_in_contents(tag) and tag.text and tag.text.replace('\n', '').strip() == '':
        return True

def has_tag_in_contents(tag):
    for x in tag.contents:
        if isinstance(x, Tag):
            return True


def remove_empty_tags(soup):
    """
    Remove empty tags from html
    """
    # def find_empty_tags(soup):
    #     # empty = soup.find_all(lambda tag: tag.text is None or tag.text.strip() == "")
    #     empty = soup.find_all(lambda tag: not tag.contents)
    #     # empty = soup.find_all(lambda tag: not tag.contents or (not tag.contents and (tag.string is None or tag.stripped_string == "")))
    #     # return empty
    #     return [x for x in empty if x.name not in ['a', 'br', 'img']]

    # tags = find_empty_tags(soup)
    # while tags:
    #     pprint(tags)
    #     for tag in tags:
    #         print(f"Tag{{{tag}}}")
    #         print(tag.name)
    #         print()
    #         tag.extract()
    #     tags = find_empty_tags(soup)

    tags = soup.find_all(is_empty_tag)
    while tags:
        print(tags)
        for tag in tags:
            tag.extract()
        tags = soup.find_all(is_empty_tag)


delete_style(soup)
delete_comments(soup)
remove_empty_tags(soup)

dur = int((time.perf_counter() - start) * 1000)

print('\n--------------------------------------------------------------------------\n')

pretty = soup.prettify(formatter='html')
pprint(pretty)

output = str(soup)

print(type(output))

with open('brin_cleaned.html', 'w+') as f:
    f.write(pretty)


# print('\n--------------------------------------------------------------------------\n')
# with open('brin.txt', 'w+') as f:
#     f.write(soup.get_text())

# print(soup.get_text())

print(f'Duration: {dur}ms')
