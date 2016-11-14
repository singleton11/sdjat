from django.apps import AppConfig


class {{cookiecutter.app_name.split('_')|map('title')|join('')}}Config(AppConfig):
    name = 'apps.{{cookiecutter.app_name}}'
    verbose_name = '{{cookiecutter.app_name.split('_')|map('title')|join('')}}'
