from faker import Faker

fake = Faker()

paras = fake.paragraphs(nb=5)

print(type(paras))

# print(paras)


def list_to_html_paragraphs(lst):
    return u"<p>{0}</p>".format("</p><p>".join(lst))


print(list_to_html_paragraphs(paras))


print()

print(fake.text())
