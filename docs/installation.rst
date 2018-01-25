Django
------

In `settings.py`, add a `loader` to `TEMPLATES` like so:

.. code:: python

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                os.path.join(BASE_DIR, 'templates')
            ],
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
                'loaders': [
                    # PyPugJS part:   ##############################
                    ('pypugjs.ext.django.Loader', (
                        'django.template.loaders.filesystem.Loader',
                        'django.template.loaders.app_directories.Loader',
                    ))
                ],
                'builtins': [
                    'pypugjs.ext.django.templatetags',
                ],
            },
        },
    ]

In case you want to use Djangos translation feature, be sure to put this import statement at the top of your settings.py.

    import pypugjs.ext.django  # noqa


Jinja2
------

Just add `pypugjs.ext.jinja.PyPugJSExtension` as extension

.. code:: python

    jinja_env = Environment(extensions=['pypugjs.ext.jinja.PyPugJSExtension'])


Mako
----

Just add  `pypugjs.ext.mako.preprocessor` as preprocessor

.. code:: python

    from pypugjs.ext.mako import preprocessor as mako_preprocessor
    mako.template.Template(haml_source,
        preprocessor=mako_preprocessor
    )


Flask
-----

Just add  `pypugjs.ext.jinja.PyPugJSExtension` as extension to the environment of the app

.. code:: python

    app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')


Pyramid
-------

Adjust your "your_project/__init__.py" and add the following line somewhere to in the main() function

.. code:: python

    config.include('pypugjs.ext.pyramid')


Tornado Templates
-----------------

Append this after importing tornado.template

.. code:: python

    from tornado import template
    from pypugjs.ext.tornado import patch_tornado
    patch_tornado()

    (...)
