custom-unit-icons
=============================

|pypi-badge| |travis-badge| |codecov-badge| |doc-badge| |pyversions-badge|
|license-badge|

An Open edX Django plugin application for getting XBlock icons from modulestore. This allows customizing icon for each unit.

Setup Instructions
------------------------

On Open edX Devstack:

1. Clone this repo into your devstack's ``src`` folder::

    git clone git@github.com/open-craft/custom-unit-icons.git

2. Install it into LMS's and Studio's devstack python environment::

    make lms-shell
    pip install -e /edx/src/custom-unit-icons/
    logout

    make studio-shell
    pip install -e /edx/src/custom-unit-icons/
    logout

3. Set the following variable in your local settings (e.g. `lms/envs/private.py`)::

     GET_UNIT_ICON_IMPL = 'custom_unit_icons.icons.get_icon'

4. Restart LMS::

    make lms-restart

Usage instructions
-------------------

You need to override Studio theme to be able to modify icons for units.

License
-------

The code in this repository is licensed under the AGPL 3.0 unless
otherwise noted.

Please see ``LICENSE.txt`` for details.

How To Contribute
-----------------

Contributions are very welcome.

Please read `How To Contribute <https://github.com/edx/edx-platform/blob/master/CONTRIBUTING.rst>`_ for details.

Even though they were written with ``edx-platform`` in mind, the guidelines
should be followed for Open edX code in general.

The pull request description template should be automatically applied if you are creating a pull request from GitHub. Otherwise you
can find it at `PULL_REQUEST_TEMPLATE.md <https://github.com/edx/custom-unit-icons/blob/master/.github/PULL_REQUEST_TEMPLATE.md>`_.

The issue report template should be automatically applied if you are creating an issue on GitHub as well. Otherwise you
can find it at `ISSUE_TEMPLATE.md <https://github.com/edx/custom-unit-icons/blob/master/.github/ISSUE_TEMPLATE.md>`_.

Reporting Security Issues
-------------------------

Please do not report security issues in public. Please email security@edx.org.

Getting Help
------------

Have a question about this repository, or about Open edX in general?  Please
refer to this `list of resources`_ if you need any assistance.

.. _list of resources: https://open.edx.org/getting-help


.. |pypi-badge| image:: https://img.shields.io/pypi/v/custom-unit-icons.svg
    :target: https://pypi.python.org/pypi/custom-unit-icons/
    :alt: PyPI

.. |travis-badge| image:: https://travis-ci.org/edx/custom-unit-icons.svg?branch=master
    :target: https://travis-ci.org/edx/custom-unit-icons
    :alt: Travis

.. |codecov-badge| image:: http://codecov.io/github/edx/custom-unit-icons/coverage.svg?branch=master
    :target: http://codecov.io/github/edx/custom-unit-icons?branch=master
    :alt: Codecov

.. |doc-badge| image:: https://readthedocs.org/projects/custom-unit-icons/badge/?version=latest
    :target: http://custom-unit-icons.readthedocs.io/en/latest/
    :alt: Documentation

.. |pyversions-badge| image:: https://img.shields.io/pypi/pyversions/custom-unit-icons.svg
    :target: https://pypi.python.org/pypi/custom-unit-icons/
    :alt: Supported Python versions

.. |license-badge| image:: https://img.shields.io/github/license/edx/custom-unit-icons.svg
    :target: https://github.com/edx/custom-unit-icons/blob/master/LICENSE.txt
    :alt: License
