import os
import os.path
import re

from collections import Callable
from datetime import date
import platform

from sublime_plugin import TextCommand

import sys
ST3 = sys.version_info >= (3, 3)

def getuser():
    OS = platform.system()
    if OS == 'Darwin':
        import Foundation
        return Foundation.NSFullUserName()
    elif OS == 'Linux':
        import pwd
        return pwd.getpwuid(os.getuid()).pw_gecos.split(',')[0]
    else:
        import getpass
        return getpass.getuser()


# This must be computed on import because of the way ST2 load plugins (__file__
# ends up being relative to plugin's directory and cwd may change later).
SNIPPETS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                            'snippets'))

# Mapping of additional snippet variable names to their values. If the value is
# callable, it is called on snippet insertion to compute actual value.
SNIPPET_VARS = {
    'YEAR': date.today().year,  # TM_YEAR doesn't seem to be supported.
    'USER': getuser()  # TM_FULLNAME doesn't seem to be supported.
}


def inc_placeholder(match):
    ''' Return matched text with number captured by group "num" increased. '''
    s = match.string
    a, b = match.span()
    i, j = match.span('num')
    return s[a:i] + str(int(s[i:j]) + 1) + s[j:b]


def load_snippet(file_name):
    # Load the file assuming UTF-8.
    mode = 'rb' if ST3 else 'rU'
    with open(os.path.join(SNIPPETS_DIR, file_name), mode) as f:
        text = f.read().decode('utf-8')

    # Wrap everything in one big tabstop and renumber old tabstops. This is
    # done for technical reasons to support automatic commenting/warpping
    # inserted text.
    text = re.sub(r'(?:\\\\)*\$(\{)?(?P<num>\d+)(?(1)[:/}]|)', inc_placeholder,
                  text)
    text = u'${{1:{0}}}'.format(text)

    return text


class InsertLicenceCommand(TextCommand):
    def run(self, edit, name):
        view = self.view
        settings = view.settings()

        comment_style = settings.get('licence_comment_style', 'line')
        if comment_style not in ('none', 'line', 'block'):
            raise ValueError('Invalid value for licence_comment_style setting')

        wrap_lines = settings.get('licence_wrap_lines', False)
        if wrap_lines not in (True, False):
            raise ValueError('Invalid value for licence_wrap_lines setting')

        args = {'contents': load_snippet(name)}
        for key, value in SNIPPET_VARS.items():
            if isinstance(value, Callable):
                value = value()
            args[key] = str(value) if ST3 else unicode(value)
        view.run_command('insert_snippet', args)

        # Since load_snippet wraps everything in one big tabstop, the whole
        # inserted text is now selected.
        if comment_style != 'none':
            view.run_command('toggle_comment',
                             {'block': comment_style == 'block'})
        if wrap_lines:
            view.run_command('wrap_lines')

        # Proceed to original first tabstop.
        view.run_command('next_field')

    def is_enabled(self):
        return len(self.view.sel()) == 1
