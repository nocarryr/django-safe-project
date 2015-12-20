"""This module defines the settings to be altered and how to handle them.

Each setting should contain a dict with the following keys:
    'value': The content to be placed in `local_settings.py`
    'default': The content will be set as the default value in `settings.py`
        `<SETTING_NAME> = getattr(local_settings, <SETTING_NAME>, <default>)`
    'update_dict': If `True`, the value in `settings.py` will be updated with
        the one in `local_settings.py`.  Useful for things like DATABASES so the
        default setup can be left alone until modification is needed.
        Note that a 'value' must be present, even if it is an empty dict.
        `<SETTING_NAME>.update(getattr(local_settings, <SETTING_NAME>))`
"""
SECRET_KEY = {'value':'{{ secret_key }}'}

DEBUG = {'value':True}

ALLOWED_HOSTS = {'default':[]}

DATABASES = {'value':{}, 'update_dict':True}
