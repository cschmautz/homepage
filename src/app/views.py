#!/usr/bin/env python
"""
views.py

Module to manage the different API endpoints for my homepage application.
"""


import os
from operator import itemgetter
import json

from flask import render_template
from flask import request
from flask import flash
from flask import abort
from flask import Response

# import markdown
# from markdown import markdown, Markdown

import jinja2
from flask_wtf.csrf import CSRFProtect
import flask_wtf.csrf
import wtforms.validators
from mistune import markdown

from src.app.application import application

from src.app.utils import extos
from src.app.utils import commext
import src.app.forms as forms


# MD = Markdown(application, extensions=['fenced_code'])
SRC_ROOT = os.path.abspath(os.path.dirname(__file__) + '../../')
TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')

JINJA_ENV = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR),
                               autoescape=True)


def markd_jinja(text: str, *args, **kwargs) -> str:
    """
    Renders HTML content from a string.
    """
    # return markdown(text, *args, **kwargs)
    return markdown(text, escape=True)


JINJA_ENV.filters['markdown'] = markd_jinja
application.jinja_env = JINJA_ENV
CSRF = CSRFProtect(application)
CSRF.init_app(application)


@application.route('/', methods=['GET'])
def base():
    """
    Base route that should take the user to the portfolio home page.
    """
    data = extos.load_json_file(os.path.abspath('src/instance/data.json'))
    cards = [x for x in data['posts']
             if x['type'] == 'portfolio']

    if not cards:
        cards = []
    else:
        for entry in cards:
            entry['postDate'] = entry['postDate'][:10]

        cards = sorted(cards, key=itemgetter('id'), reverse=True)

    return render_template("portfolio.html",
                           title="mounds makes",
                           cards=cards)


@application.route('/index', methods=['GET'])
def index():
    """
    Base route that should take the user to the portfolio home page.
    """
    data = extos.load_json_file(os.path.abspath('src/instance/data.json'))
    cards = [x for x in data['posts']
             if x['type'] == 'portfolio']

    if not cards:
        cards = []
    else:
        for entry in cards:
            entry['postDate'] = entry['postDate'][:10]

        cards = sorted(cards,
                       key=itemgetter('id'),
                       reverse=True)

    return render_template("portfolio.html",
                           title="mounds makes",
                           cards=cards)


@application.route('/portfolio', methods=['GET'])
def portfolio():
    """
    Main route to serve up the 'portfolio' section of the site.
    """
    data = extos.load_json_file(os.path.abspath('src/instance/data.json'))
    cards = [x for x in data['posts']
             if x['type'] == 'portfolio']

    if not cards:
        cards = []
    else:
        for entry in cards:
            entry['postDate'] = entry['postDate'][:10]

        cards = sorted(cards, key=itemgetter('id'), reverse=True)

    return render_template("portfolio.html",
                           title="mounds makes",
                           cards=cards)


@application.route('/portfolio/posts', methods=['GET'])
def portfolio_posts():
    """
    Main route to serve up the 'portfolio' section of the site.
    """
    data = extos.load_json_file(os.path.abspath('src/instance/data.json'))
    portfolio_data = [x for x in data['posts']
                      if x['type'] == 'portfolio']

    return json.dumps(portfolio_data)


@application.route('/portfolio/posts/<int:post>', methods=['GET'])
def portfolio_post(post=None):
    """
    Used to provide the specific pages for a portfolio entry. This will
    have posts in line with the posts in the blog area, however, they will
    be differentiated by a 'type' attribute, designating their role.

    Since all posts in this model have a unique post number, the 'role' is
    used to filter the returned list. Since each post is unique, it will
    run from oldest to newest based on the index of the 'id'.
    """
    data = extos.load_json_file(os.path.abspath('src/instance/data.json'))
    post_data = [x for x in data['posts']
                 if x['type'] == 'portfolio' and
                 x['id'] == post]

    if post_data:
        post_data = post_data[0]
        post_data['postDate'] = post_data['postDate'][:10]
    else:
        post_data = {'content': 'No portfolio entry found for that post id!',
                     'title': 'Content not found'}

    return render_template("portfolio_post.html",
                           title=post_data['title'],
                           content=post_data['content'])


@application.route('/blog', methods=['GET'])
def blog():
    """
    Endpoint to return the blog dashboard with the most recent posts.
    """
    data = extos.load_json_file(os.path.abspath('src/instance/data.json'))
    cards = [x for x in data['posts']
             if x['type'] == 'blog']

    if not cards:
        cards = []
    else:
        for entry in cards:
            entry['postDate'] = entry['postDate'][:10]

        cards = sorted(cards,
                       key=itemgetter('id'),
                       reverse=True)

    return render_template("blog.html",
                           title="mounds blogs",
                           cards=cards)


@application.route('/blog/posts', methods=['GET'])
def blog_posts():
    """
    Endpoint to serve up all the posts which reside on the server, or insert
    a new post if the right secret is given to the endpoint (future state).
    """
    data = extos.load_json_file(os.path.abspath('src/instance/data.json'))
    posts_data = [x for x in data['posts']
                  if x['type'] == 'blog']

    return json.dumps(posts_data)


@application.route('/blog/posts/<int:post>', methods=['GET'])
def blog_post(post):
    """ Endpoint that serves up a specific post which corresponds to the post
        'id' attribute. Similar to the portfolio post endpoint.
    """
    data = extos.load_json_file(os.path.abspath('src/instance/data.json'))
    post_data = [x for x in data['posts']
                 if x['type'] == 'blog' and
                 x['id'] == post]

    if post_data:
        post_data = post_data[0]
    else:
        post_data = {'content': 'No blog entry found for that post id!',
                     'title': 'Content not found'}

    return render_template("blog_post.html",
                           title=post_data['title'],
                           content=post_data['content'])


@application.route('/about', methods=['GET'])
def about():
    """
    Endpoint for retrieving 'about' section infomation.
    """
    data = extos.load_json_file(os.path.abspath('src/instance/data.json'))
    about_data = data['about']

    return render_template("about.html",
                           title="Who is Chris Schmautz (mounds)",
                           content=about_data)


@application.route('/contact', methods=['GET'])
def contact():
    """
    Endpoint for retrieving 'contact' section infomation.
    """
    data = extos.load_json_file(os.path.abspath('src/instance/data.json'))

    contact_data = data['contact']

    return render_template("contact.html",
                           title="Talk to the mounds",
                           content=contact_data)

@application.route('/message', methods=['POST'])
def message():
    """
    Endpoint to receive application messages, including contact form
    submissions and comments on blog posts.
    """
    data = request.form

    if (data is None or
            ('email' not in data.keys() or data['email'] == "") or
            ('subject' not in data.keys() or data['subject'] == "") or
            ('message' not in data.keys() or data['message'] == "")):
        abort(Response(response="Incomplete form data", status=400))

    try:
        flask_wtf.csrf.validate_csrf(data=data['csrf'])
    except wtforms.validators.ValidationError:
        abort(Response(response="There was a problem with the csrf token",
                       status=400))

    if forms.is_message_email_valid(email=data['email']) is False:
        abort(Response(response="Incorrect message email", status=400))

    elif forms.is_message_title_valid(title=data['subject']) is False:
        abort(Response(response="Incorrect message subject", status=400))

    elif forms.is_message_body_valid(body=data['message']) is False:
        abort(Response(response="Incorrect message body", status=400))

    else:
        if 'email' in data['messageType']:
            to_send = commext.form_message(msgfrom=data['email'],
                                           msgto=commext.GUSER,
                                           subject=data['subject'],
                                           content=data['message'])

            commext.gmail_send(to_send,
                               msgfrom=data['email'],
                               msgto=commext.GUSER)

            return Response(response="Message sent successfully", status=200)

        return Response(response="Invalid message type", status=400)

    return Response(response="Something went wrong processing the request",
                    status=500)
