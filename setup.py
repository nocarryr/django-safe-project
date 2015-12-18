from setuptools import setup

setup(
    name = "django-safe-project",
    version = "0.0.1",
    author = "Matthew Reid",
    author_email = "matt@nomadic-recording.com",
    description = ("Start Django projects with sensitive data outside of the "
                                   "global settings module"),
    keywords = "django",
    packages=['django_safe_project'],
    scripts=['startproject.py'],
    entry_points={
        'console_scripts':[
            'django-safe-project = startproject:main',
        ],
    },
)
