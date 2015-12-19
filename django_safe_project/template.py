import os
import sys
import shutil

from django_safe_project import safe_settings

PY3 = sys.version_info.major > 2

if PY3:
    basestring = str

class Template(object):
    """Handles copying and modifying the project template.

    :param source: Source path of the project template
    :param dest: Destination for modified template

    """
    def __init__(self, **kwargs):
        self.source = kwargs.get('source')
        self.dest = kwargs.get('dest')
    def build_dest(self):
        """Initiates the copy/modification process.

        This is not called by the constructor.
        """
        ign = shutil.ignore_patterns('*.pyc')
        shutil.copytree(self.source, self.dest, ignore=ign)
        self.build_local_settings()
        self.update_settings()
        self.build_gitignore()
    def build_local_settings(self):
        """Generates the local_settings.py module.

        Uses the contents of safe_settings.py.
        """
        filename = os.path.join(self.dest, 'project_name', 'local_settings.py')
        lines = []
        for attr, val in self.iter_safe_settings():
            if 'value' not in val:
                continue
            value = self.make_py_string(val['value'])
            lines.append(' = '.join([attr, value]))
        with open(filename, 'w') as f:
            f.write('\n'.join(lines))
    def update_settings(self):
        """Modifies the destination's settings.py module.

        Adds an import for the generated local_settings.py.
        All values for 'local_settings' are either replaced via `getattr`.
        """
        filename = os.path.join(self.dest, 'project_name', 'settings.py')
        with open(filename, 'r') as f:
            lines = f.read().splitlines()
        def add_import():
            last_import = None
            for i, line in enumerate(lines):
                if line.startswith('import'):
                    last_import = i
                elif last_import is not None:
                    break
            lines.insert(last_import + 1, 'import local_settings')
        add_import()
        settings_dict = self.build_settings_dict(lines)
        for attr, val in self.iter_safe_settings():
            if 'default' in val:
                df = self.make_py_string(val['default'])
                value = "getattr(local_settings, '%s', %s)" % (attr, df)
            else:
                value = "getattr(local_settings, '%s')" % (attr)
            if val.get('update_dict'):
                value = '%s.update(%s)' % (attr, value)
                lines.append(value)
            else:
                d = settings_dict[attr]
                lines[d['line_num']] = ' = '.join([attr, value])
        with open(filename, 'w') as f:
            f.write('\n'.join(lines))
    def build_gitignore(self):
        """Builds a `.gitignore` file to exclude the `local_settings` module.
        """
        filename = os.path.join(self.dest, 'project_name', '.gitignore')
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                lines = f.read().splitlines()
        else:
            lines = []
        if 'local_settings.py*' in lines:
            return
        lines.append('local_settings.py*')
        with open(filename, 'w') as f:
            f.write('\n'.join(lines))
    def iter_safe_settings(self):
        for attr in dir(safe_settings):
            if attr.startswith('_'):
                continue
            if not attr.isupper():
                continue
            yield attr, getattr(safe_settings, attr)
    def make_py_string(self, obj):
        if isinstance(obj, basestring):
            return "'%s'" % (obj)
        return str(obj)
    def build_settings_dict(self, lines):
        """Parses the `settings.py` file manually.

        Generates a `dict` of settings attributes with their corresponding
        line numbers.
        """
        d = {}
        bracket_chars = [['{', '[', '('], ['}', ']', ')']]
        def find_bracket_close(line_num, bracket_char):
            # The results of this function are not currently used, but may
            # possibly be in future versions.
            close_char = bracket_chars[1][bracket_chars[0].index(bracket_char)]
            num_open = 0
            for i, line in enumerate(lines[line_num:]):
                num_open += line.count(bracket_char) - line.count(close_char)
                if num_open == 0:
                    return line_num + i
        def find_next_setting(start_line):
            for i, line in enumerate(lines[start_line:]):
                if line.startswith('#'):
                    continue
                if ' = ' not in line:
                    continue
                s = line.split(' = ')[0]
                if not s.isupper():
                    continue
                if s in d:
                    continue
                value = line.split(' = ')[1].rstrip('\n').rstrip(' ')
                line_num = start_line + i
                if value[-1] in bracket_chars[0]:
                    last_line = find_bracket_close(line_num, value[-1])
                else:
                    last_line = line_num
                d[s] = {'line_num':line_num, 'last_line':last_line}
                return last_line
            return None
        line_num = 0
        while True:
            line_num = find_next_setting(line_num)
            if line_num is None:
                break
        return d
