"""Testing our journal app."""

from pyramid import testing
import pytest

# @pytest.fixture
# def req():
#     the_request = testing.DummyRequest()
#     return the_request


# def test_home_page_renders_file_data(req):
#     """My home page view returns some data."""
#     from .views import home_page
#     reponse = home_page(req)
#     assert '<p class="lead">Claire Gatenby\'s learning journal submissions for Codefellows Python 401</p>'

def test_home_view():
    """Test that the home page returns what we expect."""
    from .views import home_page
    request = testing.DummyRequest()
    info = home_page(request)
    assert "entries" in info


# functional testing here

@pytest.fixture()
def testapp():
    """Create an instance of our app for testing."""
    from learning_journal_basic import main
    app = main({})
    from webtest import TestApp
    return TestApp(app)


def test_layout_root(testapp):
    """Test that the contents of the root page contains <article>."""
    response = testapp.get('/', status=200)
    html = response.html
    assert "Claire's Learning Journal ~ Python 401" in html.find("footer").text



def test_root_contents(testapp):
    """Test that the contents of the root page contains as many <article> tags as journal entries."""
    from .views import ENTRIES
    response = testapp.get('/', status=200)
    html = response.html
    assert len(ENTRIES) == len(html.findAll("article"))


# def test_detail_contents(testapp):
#     """Test that the detail view has the correct number of <p>s."""
#     from .views import ENTRIES
#     response = testapp.get('/journal/{id:\d+}', status=200)
#     html = response.html
#     assert