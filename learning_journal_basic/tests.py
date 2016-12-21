"""Testing our journal app."""

from pyramid import testing
import pytest

@pytest.fixture
def req():
    the_request = testing.DummyRequest()
    return the_request


def test_home_page_renders_file_data(req):
    """My home page view returns some data."""
    from .views import home_page
    reponse = home_page(req)
    assert '<p class="lead">Claire Gatenby\'s learning journal submissions for Codefellows Python 401</p>'
