from sampo1.views import *
from rhombus.views.home import login as rb_login, logout as rb_logout


def index(request):
    return render_to_response('sampo:templates/generic_page.mako',
                              {}, request=request
                              )


def home(request):
    """return home page"""

    return render_to_response('sampo:templates/generic_page.mako', {}, request=request)


# TODO: add sampo home, simple and bar template


def login(request):
    return rb_login(request)


def logout(request):
    return rb_logout(request)