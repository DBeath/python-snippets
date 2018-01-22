import newspaper

qz_paper = newspaper.build('http://cnn.com')

print(qz_paper)
print(qz_paper.articles)
for article in qz_paper.articles:
    print(article.url)
    print(article.authors)

# from newspaper import Article

# url = 'http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ix-pagination'

# a = Article(url)

# article = a.download()
# print(article)

# # a.download()
# # a.parse()

# print(a.title)
# print(a.authors)
