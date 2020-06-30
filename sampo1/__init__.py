from pyramid.config import Configurator
from rhombus import get_dbhandler, cerr, init_app, RhoRequest, get_userobj
from rhombus.models.core import set_func_userid
from .views import *


def includeme(config):
    """ this configuration must be included as the last order
    """

    set_func_userid(get_userid_func)

    config.add_static_view('static', 'static', cache_max_age=3600)

    # override assets here
    config.override_asset('rhombus:templates/base.mako', 'sampo1:templates/base.mako')
    config.override_asset('rhombus:templates/plainbase.mako', 'sampo1:templates/plainbase.mako')

    # add route and view for home ('/'), /login and /logout
    config.add_route('home', '/')
    config.add_view('sampo1.views.home.index', route_name='home')

    config.add_route('login', '/login')
    config.add_view('sampo1.views.home.login', route_name='login')

    config.add_route('logout', '/logout')
    config.add_view('sampo1.views.home.logout', route_name='logout')

    # below are example for route for class-based viewer
    # the same thing can be achieved using add_view_route_class()
    #
    # config.add_route('post-add', '/add')
    # config.add_view('sampo1.views.post.PostViewer', attr='add', route_name='post-add')
    #
    # config.add_route('post-edit', '/posts/{id}@@edit')
    # config.add_view('sampo1.views.post.PostViewer', attr='edit', route_name='post-edit')
    #
    # config.add_route('post-view', '/posts/{id}')
    # config.add_view('sampo1.views.post.PostViewer', attr='index', route_name='post-view')

    # add additional routes and views here
    # TODO: add views and routes

def get_userid_func():
    return get_dbhandler().session().user.id

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    with Configurator(settings=settings) as config:
        config.set_request_factory(RhoRequest)
        config.add_request_method(get_userobj, 'user', reify=True)
        config.include('.models')
        config.add_static_view(name='rhombus_static', path="rhombus:static/")
        config.include('pyramid_mako')
        includeme(config)
        config.scan()
    return config.make_wsgi_app()

    # """This is the original"""
    #
    # with Configurator(settings=settings) as config:
    #     config.include('.models')
    #     config.include('pyramid_mako')
    #     includeme(config)
    #     config.scan()
    # return config.make_wsgi_app()
    #
    # """with rhombus init app"""
    #
    # cerr('sampo main() is running...')
    #
    # # attach rhombus to /mgr url, include custom configuration
    # config = init_app(global_config, settings, prefix='/mgr',
    #                   include=includeme, include_tags=['sampo1.includes'])
    #
    # return config.make_wsgi_app()
