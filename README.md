# PyPugJS [![Build Status](https://travis-ci.org/matannoam/pypugjs.svg)](https://travis-ci.org/matannoam/pypugjs)

**PyPugJS is just a fork of [PyJade](https://github.com/syrusakbary/pyjade) with the name Jade changed to [PugsJS](https://github.com/pugjs/pug).**

PyPugJS is a high performance port of PugJS for python, that converts any .pug source to the each Template-language (Django, Jinja2, Mako or Tornado).


UTILITIES
=========
To simply output the conversion to your console:

```console
pypugjs [-c django|jinja|mako|tornado] input.pug [output.html]
```

or, alternatively:

```console
pypugjs [-c django|jinja|mako|tornado] [-o output.html] < input.pug
```

To convert directly inside a python script:

```
import pypugjs
pugjs_text = '''!!! 5
html
head
    body foo bar!
'''
print pypugjs.simple_convert(pugjs_text)

```


INSTALLATION
============

First, you must do:

```console
pip install pypugjs
```

Or:

```console
python setup.py install
```

Now simply **name your templates with a `.pug` extension** and this pugjs compiler
will do the rest.  Any templates with other extensions will not be compiled
with the pypugjs compiler.


Django
------

**For Django 1.9**

In `settings.py`, add a `loader` to `TEMPLATES` like so:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request'
            ],
            'loaders': [
                # PyPugJS part:   ##############################
                ('pypugjs.ext.django.Loader', (
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ))
            ],
            'builtins': ['pypugjs.ext.django.templatetags'],
        },
    },
]
```

**For Django 1.8**

In `settings.py`, add a `loader` to `TEMPLATES` like so:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request'
            ],
            'loaders': [
                # PyPugJS part:   ##############################
                ('pypugjs.ext.django.Loader', (
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ))
            ],
        },
    },
]
```

**Or, in Django 1.7 or earlier:**

In `settings.py`, modify `TEMPLATE_LOADERS` like:

```python
TEMPLATE_LOADERS = (
    ('pypugjs.ext.django.Loader',(
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)
```

Jinja2
------

Just add `pypugjs.ext.jinja.PyPugJSExtension` as extension:

```python
jinja_env = Environment(extensions=['pypugjs.ext.jinja.PyPugJSExtension'])
```

Mako
----

Just add  `pypugjs.ext.mako.preprocessor` as preprocessor:

```python
from pypugjs.ext.mako import preprocessor as mako_preprocessor
mako.template.Template(pugjs_source,
    preprocessor=mako_preprocessor
)
```

Flask
-----

Just add  `pypugjs.ext.jinja.PyPugJSExtension` as extension to the environment of the app::

```python
app.jinja_env.add_extension('pypugjs.ext.jinja.PyPugJSExtension')
```

Pyramid
-------

Adjust your "your_project/__init__.py" and add the following line somewhere to in the main() function:

```python
config.include('pypugjs.ext.pyramid')
```

Tornado Templates
-----------------

Append this after importing tornado.template

```python
from tornado import template
from pypugjs.ext.tornado import patch_tornado
patch_tornado()

(...)
```

Syntax
======

Generally the same as the PugJS Node.js module (except of cases and several other features, which are not implemented)
https://github.com/pugjs/pug/blob/master/README.md


Example
-------

This code:

```jade
!!! 5
html(lang="en")
  head
    title= pageTitle
    script(type='text/javascript').
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
```


Converts to:

```html
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
```

Register filters
================

If you want to register a function as a filter, you only have to
decorate the function with `pypugjs.register_filter("filter_name")`

```python
import pypugjs

@pypugjs.register_filter('capitalize')
def capitalize(text,ast):
  return text.capitalize()
```

### Using templatetags (and any feature of the compiled-to language)

*Using Django and crispy-forms as an illustrative example but the information
can be generalized.*

If you need to use templatetags, you can use PugJS's syntax for rendering code:

```jade
- load crispy_forms_tags
- crispy form
```

This will compile into

```html
{% load crispy_forms_tags %}
{% crispy form %}
```

If you have any trouble with this feature, or there's some feature of your
template language that is being misinterpreted when using this syntax, you
can also do something like this:

```jade
| {% load crispy_forms_tags %}
| {% crispy form %}
```

This will compile into the same Django template snippet.

TESTING
=======

You must have `nose` package installed.
You can do the tests with

```console
./test.sh
```


TODOs and BUGS
==============
See: http://github.com/matannoam/pypugjs/issues
