==================
django-moreloaders
==================

Additional template loaders for Django.

Right now, only one additional ``Loader`` is provided -
``mostlycached.Loader``.

What the ...
------------

``mostlycached.Loader`` is a subclass of the standard `cached.Loader`_ with
a focus on explicitly *not* caching certain templates, if they match a
developer-defined regular expression.


Why would you ...
-----------------

Well, because I'm seriously considering loading certain configuration at
runtime, and allowing template authors to control certain aspects.

Beyond that, it's concievable that it could work for allowing using the
`cached.Loader`_ in development and just setting ``MOSTLYCACHED_EXCLUDES``
to something like::

    MOSTLYCACHED_EXCLUDES = (
        r'^*+$',
    )


How to ...
----------

Install it
^^^^^^^^^^

Right now, ``git clone`` (or ``pip install -e``) is the only way to do so.

Shove ``moreloaders`` onto your Python Path however you choose, and then
change your Django settings to::

    TEMPLATE_LOADERS = (
        ('moreloaders.mostlycached.Loader', (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        )),
    )

Without any further configuration, this should be identical in behaviour to::

    TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader', (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        )),
    )

Uncache certain extensions
^^^^^^^^^^^^^^^^^^^^^^^^^^

Set your ``MOSTLYCACHED_EXCLUDES`` to something like::

    MOSTLYCACHED_EXCLUDES = (
        r'^.+\.json$',
    )

Where in this case, I'm excluding JSON filetypes from being cached; each time
a JSON file is requested via the template system, it will be re-compiled.

Uncache certain folders
^^^^^^^^^^^^^^^^^^^^^^^

Set your ``MOSTLYCACHED_EXCLUDES`` to something like::

    MOSTLYCACHED_EXCLUDES = (
        r'^myapp/includes/.+$',
    )

As you can see, being a regular expression, there's a reasonable amount of
flexibility in what you can exclude.

Settings
--------

``MOSTLYCACHED_EXCLUDES`` - an iterable of regular expressions (expressed as
raw strings, please!) which should *not* be cached by the `cached.Loader`_.

License
-------

``django-moreloaders`` is available under the terms of the
Simplified BSD License (alternatively known as the FreeBSD License, or
the 2-clause License). See the ``LICENSE`` file in the source
distribution for a complete copy.

.. _cached.Loader: https://docs.djangoproject.com/en/stable/ref/templates/api/#django.template.loaders.cached.Loader
