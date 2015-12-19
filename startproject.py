#! /usr/bin/env python

import os
import sys
import shutil
import tempfile

import django
from django.core.management import call_command

from django_safe_project.template import Template

def build_template(**kwargs):
    template = Template(**kwargs)
    template.build_dest()
    return template

def start_project(project_name, template_dir):
    args = ['startproject', sys.argv[1]]
    opts = {'template':template_dir}
    return call_command(*args, **opts)

def main(project_name=None):
    """Main function to start a project using django-safe-project.

    Finds the location of the project template in the available django package.
    Creates a temp directory to copy and modify the template.
    Calls `django-admin startproject <project_name>` and supplies it with
    the modified template.

    :param project_name: The name of the project to create.
                         (If None, uses the first command line argument)

    """
    if project_name is None:
        project_name = sys.argv[1]
    dj_root = os.path.dirname(django.__file__)
    source_dir = os.path.join(dj_root, 'conf', 'project_template')
    tmp_dir = tempfile.mkdtemp()
    dest_dir = os.path.join(tmp_dir, 'project_template')

    try:
        build_template(source=source_dir, dest=dest_dir)
        start_project(project_name, dest_dir)
    finally:
        shutil.rmtree(tmp_dir)

if __name__ == '__main__':
    main()
