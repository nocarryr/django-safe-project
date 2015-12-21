[![Build Status](https://travis-ci.org/nocarryr/django-safe-project.svg?branch=master)](https://travis-ci.org/nocarryr/django-safe-project)

# django-safe-project
Creates and uses the installed Django project template to keep sensitive data out of global settings.

## Installation
To install `django-safe-project` run:
```
pip install django-safe-project
```
Or download the latest release [here](https://github.com/nocarryr/django-safe-project/releases/latest) and install by running:
```
python setup.py install
```

## Usage

When installed, call
```
django-safe-project <projectname>
```
instead of
```
django-admin startproject <projectname>
```

This will create a separate module in the project path named `local_settings.py` containing all the things you don't want to ever place in any sort of VCS ever.

`local_settings.py` will then be gitignored and its contents imported into the main `settings.py` module.

Currently the list of settings this handles are:

* SECRET_KEY (obviously)
* DATABASES (duh!!!)
* DEBUG
* ALLOWED_HOSTS
