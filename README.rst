Simple django app template
==========================

A very simple django app template.

To use this cookiecutter you should type:

.. code-block:: bash

    cookiecutter https://github.com/singleton11/sdjat

There are three values which you should provide to this cookiecutter template:

- ``app_name`` (default: "Polls")
- ``app_slug`` (default: "polls")
- ``app_camel_case`` (default: "Polls")

After project generation app structure will be following:


.. code-block:: bash

    <app_slug>
    ├── apps.py
    ├── __init__.py
    ├── models.py
    └── tests
        ├── __init__.py
        └── test_models.py
