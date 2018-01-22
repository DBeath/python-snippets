from spacy.en import English

text = u'Joe (Davy) Blogs, (jane@smith.com) Jane Smith; John Doe {john@doe.com} and Jim Jones - Tim (tim@tim.com)'

nlp = English()
doc = nlp(text)


# for i in doc:
#     print(i)
#     for ent in i.ents:
#         print(ent)
#         if ent.label_ == 'PERSON':
#             print("It's a person: {0}".format(ent))

print(doc)
# print doc.ents
# for ent in doc.ents:
#     if ent.label_ == 'PERSON':
#         print("It's a person: {0}".format(ent))
