# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1357613918.484823
_enable_loop = True
_template_filename = '/Users/markgilbert/sandbox/pylons/twitbox/twitbox/templates/sessions.html'
_template_uri = '/sessions.html'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'Hello from sessions controller')
        return ''
    finally:
        context.caller_stack._pop_frame()


