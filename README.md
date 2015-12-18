# django-safe-project
Creates and uses the installed Django project template to keep sensitive data out of global settings.

When installed, call `django-safe-project <projectname>` instead of `django-admin startproject <projectname>`

This will create a separate module in the project path `local_settings.py` containing all the things you don't want to ever place in any sort of VCS ever.

`local_settings.py` will then be gitignored and its contents imported into the main `settings.py` module.

Currently the list of settings this handles are:

* SECRET_KEY (obviously)
* DATABASES (duh!!!)
* DEBUG
* ALLOWED_HOSTS
