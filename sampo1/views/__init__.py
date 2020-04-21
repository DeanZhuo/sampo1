from rhombus.views import m_roles
from pyramid.httpexceptions import HTTPFound
from pyramid.renderers import render_to_response
from rhombus import get_dbhandler
from rhombus.lib.tags import *
from sampo1.lib.roles import *
from datetime import date
from rhombus.models.core import get_userid
