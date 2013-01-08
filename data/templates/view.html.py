# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1357607204.944007
_enable_loop = True
_template_filename = '/Users/tonthat/Desktop/sandbox/pylons/twitbox/twitbox/templates/view.html'
_template_uri = '/view.html'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        tweets = context.get('tweets', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<html>\n<head>\n  <title>FOOO</title>\n  <link rel="stylesheet" href="/css/app.css">\n</head>\n<body>\n')
        # SOURCE LINE 7
        for tweet in tweets:
            # SOURCE LINE 8
            __M_writer(u'    <div class="tweet">')
            __M_writer(escape(tweet.text))
            __M_writer(u'</div>\n')
        # SOURCE LINE 10
        __M_writer(u'</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


