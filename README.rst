=======
PyPugJS
=======

**PyPugJS is a fork of** `PyJade <http://github.com/syrusakbary/pyjade>`_
**with the name Jade changed to** `PugsJS <https://github.com/pugjs/pug>`_.

**Additional disclaimer:** Since the original pypugjs died i took the liberty to keep it alive, because
since starting to work with the jade compile for node i hate writing HTML and want to continue using it in my Django projects.
I will keep the existing non Django stuff inside the project but i will only continue to support Django myself.
Tornado, Mako etc. support will be welcome tho!

PyPugJS is a high performance port of PugJS for python, that converts any .pug source into different
Template-languages (Django, Jinja2, Mako or Tornado).

UTILITIES
=========
To simply output the conversion to your console::

    pypugjs [-c django|jinja|mako|tornado] input.pug [output.html]


INSTALLATION
============

To install pypugjs::

    pip install pypugjs

Or::

    python setup.py install

Now simply **name your templates with a `.pug` extension** and this PugJS compiler
will do the rest.  Any templates with other extensions will not be compiled
with the pypugjs compiler.


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


Syntax
======

Generally the same as the PugJS Node.js module (except of cases and several other features, which are not implemented)
https://github.com/pugjs/pug/blob/master/README.md


Example
-------

This code

.. code:: jade

    !!! 5
    html(lang="en")
      head
        title= pageTitle
        script(type='text/javascript')
          if (foo) {
             bar()
          }
      body
        h1.title PugJS - node template engine
        #container
          if youAreUsingPugJS
            p You are amazing
          else
            p Get on it!


Converts to

.. code:: html

    <!DOCTYPE html>
    <html lang="en">
      <head>
        <title>{{pageTitle}}</title>
        <script type='text/javascript'>
          if (foo) {
             bar()
          }
        </script>
      </head>
      <body>
        <h1 class="title">PugJS - node template engine</h1>
        <div id="container">
          {%if youAreUsingPugJS%}
            <p>You are amazing</p>
          {%else%}
            <p>Get on it!</p>
          {%endif%}
        </div>
      </body>
    </html>


Register filters
================

If you want to register a function as a filter, you only have to
decorate the function with ``pypugjs.register_filter("filter_name")``

.. code:: python

    import pypugjs

    @pypugjs.register_filter('capitalize')
    def capitalize(text,ast):
      return text.capitalize()


TESTING
=======

You must have `nose` package installed.
You can do the tests with::

    ./test.sh


TODOs and BUGS
==============
See: https://github.com/kakulukia/pypugjs/issues
