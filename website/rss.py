import feedparser
import eventlet


with eventlet.Timeout(10):
    url = 'http://afeeds.feedburner.com/PythonInsider/.rss'


def get_rss():

    feed = feedparser.parse(url)
    posts_to_show = []

    for post in feed.entries[0:4]:
        title = post.title
        link = post.link
        posts_to_show.append((title, link))
    if not posts_to_show:
        posts_to_show = [('Click here for latest news from python.org',
                               'https://pythoninsider.blogspot.com/')]
    return posts_to_show
