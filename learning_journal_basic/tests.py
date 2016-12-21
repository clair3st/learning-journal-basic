"""Testing our journal app."""

from pyramid import testing
import pytest


@pytest.fixture
def req():
    """Fixture for a dummy request."""
    the_request = testing.DummyRequest()
    return the_request


@pytest.fixture()
def testapp():
    """Create an instance of our app for testing."""
    from learning_journal_basic import main
    app = main({})
    from webtest import TestApp
    return TestApp(app)


def test_home_view(req):
    """Test that the home page returns what we expect."""
    from .views import home_page
    info = home_page(req)
    assert "entries" in info


# functional testing here

def test_layout_root(testapp):
    """Test that the contents of the root page contains <article>."""
    response = testapp.get('/', status=200)
    html = response.html
    assert "Claire's Learning Journal ~ Python 401" in html.find("footer").text


def test_root_contents(testapp):
    """Test that home contains as many <article> tags as journal entries."""
    from .views import ENTRIES
    response = testapp.get('/', status=200)
    html = response.html
    assert len(ENTRIES) == len(html.findAll("article"))


def test_new_layout(testapp):
    """Test that the contents of the root page contains <article>."""
    response = testapp.get('/journal/new-entry', status=200)
    html = response.html
    assert "Title" in html.find("h2").text


# def test_detail_view():
#     """Test that the detail page contains 'title'."""
#     from .views import detail_page
#     request = testing.DummyRequest()
#     info = detail_page(request)
#     assert "title" in info
