Bump Ace version
================

To update the package's copy of Ace run the make target ``upgrade_ace``
and commit he copied files.
Optionally provide ``ACE_VERSION`` to use a specific commit/branch/tag.

.. code-block:: shell

    ACE_VERSION=v1.5.0 make upgrade_ace


How to release
==============

- Update the Changelog.
- Update version in :file:`setup.py` and :file:`django_ace/__init__.py`.
- Commit with a message like "Bump to version 1.0.9".
- Tag it, with the ``v`` prefix, like ``git tag v1.0.9``.
- Test it one last time.
- git push && git push --tags
- Ensure you have ``setuptools``, ``wheel``, and ``twine`` up to date.
- Build: ``python setup.py sdist bdist_wheel``.
- Push to pypi: ``twine upload dist/*``.
- Create realease from the tag on Github
