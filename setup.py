from setuptools import setup

setup(
    name = "django-safe-project",
    version = "0.0.6",
    author = "Matthew Reid",
    author_email = "matt@nomadic-recording.com",
    description = ("Start Django projects with sensitive data outside of the "
                                   "global settings module"),
    url='https://github.com/nocarryr/django-safe-project',
    license='MIT',
    keywords = "django",
    packages=['django_safe_project'],
    include_package_data=True,
    scripts=['startproject.py'],
    entry_points={
        'console_scripts':[
            'django-safe-project = startproject:main',
        ],
    },
    setup_requires=['setuptools-markdown'],
    long_description_markdown_filename='README.md',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Security',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
)
