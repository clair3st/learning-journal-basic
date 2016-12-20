

def includeme(config):
    """This function adds routes to pyramid's configurator."""
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')