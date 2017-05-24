""" views.py

    Module to manage the different API endpoints for my homepage applicationlication.
"""

import os
from operator import itemgetter
import json

from flask import render_template
import markdown
from markdown import markdown, Markdown
import jinja2

from src import application
from src.utils import extos

MD = Markdown(application, extensions=['fenced_code'])
TOP_LEVEL_DIR = (os.path.abspath(__file__) + '../')
TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')

JINJA_ENV = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR),
                               autoescape=True)

def markd_jinja(text, *args, **kwargs):
    """ Renders HTML content from a string.
    """
    return markdown(text, *args, **kwargs)

JINJA_ENV.filters['markdown'] = markd_jinja
application.jinja_env = JINJA_ENV

@application.route('/', methods=['GET'])
def base():
    """ Base route that should take the user to the portfolio home page.
    """
    return render_template("portfolio.html", title="mounds")

@application.route('/index', methods=['GET'])
def index():
    """ Base route that should take the user to the portfolio home page.
    """
    return render_template("portfolio.html", title="mounds")


@application.route('/portfolio', methods=['GET'])
def portfolio():
    """ Main route to serve up the 'portfolio' section of the site.
    """
    data = extos.load_json_file(os.path.abspath('instance/data.json'))
    cards = [x for x in data['posts'] if x['type'] == 'portfolio']

    if(not cards):
        cards = []
    else:
        for entry in cards:
            entry['postDate'] = entry['postDate'][:10]

        cards = sorted(cards, key=itemgetter('id'), reverse=True)

    return render_template("portfolio.html", title="mounds", cards=cards)


@application.route('/portfolio/posts', methods=['GET'])
def portfolio_posts():
    """ Main route to serve up the 'portfolio' section of the site.
    """
    data = extos.load_json_file(os.path.abspath('instance/data.json'))
    portfolio_data = [x for x in data['posts'] if x['type'] == 'portfolio']

    return json.dumps(portfolio_data)


@application.route('/portfolio/posts/<int:post>', methods=['GET'])
def portfolio_post(post=None):
    """ Used to provide the specific pages for a portfolio entry. This will
        have posts in line with the posts in the blog area, however, they will
        be differentiated by a 'type' attribute, designating their role.

        Since all posts in this model have a unique post number, the 'role' is
        used to filter the returned list. Since each post is unique, it will
        run from oldest to newest based on the index of the 'id'.
    """
    data = extos.load_json_file(os.path.abspath('instance/data.json'))
    post_data = [x for x in data['posts']
                  if x['type'] == 'portfolio' and
                  x['id'] == post]

    if(post_data):
        post_data = post_data[0]
        post_data['postDate'] = post_data['postDate'][:10]
    else:
        post_data = {'content': 'No portfolio entry found for that post id!',
                     'title': 'Content not found'}

    return render_template("portfolio_post.html", title=post_data['title'], content=post_data['content'])


@application.route('/blog', methods=['GET'])
def blog():
    """ Endpoint to return the blog dashboard with the most recent posts.
    """
    data = extos.load_json_file(os.path.abspath('instance/data.json'))
    cards = [x for x in data['posts'] if x['type'] == 'blog']

    if(not cards):
        cards = []
    else:
        for entry in cards:
            entry['postDate'] = entry['postDate'][:10]

        cards = sorted(cards, key=itemgetter('id'), reverse=True)

    return render_template("blog.html", title="Test", cards=cards)


@application.route('/blog/posts', methods=['GET'])
def blog_posts():
    """ Endpoint to serve up all the posts which reside on the server, or insert
        a new post if the right secret is given to the endpoint
    """
    data = extos.load_json_file(os.path.abspath('instance/data.json'))
    posts_data = [x for x in data['posts']
                  if x['type'] == 'blog']

    return json.dumps(posts_data)


@application.route('/blog/posts/<int:post>', methods=['GET'])
def blog_post(post):
    """ Endpoint that serves up a specific post which corresponds to the post
        'id' attribute. Similar to the portfolio post endpoint.
    """
    data = extos.load_json_file(os.path.abspath('instance/data.json'))
    post_data = [x for x in data['posts']
                 if x['type'] == 'blog' and
                 x['id'] == post]

    if(post_data):
        post_data = post_data[0]
    else:
        post_data = {'content': 'No blog entry found for that post id!',
                     'title': 'Content not found'}

    return render_template("blog_post.html", title=post_data['title'], content=post_data['content'])

@application.route('/about', methods=['GET'])
def about():
    """ Endpoint for retrieving 'about' section infomation.
    """
    data = extos.load_json_file(os.path.abspath('instance/data.json'))
    about_data = data['about']

    return render_template("about.html", title="About Chris Schmautz", content=about_data)

@application.route('/contact', methods=['GET'])
def contact():
    """ Endpoint for retrieving 'contact' section infomation.
    """
    data = extos.load_json_file(os.path.abspath('instance/data.json'))
    contact_data = data['contact']

    return render_template("contact.html", title="How to get in touch", content=contact_data)