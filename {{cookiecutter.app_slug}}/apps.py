from django.apps import AppConfig

class {{cookiecutter.app_camel_case}}Config(AppConfig):
    name = 'apps.{{cookiecutter.app_slug}}'
    verbose_name = '{{cookiecutter.app_name}}'