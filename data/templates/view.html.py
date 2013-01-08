# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1357618681.085621
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
        media = context.get('media', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<html>\n<head>\n  <title>TwitBox</title>\n  <link rel="stylesheet" href="/css/app.css">\n</head>\n<body>\n')
        # SOURCE LINE 7
        for tweet in tweets:
            # SOURCE LINE 8
            __M_writer(u'    <div class="tweet">\n      ')
            # SOURCE LINE 9
            __M_writer(escape(tweet.text))
            __M_writer(u'\n    </div>\n')
        # SOURCE LINE 12
        __M_writer(u'  \n')
        # SOURCE LINE 13
        for m in media:
            # SOURCE LINE 14
            __M_writer(u'    <img src="')
            __M_writer(escape(m))
            __M_writer(u'"/>\n')
        # SOURCE LINE 16
        __M_writer(u'</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


