.. highlight:: shell

============
Installation
============


Stable release
--------------

To install Wagtail Form Blocks, run this command in your terminal:

.. code-block:: console

    $ pip install wagtailformblocks

This is the preferred method to install Wagtail Form Blocks, as it will always install the most recent stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


From sources
------------

The sources for Wagtail Form Blocks can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/tleguijt/wagtailformblocks

Or download the `tarball`_:

.. code-block:: console

    $ curl  -OL https://github.com/tleguijt/wagtailformblocks/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python setup.py install

Configure Django
----------------

Add ``wagtailformblocks`` and ``wagtail.wagtailforms`` to your ``INSTALLED_APPS`` in settings:

.. code-block:: python

    INSTALLED_APPS += [
        'wagtailformblocks',
        'wagtail.wagtailforms',
    ]

Add ``wagtailformblocks.url`` to your url config to enable the form processing views:

.. code-block:: python

    from wagtailformblocks import urls as wagtailformblock_urls

    urlpatterns = [
        ...
        url(r'^forms/', include(wagtailformblock_urls)),
        ...
    ]

.. _Github repo: https://github.com/tleguijt/wagtailformblocks
.. _tarball: https://github.com/tleguijt/wagtailformblocks/tarball/master
