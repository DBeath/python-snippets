from newspaper import Article

url = "http://qz.com/829043/marijuana-on-the-ballot-after-nov-8-five-more-us-states-may-legalize-marijuana-for-recreational-use/"

article = Article(url)

article.download()

article.parse()

print(article.authors)

print(article.top_image)

print(article.title)
