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
    if project_name is None:
        project_name = sys.argv[1]
    dj_root = os.path.dirname(django.__file__)
    source_dir = os.path.join(dj_root, 'conf', 'project_template')
    tmp_dir = tempfile.mkdtemp()
    dest_dir = os.path.join(tmp_dir, 'project_template')

    try:
        template = build_template(source=source_dir, dest=dest_dir)
        r = start_project(project_name, dest_dir)
    finally:
        shutil.rmtree(tmp_dir)

if __name__ == '__main__':
    main()
