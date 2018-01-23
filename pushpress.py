import re

pushpressRegex = re.compile('\?pushpress=hub')

def is_wordpress_hub(url):
    """
    Returns a Regex Match object that evaluates to True if the url is
    a Wordpress Pushpress hub.
    """
    return pushpressRegex.search(url)

url = 'http://qz.com/?pushpress=hub'
url2 = 'http://pubsubhubbub.appspot.com/'

if is_wordpress_hub(url2) is None:
    print('Is not wordpress hub')
else:
    print('Is wordpress hub')
