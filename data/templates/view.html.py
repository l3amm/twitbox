# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1357674613.698404
_enable_loop = True
_template_filename = '/Users/winky/projects/twitbox/twitbox/mako/view.html'
_template_uri = '/view.html'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        media = context.get('media', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<html>\n<head>\n  <title>TwitBox</title>\n  <link rel="stylesheet" href="/css/app.css">\n</head>\n<body>\n  \n  <div id="media-box">\n')
        # SOURCE LINE 9
        for m in media:
            # SOURCE LINE 10
            __M_writer(u'      <div class="pic">\n        <a href="')
            # SOURCE LINE 11
            __M_writer(escape(m))
            __M_writer(u'"><img src="')
            __M_writer(escape(m))
            __M_writer(u'"/></a>\n      </div>\n')
        # SOURCE LINE 14
        __M_writer(u'  </div>\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


