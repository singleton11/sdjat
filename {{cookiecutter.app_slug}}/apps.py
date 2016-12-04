from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class {{cookiecutter.app_camel_case}}Config(AppConfig):
    name = 'apps.{{cookiecutter.app_slug}}'
    verbose_name = _('{{cookiecutter.app_name}}')
