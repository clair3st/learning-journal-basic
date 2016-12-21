"""Serve the website files."""


from pyramid.view import view_config
import os

HERE = os.path.dirname(__file__)


ENTRIES = [
    {"title": "Day 11",
     "id": 1,
     "body": """Today we learnt so many new things! First we
     learned about web frameworks and in particular how to use Pyramid.
     We went pretty quickly over this so I got a little lost in class but
     doing it twice for both me and my partner's learning journal was great
     practice. We also learned about deploying simple python apps to heroku.
     I had a surprsing amount of difficulty with this. after a lot of
     frustration I realized t was a problem with my file tree setup.
     Luckily I was able to get my site up and running.<br>
            I'm really enjoying the data structures at the moment.
     I feel like the more we do the easier it is for me to get
     my head around how they work and what they could be used for.
     Today was a deque which was similar to a queue and a double
     linked list.""",
     "creation_date": "Dec 19, 2016"},

    {"title": "Day 12",
     "id": 2,
     "creation_date": "Dec 20, 2016",
     "body": """I learned about the binary heap data structure. I can see that
     this would shorten the time needed to sort data compated to just looping
     through a normal list. I found it hard to get my head around not using
     nodes when we implemented it using a list in python.<br>
     We also learned about jinja2 today and using it as a templating system for
     a website. I think initially I was a little freaked out by jinja when I
     did the reading but now that I've had the chance to practise and implement
     it in this site I feel like I'm starting to get the hang of it. """},
]


@view_config(route_name="home", renderer="templates/list.jinja2")
def home_page(request):
    """View the home page."""
    return {"entries": ENTRIES}


@view_config(route_name="new", renderer="templates/new.jinja2")
def new_entry(request):
    """View the new entry page."""
    return {"entries": ENTRIES}


@view_config(route_name="detail", renderer="templates/detail.jinja2")
def detail_page(request):
    """View the detail page."""
    entry_id = int(request.matchdict['id'])
    return {"entries": ENTRIES[entry_id - 1]}


@view_config(route_name="edit", renderer="templates/edit.jinja2")
def edit_page(request):
    """View the edit page."""
    entry_id = int(request.matchdict['id'])
    return {"entries": ENTRIES[entry_id - 1]}
