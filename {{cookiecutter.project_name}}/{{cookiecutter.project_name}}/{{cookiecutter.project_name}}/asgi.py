"""
ASGI config for {{cookiecutter.project_name}} project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from configurations.asgi import get_asgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "{{cookiecutter.project_name}}.{{cookiecutter.project_name}}.settings",
)
os.environ.setdefault("DJANGO_CONFIGURATION", "Prod")

application = get_asgi_application()
