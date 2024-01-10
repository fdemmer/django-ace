==========
django-ace
==========

|Build| |Coverage| |PyPI Download| |PyPI Python Versions| |PyPI License|

.. |Build| image:: https://github.com/fdemmer/django-ace/workflows/CI/badge.svg?branch=master
    :target: https://github.com/fdemmer/django-ace/actions?workflow=CI

.. |Coverage| image:: https://codecov.io/gh/fdemmer/django-ace/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/fdemmer/django-ace

.. |PyPI Download| image:: https://img.shields.io/pypi/v/fdemmer-django-ace.svg
   :target: https://pypi.python.org/pypi/fdemmer-django-ace/

.. |PyPI Python Versions| image:: https://img.shields.io/pypi/pyversions/fdemmer-django-ace.svg
   :target: https://pypi.python.org/pypi/fdemmer-django-ace/

.. |PyPI License| image:: https://img.shields.io/pypi/l/fdemmer-django-ace.svg
   :target: https://pypi.python.org/pypi/fdemmer-django-ace/


django-ace provides integration for `Ace - The High Performance Code Editor for the Web`__ with Django.

django-ace is a fork of Kit Sunde's django-ace-editor by Bradley Ayers and continued by Julien Palard et al.

This is another fork by Florian Demmer; Compare changelog and source to decide whether you need the changes or better use upstream.

.. __: https://ace.c9.io


Usage
=====

.. code-block:: python

    from django import forms
    from django_ace import AceWidget

    class EditorForm(forms.Form):
        text = forms.CharField(widget=AceWidget)

Syntax highlighting and static analysis can be enabled by specifying the
language:

.. code-block:: python

    class EditorForm(forms.Form):
        text = forms.CharField(widget=AceWidget(mode='css'))

Themes are also supported:

.. code-block:: python

    class EditorForm(forms.Form):
        text = forms.CharField(widget=AceWidget(mode='css', theme='twilight'))

To deactivate the syntax checker completely, disable the Web Worker:

.. code-block:: python

    class EditorForm(forms.Form):
        text = forms.CharField(widget=AceWidget(
            mode='css', theme='twilight', use_worker=False
        ))


All options, and their default values, are:

.. code-block:: python

    class EditorForm(forms.Form):
        text = forms.CharField(widget=AceWidget(
            mode=None,  # try for example "python"
            theme=None,  # try for example "twilight"
            use_worker=True,
            wordwrap=False,
            width="500px",
            height="300px",
            minlines=None,
            maxlines=None,
            showprintmargin=True,
            showinvisibles=False,
            usesofttabs=True,
            tabsize=None,
            fontsize=None,
            toolbar=True,
            readonly=False,
            showgutter=True,  # To hide/show line numbers
            behaviours=True,  # To disable auto-append of quote when quotes are entered
        ))


Installation
============

1. Install using pip:

.. code-block:: shell

    pip install django_ace

2. Update ``INSTALLED_APPS``:

.. code-block:: python

    INSTALLED_APPS = (
        # ...
        'django_ace',
    )


Example Project
===============

There's an example project included in the source, to try it do:

.. code-block:: shell

    # install in virtualenv
    cd example/
    virtualenv .env
    . .env/bin/activate
    pip install -e ..
    # prepare sqlite database
    ./manage.py makemigrations app
    ./manage.py migrate
    # user for admin access
    ./manage.py createsuperuser
    # run dev-server
    ./manage.py runserver

Then browser to ``http://localhost:8000`` or ``http://localhost:8000/admin``.


Change log
==========

v2.2.1
------

- Update Ace editor to version v1.32.3
- Expose extensions, contributed by @okaycj in upstream v1.32.0

v2.1.0
------

- Update Ace editor to version v1.31.2
- Add CSS to work with admin changes in Django 4.2.
  Now you can use `width="100%"` without breaking the layout.
  (Anh Tran <anhtran.sky@gmail.com> in upstream v1.15.4)
- Replace flake8 with ruff

v2.0.0
------

- Update Ace editor to version v1.10.1 and use minified build
- General cleanup and modernization of code
- Update example with widget in ``TabularInline``
- Update packaging by Julien Palard
- Python >= 3.6 is required

v1.1.0
------

- Rewrite of ``init()`` function to support admin inline-forms
- New widget option ``use_worker``
- Use template engine to generate widget HTML
- Rewrite of boolean data attributes
- Add tests, update example with admin integration
- Last release supporting Python 2.7


v1.0.11
-------

- Support Grappelli inlines.


v1.0.10
-------

- FIX JavaScript error when using ``JavaScriptCatalog``.


v1.0.9
------

- New widget option ``showgutters`` to hide line numbers.
- New widget option ``behaviours`` to avoid auto-insert of quotes.


v1.0.8
------

- New widget option ``readonly``.
- Update ACE editor to version v1.4.12.


v1.0.7
------

- New widget option ``toolbar``.
- Update ACE editor to version v1.4.8.


v1.0.6
------

- New widget option ``fontsize``.
- Update ACE editor to version v1.4.7.


v1.0.5
------

- New widget option ``tabsize``.
- Upgrade ACE editor to version v1.4.2.


v1.0.4
------

- Update Django compatibility to ``>1.11,<=2.1``
- New widget options ``minLines``, ``maxLines``, ``showinvisibles``, ``usesofttabs``.
- Upgrade ACE editor to version v1.4.0.
- Updated example for Django 1.11
- PEP8 improvements

v1.0.2
------

- Upgrade ACE editor to version 1.1.8
- Add support for showprintmargin

v1.0.1
------

- Add support for Django 1.7 by removing deprecated imports.

v1.0.0
------

- Initial release.
