custom-unit-icons
=============================

An Open edX Django plugin application for getting XBlock icons from modulestore. This allows customizing icon for each unit.

Setup Instructions
------------------------

On Open edX Devstack:

#. Clone this repo into your devstack's ``src`` folder:

    .. code-block:: bash

        git clone git@github.com/open-craft/custom-unit-icons.git

#. Install it into LMS's and Studio's devstack python environment:

    .. code-block:: bash

        make lms-shell
        pip install -e /edx/src/custom-unit-icons/
        logout

        make studio-shell
        pip install -e /edx/src/custom-unit-icons/
        logout

#. Set the following variables in either:

    a. ``/edx/etc/lms.yml``:

        .. code-block:: yaml

            GET_UNIT_ICON_IMPL: custom_unit_icons.icons.get_icon
            XBLOCK_EXTRA_MIXINS:
                - custom_unit_icons.icons.IconOverrideMixin

    #. ``lms/envs/private.py``:

        .. code-block:: python

            from .common import XBLOCK_MIXINS
            GET_UNIT_ICON_IMPL = 'custom_unit_icons.icons.get_icon'
            XBLOCK_MIXINS += ('custom_unit_icons.icons.IconOverrideMixin',)

#. Restart LMS:

    .. code-block:: bash

        make lms-restart

Usage instructions
-------------------

You need to override Studio theme to be able to modify icons for units.

If you want to modify an icon manually, you can use the following snippet via Django shell:

.. code-block:: python

    from xmodule.modulestore.django import modulestore
    from opaque_keys.edx.keys import UsageKey

    usage_key = UsageKey.from_string('block-v1:edX+DemoX+Demo_Course+type@vertical+block@vertical_0270f6de40fc')
    item = modulestore().get_item(usage_key)
    item.icon_override = 'video'
    modulestore().update_item(item, 1)

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
