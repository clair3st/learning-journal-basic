"""Serve the website files."""


# from pyramid.response import Response
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
    linked list..""",
     "creation_date": "Dec 19, 2016"},

    {"title": "Day 12",
     "id": 2,
     "creation_date": "Dec 20, 2016",
     "body": "I learned stuff, it was hard."},
]


@view_config(route_name="home", renderer="templates/list.jinja2")
def home_page(request):
    """View the home page."""
    return {"entries": ENTRIES}


# @view_config(route_name="home", renderer="string")
# def home_page(request):
#     """View the home page."""
#     file_data = open(os.path.join(HERE, 'templates/main.html')).read()
#     # return Response(imported_text)
#     return file_data


# @view_config(route_name="new", renderer="string")
# def new_entry(request):
#     """View the new entry page."""
#     imported_text = open(os.path.join(HERE, 'templates/new.html')).read()
#     # return Response(imported_text)
#     return imported_text


@view_config(route_name="detail", renderer="templates/detail.jinja2")
def detail_page(request):
    """View the detail page."""
    entry_id = request.matchdict['id']
    dictionary_filtered = [entry for entry in ENTRIES if entry['id'] == int(entry_id)]
    # import pdb; pdb.set_trace()
    return {"entries": dictionary_filtered[0]}


# @view_config(route_name="edit", renderer="string")
# def edit_page(request):
#     """View the edit page."""
#     imported_text = open(os.path.join(HERE, 'templates/edit.html')).read()
#     # return Response(imported_text)
#     return imported_text


# # def includeme(config):
# #     """Configure the journal pages for viewing."""
# #     config.add_view(home_page, route_name='home')
# #     config.add_view(new_entry, route_name='new')
# #     config.add_view(detail_page, route_name='detail')
# #     config.add_view(edit_page, route_name='edit')
