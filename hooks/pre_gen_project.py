import re

# Validate ``app_camel_case`` and ``app_slug`` variables

CAMEL_CASE_REGEX = r'([A-Z][a-z0-9]+)+'
SLUG_REGEX = r'^[a-z0-9](_?[a-z0-9]+)*$'

app_camel_case = '{{cookiecutter.app_camel_case}}'
app_slug = '{{cookiecutter.app_slug}}'

assert re.match(SLUG_REGEX, app_slug)
assert re.match(CAMEL_CASE_REGEX, app_camel_case)
