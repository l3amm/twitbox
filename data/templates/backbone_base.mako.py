# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1357617350.098159
_enable_loop = True
_template_filename = u'/Users/markgilbert/sandbox/pylons/twitbox/twitbox/mako/backbone_base.mako'
_template_uri = u'/backbone_base.mako'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<html>\n    <head>\n      <script type="text/javascript" src="/javascripts/templates/templates.js"></script>\n      <script type="text/javascript" src="/javascripts/libs/jquery-1.8.3.min.js"></script>\n      <script type="text/javascript" src="/javascripts/libs/jquery-ui-1.9.2.min.js"></script>\n      <script type="text/javascript" src="/javascripts/libs/underscore-1.4.3.min.js"></script>\n      <script type="text/javascript" src="/javascripts/libs/backbone-0.9.9.min.js"></script>\n    </head>\n    <body>\n        ')
        # SOURCE LINE 10
        __M_writer(escape(self.body()))
        __M_writer(u'\n    </body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


