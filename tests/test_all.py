
def test(tmpdir):
    print('tmpdir: ', tmpdir)
    import os
    import subprocess
    with tmpdir.as_cwd():
        subprocess.call(['django-safe-project', 'myproject'])
        project_path = tmpdir.join('myproject')
        print('Project created: %s' % (project_path))
        subprocess.call([str(project_path.join('manage.py')), 'test'])
