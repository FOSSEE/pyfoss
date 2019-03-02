import feedparser
import eventlet


with eventlet.Timeout(10):
    url = 'http://feeds.feedburner.com/PythonInsider/.rss'


def get_rss():

    feed = feedparser.parse(url)
    posts_to_show = []

    for post in feed.entries[0:4]:
        title = post.title
        link = post.link
        posts_to_show.append((title, link))
    return posts_to_show
