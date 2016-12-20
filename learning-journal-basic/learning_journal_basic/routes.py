"""Hold route info broken out of __init__."""

def includeme(config):
    """This function adds routes to pyramid's configurator."""
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('new', '/journal/new-entry')
    config.add_route('detail', '/journal/1')
    config.add_route('edit', '/journal/1/edit-entry')
